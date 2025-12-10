from models.player import Player

class Team:
    def __init__(self, name: str = None, captain: Player.handle = None, players: list[Player] = None):
        self.name = name
        self.captain = captain
        self.players = players
