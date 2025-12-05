
import csv
import os
from models.tournament import Tournament

class TournamentIO:
    def __init__(self):
        self._tournament_file_path = os.path.join("data", "tournaments.csv")

        # Create file if missing
        if not os.path.exists(self._tournament_file_path):
            with open(self._tournament_file_path, "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "name", "location", "date"])

    def create_tournament(self, tournament: Tournament):
        with open(self._tournament_file_path, "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                tournament.tournament_id,
                tournament.name,
                tournament.location,
                tournament.date
            ])
        return tournament

    def load_all_tournaments(self):
        tournaments = []
        with open(self._tournament_file_path, "r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tournaments.append(Tournament(
                    int(row["id"]),
                    row["name"],
                    row["location"],
                    row["date"]
                ))
        return tournaments
