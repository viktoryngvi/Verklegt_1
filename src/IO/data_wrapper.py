
# IO/data_wrapper.py

from __future__ import annotations

import os
import csv
from typing import List, Optional

from models.player import Player
from models.tournament import Tournament
from IO.Player_IO import Player_IO
from IO.event_io import EventIO
from IO.tournament_io import TournamentIO
from IO.tournament_schedule_io import TournamentScheduleIO


class DLWrapper:
    """
    Data-Layer Wrapper

    This class is the ONLY thing the Logic Layer should talk to in the Data Layer.
    It hides all file details and IO classes.
    """

    def __init__(self) -> None:
        # Underlying IO helpers / Create objects
        self._player_io = Player_IO()
        self._event_io = EventIO()
        self._tournament_io = TournamentIO()
        self._schedule_io = TournamentScheduleIO()

        # Point to data/teams.csv
        self._teams_file_path = os.path.join("data", "teams.csv")

    # ------------------------------------------------------------------
    # PLAYER METHODS
    # ------------------------------------------------------------------

    def create_player(self, player: Player) -> str:
        """
        Store a new player in the data store.
        Returns what Player_IO.create_player() returns.
        """
        return self._player_io.create_player(player) # Uses the model class: player.py

    def get_all_players(self) -> List[dict]:
        """
        Return all players as a list of dicts.
        """
        return self._player_io.load_all_player_info()

    def check_if_player_exists(self, name: str) -> bool:
        """
        Returns True if any player with this name exists in storage.
        """
        players = self._player_io.load_all_player_info()
        for row in players:
            if row.get("name") == name:
                return True
        return False

    def check_if_handle_exists(self, handle: str) -> bool:
        """
        Returns True if any player with this handle exists in storage.
        Used by PlayerLL.check_player_handle().
        """
        players = self._player_io.load_all_player_info()
        for row in players:
            if row.get("handle") == handle:
                return True
        return False

    def edit_player_info(self, player_name: str, email: str, phone: str) -> bool:
        """
        Update basic info for a single player, identified by name.

        NOTE: This is intentionally implemented here instead of relying on the
        incomplete Player_IO.edit_player_info(). This keeps DLWrapper stable even
        while Player_IO is still work in progress.
        """
        file_path = self._player_io.file_path

        if not os.path.exists(file_path):
            return False

        # Read all rows
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames

        if not fieldnames:
            # File is malformed / no header
            return False

        # Modify the matching player
        updated = False
        for row in rows:
            if row.get("name") == player_name:
                if email is not None:
                    row["email"] = email
                if phone is not None:
                    row["phone"] = phone
                updated = True

        if not updated:
            return False

        # Write back to file
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        return True

    # ------------------------------------------------------------------
    # TEAM METHODS (WIP / SAFE STUBS)
    # ------------------------------------------------------------------

    def check_if_team_exists(self, team_name: str) -> bool:
        """
        Returns True if a team with this name exists in teams.csv.

        This is a minimal implementation so PlayerLL.check_player_team() can work.
        You can later replace this with a proper Team_IO wrapper if you refactor teams_data.py.
        """
        if not os.path.exists(self._teams_file_path):
            return False

        with open(self._teams_file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                # Expecting format: name,captain,players,...
                if row and row[0] == team_name:
                    return True

        return False

    def get_team(self, team_name: str) -> Optional[dict]:
        """
        TODO: Implement properly once team storage format is finalized.

        Expected return shape for TeamLL:
            {
                "name": str,
                "captain": str,
                "players": [str, ...]
            }

        For now this returns None so TeamLL.change_captain() will reply "Team not found".
        """
        # Placeholder implementation – safe but not yet functional.
        return None

    def update_captain(self, team_name: str, new_captain: str) -> bool:
        """
        TODO: Implement when team CSV format is fixed.

        Should locate the team in teams.csv and update the captain field.
        """
        # Placeholder implementation
        return False

    # ------------------------------------------------------------------
    # TOURNAMENT METHODS
    # ------------------------------------------------------------------

    def create_tournament(self, tournament: Tournament) -> bool:
        """
        Persist a new tournament using TournamentIO.

        LL (TournamentLL) is responsible for validation before calling this.
        """
        return self._tournament_io.save_tournament(tournament)

    def load_tournament(self, name: str) -> Optional[Tournament]:
        """
        Load a single tournament by name.
        """
        return self._tournament_io.load_tournament(name)

    def list_tournaments(self) -> List[str]:
        """
        Return a list of all stored tournament names.
        Useful for menus like 'view schedule' or 'enter results'.
        """
        return self._tournament_io.list_tournaments()

    # ------------------------------------------------------------------
    # EVENT / SCHEDULE METHODS
    # ------------------------------------------------------------------

    def save_event(self, tournament_name: str, event) -> bool:
        """
        Save Event + Matches into CSV (delegated to EventIO).
        """
        return self._event_io.save_event(tournament_name, event)

    def load_event(self, tournament_name: str):
        """
        Load Event + Matches from CSV (delegated to EventIO).
        Returns an Event or None.
        """
        return self._event_io.load_event(tournament_name)

    def save_schedule(self, tournament_name: str, event) -> bool:
        """
        Optional: alternative way to store the schedule using TournamentScheduleIO.

        If you decide to standardize on EventIO only, you can remove this later.
        """
        return self._schedule_io.save_schedule(tournament_name, event)
