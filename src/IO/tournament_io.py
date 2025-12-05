import csv
import os
from models.tournament import Tournament
from models.person import Person


class TournamentIO:
    """
    Handles storing and loading tournaments from tournaments.csv
    """

    def __init__(self):
        self.file_path = os.path.join("data", "tournaments.csv")
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "name",
                    "type",
                    "location",
                    "start_date",
                    "end_date",
                    "contact_name",
                    "contact_phone",
                    "contact_email"
                ])

    # ----------------------------------------------------------------------
    # SAVE TOURNAMENT
    # ----------------------------------------------------------------------
    def create_tournament(self, tournament: Tournament) -> bool:
        """Append a new tournament to the CSV file."""

        # Check if name exists
        if self._tournament_exists(tournament.name):
            return False

        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            cp = tournament.contact_person

            writer.writerow([
                tournament.name,
                tournament.type,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                cp.name if cp else "",
                cp.phone if cp else "",
                cp.email if cp else ""
            ])

        return True

    # ----------------------------------------------------------------------
    # LOAD ALL
    # ----------------------------------------------------------------------
    def load_all_tournaments(self):
        """Return a list of Tournament objects."""

        if not os.path.exists(self.file_path):
            return []

        tournaments = []

        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                contact = Person(
                    name=row["contact_name"],
                    phone=row["contact_phone"],
                    address=None,
                    dob=None,
                    email=row["contact_email"]
                )

                t = Tournament(
                    name=row["name"],
                    type=row["type"],
                    location=row["location"],
                    start_date=row["start_date"],
                    end_date=row["end_date"],
                    contact_person=contact,
                    events=[]
                )

                tournaments.append(t)

        return tournaments

    # ----------------------------------------------------------------------
    # EXISTS CHECK
    # ----------------------------------------------------------------------
    def _tournament_exists(self, name: str) -> bool:
        """Return True if tournament with this name already exists."""

        if not os.path.exists(self.file_path):
            return False

        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["name"] == name:
                    return True

        return False
