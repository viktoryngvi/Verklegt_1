from models.person import Person
from models.event import Event
from models.contact_person import contact_person

class Tournament(contact_person):
    def __init__(self, name: str, location: str, start_date: str, end_date: str
                 , contact_name: str, contact_email: str,
                 contact_phone: str, tournament_id: int = None):
        super().__init__(contact_name,contact_email,contact_phone)
        
        
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date   
        self.end_date = end_date       
        # self.type = type_choice        


