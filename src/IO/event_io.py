# data/event_io.py

# models/event.py

import os
import csv

class EventIO:
    def __init__(self, name: str, game_type: str):
        self.name = name
        self.game_type = game_type
        self.matches = []

    def add_match(self, event_name: str, match):
        """
        Appends a single match row into data/matches.csv at the end of the file.
        """

        # Create file with header if it doesn't exist yet
        if not os.path.exists(self.matches_file):
            with open(self.matches_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "event_name",
                    "match_id",
                    "team_a",
                    "team_b",
                    "winner",
                    "server_id",
                    "schedule_time"
                ])

        # Append ONE match row
        with open(self.matches_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                event_name,
                match.id,
                match.team_a.name if match.team_a else "",
                match.team_b.name if match.team_b else "",
                match.winner.name if match.winner else "",
                match.server_id if match.server_id else "",
                match.schedule_time if match.schedule_time else ""
            ])

        return True
