from models.person import Person

class Organiser(Person):
    def __init__(self, id: int):
        super().__init__()
        self.id = id
