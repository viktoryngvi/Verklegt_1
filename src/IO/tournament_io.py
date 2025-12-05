import os
import csv
from typing import List, Optional

from models.tournament import Tournament
from models.person import Person

class TournamentIO:
    """
    Data Layer class for storing and loading Tournament metadata.

    Responsibilities:
    - Map Tournament <-> CSV rows
    - Never validate or apply business rules
    - Never touch UI or Logic classes
    """

    def __init__(self, base_path: str = "data") -> None:
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)
        self.file_path = os.path.join(self.base_path, "tournaments.csv")

    # -----------------------------
    # SAVE
    # -----------------------------
    def save_tournament(self, tournament: Tournament) -> bool:
        """
        Append (or create) a tournament row in tournaments.csv.
        DL does NOT check for duplicates or validate anything.
        """

        file_exists = os.path.exists(self.file_path)

        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # write header once
            if not file_exists:
                writer.writerow([
                    "name",
                    "type",
                    "location",
                    "start_date",
                    "end_date",
                    "contact_name",
                    "contact_phone",
                    "contact_email",
                ])

            cp = tournament.contact_person

            writer.writerow([
                tournament.name,
                tournament.type,
                tournament.location,
                tournament.start_date,
                tournament.end_date,
                cp.name if cp else "",
                cp.phone if cp else "",
                cp.email if cp else "",
            ])

        return True

    # -----------------------------
    # LOAD SINGLE TOURNAMENT
    # -----------------------------
    def load_tournament(self, name: str) -> Optional[Tournament]:
        """
        Load a single tournament by name.
        Returns a Tournament object, or None if not found.
        Events list is left as None/empty; LL will attach events.
        """

        if not os.path.exists(self.file_path):
            return None

        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row.get("name") == name:
                    contact = Person(
                        name=row.get("contact_name", ""),
                        phone=row.get("contact_phone", ""),
                        address=None,
                        dob=None,
                        email=row.get("contact_email", ""),
                    )

                    return Tournament(
                        name=row.get("name", ""),
                        type=row.get("type", ""),
                        location=row.get("location", ""),
                        start_date=row.get("start_date", ""),
                        end_date=row.get("end_date", ""),
                        contact_person=contact,
                        events=[]  # LL can later load events via EventIO
                    )

        return None

    # -----------------------------
    # LIST ALL TOURNAMENTS (for UI lists)
    # -----------------------------
    def list_tournaments(self) -> List[str]:
        """
        Return a list of all tournament names stored in tournaments.csv.
        Useful for 'view tournament schedule' menus in LL/UI.
        """

        if not os.path.exists(self.file_path):
            return []

        names: List[str] = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("name"):
                    names.append(row["name"])

        return names
