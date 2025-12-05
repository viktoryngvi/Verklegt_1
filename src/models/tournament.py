from models.person import Person
from models.event import Event

class Tournament:
    def __init__(self, tournament_id: int, name: str, venue: str, date_start: str, date_end: str, contact_pers: str, contact_mobile: str, contact_email: str):
        self.tournament_id = tournament_id
        self.name = name
        venue = venue
        self.date_star = date_start
        self.date_end = date_end
        self.contact_pers = contact_pers
        self.contact_mobile = contact_mobile
        self.contact_email = contact_email
        
    def __str__(self):
        return f"{self.tournament_id},{self.name},,{self.venue},{self.date_start},{self.date_end},{self.contact_pers},{self.contact_mobile},{self.contact_email}"
    
