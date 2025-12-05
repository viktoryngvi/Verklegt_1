import csv
import os
from IO.Player_IO import Player_IO
from IO.event_io import EventIO
from IO.tournament_io import TournamentIO   # <--- NEW

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.eventio = EventIO()
        self.tournamentio = TournamentIO()   # <--- NEW

    # -------------------------
    # Existing Player Methods
    # -------------------------
    def create_player(self, player: Player_IO):
        return self.playerio.create_player(player)

    def check_if_player_exists(self, player: Player_IO):
        return self.playerio.check_if_player_exists(player)
    
    def edit_player_info(self, player: Player_IO):
        return self.playerio.edit_player_info(player)
    
    def load_all_player_short_info(self, player: Player_IO):
        return self.playerio.load_all_player_short_info(player)
    
    def load_all_player_info(self, player: Player_IO):
        return self.playerio.load_all_player_info(player)
    


    def check_if_team_exists(self, player : Player_IO):
        return self

    def check_if_player_in_team(self, player : Player_IO):
        return self

    def check_if_handle_exists(self, player : Player_IO):
        return self.playerio.check_if_handle_exists(player)

    # (your TODO team-related stubs can stay as-is)

    # -------------------------
    # Event / Schedule Methods
    # -------------------------
    def save_event(self, tournament_name, event):
        """Save Event + Matches into CSV (delegated to EventIO)."""
        return self.eventio.save_event(tournament_name, event)

    def load_event(self, tournament_name):
        """Load Event + Matches from CSV (delegated to EventIO)."""
        return self.eventio.load_event(tournament_name)

    # -------------------------
    # NEW Tournament Methods
    # -------------------------
    def create_tournament(self, tournament):
        """Forward Tournament object to TournamentIO for creation."""
        return self.tournamentio.create_tournament(tournament)
    #TODO add more tournament methods as needed - KRISTO ADDED
    
    def save_tournament(self, tournament):
        """Forward Tournament object to TournamentIO for storage."""
        return self.tournamentio.save_tournament(tournament)

    def load_tournament(self, name: str):
        """Load one Tournament by name."""
        return self.tournamentio.load_tournament(name)

    def list_tournaments(self):
        """Return a list of stored tournament names."""
        return self.tournamentio.list_tournaments()
