from models.player import Player

class Team:
    """TEAM CLASS REPRESENTS TEAM ID, NAME, CAPTAIN, AND PLAYERS."""
    
    def __init__(self, id: int = None, name: str = None, captain: str = None, players: list[str] = None):
        self.id = id
        self.name = name
        self.captain = captain
        self.players = players
    def __repr__(self):
        return f"Team({self.name})"