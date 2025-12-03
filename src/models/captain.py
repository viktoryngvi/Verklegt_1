from models.player import Player

class Captain(Player):
    def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str, captain: bool = True):
        super().__init__(name, phone, address, dob, email, id, handle, captain)