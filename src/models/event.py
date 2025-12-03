from models.team import Team
from models.match import Match

class Event:
    def __init__(self, name: str, game_type: str, teams: list[Team], matches: list[Match]):
        self.name = name
        self.game_type = game_type
        self.teams = teams
        self.matches = matches
        pass