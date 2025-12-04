import os
import csv

from models.event import Event
from models.match import Match
from models.team import Team


class EventIO:
    """
    Data Layer class:
    Stores and loads data
    """

    def __init__(self, base_path="data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    # -----------------------------------------------------
    # SAVE EVENT (schedule)
    # -----------------------------------------------------
    def save_event(self, tournament_name: str, event: Event):
        """
        Saves an Event and all of its Matches into CSV files.
        """

        # 1. Save event metadata
        event_file = os.path.join(self.base_path, f"{tournament_name}_event.csv")

        with open(event_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["event_name", "game_type"])
            writer.writerow([event.name, event.game_type])

        # 2. Save matches
        matches_file = os.path.join(self.base_path, f"{tournament_name}_matches.csv")

        with open(matches_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "id",
                "round_name",
                "team_a",
                "team_b",
                "winner",
                "score",
                "server_id",
                "schedule_time"
            ])

            for m in event.matches:
                writer.writerow([
                    m.id,
                    m.round_name,
                    m.team_a.name if m.team_a else "",
                    m.team_b.name if m.team_b else "",
                    m.winner.name if m.winner else "",
                    m.result_score if m.result_score else "",
                    m.server_id if m.server_id else "",
                    m.schedule_time if m.schedule_time else ""
                ])

        return True


    # -----------------------------------------------------
    # LOAD EVENT (schedule)
    # -----------------------------------------------------
    def load_event(self, tournament_name: str):
        """
        Loads an Event and all its Matches from CSV.
        Returns an Event object containing Match objects.
        """

        event_file = os.path.join(self.base_path, f"{tournament_name}_event.csv")
        matches_file = os.path.join(self.base_path, f"{tournament_name}_matches.csv")

        # If no saved event exists
        if not os.path.exists(event_file) or not os.path.exists(matches_file):
            return None

        # 1. Load event metadata
        with open(event_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = next(reader)
            event_name = data["event_name"]
            game_type = data["game_type"]

        # 2. Load matches
        matches = []
        with open(matches_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Reconstruct team objects
                team_a = Team(row["team_a"]) if row["team_a"] else None
                team_b = Team(row["team_b"]) if row["team_b"] else None
                winner = Team(row["winner"]) if row["winner"] else None

                match = Match(
                    id=int(row["id"]),
                    team_a=team_a,
                    team_b=team_b,
                    winner=winner,
                    result_score=row["score"] if row["score"] else None,
                    server_id=row["server_id"] if row["server_id"] else None,
                    schedule_time=row["schedule_time"] if row["schedule_time"] else None,
                    round_name=row["round_name"]
                )

                matches.append(match)

        # Return Event object
        return Event(
            name=event_name,
            game_type=game_type,
            teams=None,        # LL will attach proper teams if needed
            matches=matches
        )
