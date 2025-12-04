from models.person import Person
from models.event import Event

class Tournament:
    def __init__(self, name: str, type: str, location: str, start_date: str, end_date: str, contact_person: Person, events: list[Event]):
        self.name = name
        self.type = type
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.contact_person = contact_person
        self.events = events
        pass