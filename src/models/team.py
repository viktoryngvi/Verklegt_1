from models.player import Player
from models.captain import Captain

class Team:
    def __init__(self, name: str = None, captain: Captain = None, players: list[Player] = None):
        self.name = name
        self.captain = captain
        self.players = players
