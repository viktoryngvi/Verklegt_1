from models.person import Person
from models.event import Event
from models.contact_person import contact_person

class Tournament(contact_person):
    def __init__(self, name: str = None, location: str = None, start_date: str = None, end_date: str = None
                 , contact_name: str = None, contact_email: str = None,
                 contact_phone: str = None, tournament_id: int = None):
        super().__init__(contact_name,contact_email,contact_phone)
        
        
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date   
        self.end_date = end_date       
        # self.type = type_choice        


