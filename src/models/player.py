from models.person import Person

class Player(Person):
    def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str, team: None, captain: bool = False):
        super().__init__(name, phone, address, dob, email)
        self.handle = handle
        self.id = id
        self.captain = captain
        self.team = team
    def __str__(self):
        return 
    #Team hjá player byrjar sem None, sem þýðir að hann er ekki í neinu liði til að byrja með
    