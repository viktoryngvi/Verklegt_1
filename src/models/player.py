from models.person import Person
from datetime import date

class Player(Person):
    def __init__(self, name: str = None, phone: str = None, address: str = None, dob: date = None,
                  email: str = None, id: int = None, handle: str = None, team: None = None):
        super().__init__(name, phone, address, dob, email)
        self.handle = handle
        self.id = id
        self.team = team
    def __str__(self):
        return 
    
    #Team hjá player byrjar sem None, sem þýðir að hann er ekki í neinu liði til að byrja með
    