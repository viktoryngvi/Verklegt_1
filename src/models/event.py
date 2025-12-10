# models/event.py

from models.team import Team
from models.match import Match

class Event:
    def __init__(self, tournament_name: str, event_name :str, game_type: str, start_date: str, end_date: str, teams: list[Team], matches: list[Match]):
        self.tournament_name = tournament_name 
        self.event_name = event_name
        self.game_type = game_type
        self.start_date = start_date
        self.end_date = end_date
        self.teams = teams # 16 liði
        self.matches = matches 