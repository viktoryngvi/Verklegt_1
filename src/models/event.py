# models/event.py

from models.team import Team
from models.match import Match

class Event:
    def __init__(self, name: str, game_type: str, start_date: str, end_date: str, teams: list[Team], matches: list[Match]):
        self.name = name 
        self.game_type = game_type
        self.start_date = start_date
        self.end_date = end_date
        self.teams = teams # 16 liði