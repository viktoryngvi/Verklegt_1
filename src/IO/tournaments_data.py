
from pathlib import Path
from typing import List
import csv
import uuid

from .tournament import Tournament

DATA_DIR = Path("data")  # All data files stored here


class TournamentsData:
    """
    PURE IO-LAYER CLASS.
    Handles:
      - reading tournaments from CSV
      - writing tournaments to CSV
      - creating Tournament objects
    Contains NO logic-layer behavior.
    """

    def __init__(self, filename: str = "tournaments.csv"):
        self.filepath = DATA_DIR / filename
        self.tournaments: List[Tournament] = []

    def load_tournaments(self) -> List[Tournament]:
        """Loads all tournaments from CSV. NO validation at IO-level."""

        if not self.filepath.exists():
            self.tournaments = []
            return self.tournaments

        tournaments = []

        with self.filepath.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) != 8:
                    continue  # Skip malformed rows silently

                tournaments.append(Tournament(
                    id=row[0],
                    name=row[1],
                    start_date=row[2],
                    end_date=row[3],
                    venue=row[4],
                    contact_name=row[5],
                    contact_email=row[6],
                    contact_phone=row[7]
                ))

        self.tournaments = tournaments
        return tournaments

    def save_tournaments(self) -> None:
        """Write all tournaments to CSV."""
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

        with self.filepath.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            for t in self.tournaments:
                writer.writerow([
                    t.id, t.name, t.start_date, t.end_date, t.venue,
                    t.contact_name, t.contact_email, t.contact_phone
                ])

    def add_tournament(self, name: str, start_date: str, end_date: str,
                       venue: str, contact_name: str, contact_email: str,
                       contact_phone: str) -> Tournament:
        """
        Creates a new Tournament object and saves to CSV.
        NO validation. NO rule checking. PURE IO.
        """

        t = Tournament(
            id=str(uuid.uuid4()),
            name=name,
            start_date=start_date,
            end_date=end_date,
            venue=venue,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone
        )

        self.tournaments.append(t)
        self.save_tournaments()
        return t
