from models.player import Player

class Team:
    def __init__(self, id: int = None, name: str = None, captain: str = None, players: list[str] = None):
        self.id = id
        self.name = name
        self.captain = captain
        self.players = players
