from models.person import Person
from models.event import Event

class Tournament:
    def __init__(self, tournament_id: int, name: str, location: str, date: str):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.date = date

    def __str__(self):
        return f"{self.tournament_id},{self.name},{self.location},{self.date}"
