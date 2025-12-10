from models.person import Person

class Player(Person):
    def __init__(self, name: str = None, phone: str = None, address: str = None, dob: str = None,
                  email: str = None, player_id: int = None, handle: str = None, team: str = None):
        super().__init__(name, phone, address, dob, email)
        self.handle = handle
        self.player_id = player_id
        self.team = team
    def __str__(self):
        return 
    #Team hjá player byrjar sem None, sem þýðir að hann er ekki í neinu liði til að byrja með
    