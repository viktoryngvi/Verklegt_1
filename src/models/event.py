# models/event.py
from datetime import date
from models.team import Team
# from models.match import Match

class Event:
    def __init__(
            self, 
            team_name: str = None, 
            name :str = None, 
            event_type: str = None, 
            tournament_name: str = None,    
            start_date: date = None,
            end_date: date = None, 
        ):
        
        self.team_name = team_name # 16 liði
        self.name = name
        self.event_type = event_type
        self.tournament_name = tournament_name 
        self.start_date = start_date
        self.end_date = end_date
        
