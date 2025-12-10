# models/event.py

from models.team import Team
# from models.match import Match

class Event:
    def __init__(self, tournament_name: str = None, name :str = None, game_type: str = None, start_date: str = None,
                  end_date: str = None, team: list[Team] = None):
        
        self.tournament_name = tournament_name 
        self.name = name
        self.game_type = game_type
        self.start_date = start_date
        self.end_date = end_date
        self.team = team # 16 liði