from models.player import Player
from models.captain import Captain

class Team:
    def __init__(self, name: str, captain: Captain, players: list[Player]):
        self.name = name
        self.captain = captain
        self.players = players
