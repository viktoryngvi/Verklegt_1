from models.person import Person
from models.event import Event
from models.contact_person import ContactPerson
from datetime import date

class Tournament(ContactPerson):
    """TOURNAMENT CLASS REPRESENTS NAME, LOCATION, START/END DATES, CONTACT INFO, AND EVENTS."""

    def __init__(
            self, 
            tournament_name: str = None,
            tournament_location: str = None,
            start_date: date = None,
            end_date: date = None,
            contact_name: str = None,
            contact_email: str = None,
            contact_phone: str = None,
            tournament_id: int = None,
            event_list: list[str] = None
            ):
        super().__init__(contact_name,contact_email,contact_phone)
        
        
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.start_date = start_date
        self.end_date = end_date
        self.event_list = event_list
        # self.type = type_choice


