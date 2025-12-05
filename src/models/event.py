# models/event.py

from models.team import Team
from models.match import Match

class Event:
    def __init__(self, name: str, game_type: str, teams: list[Team] = None, matches: list[Match] = None):
        self.name = name
        self.game_type = game_type
        self.teams = teams if teams is not None else []
        self.matches = matches if matches is not None else []
