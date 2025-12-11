# models/event.py
from datetime import date
# from models.match import Match

class Event:
    def __init__(
            self,  
            event_name :str = None, 
            event_type: str = None, 
            tournament_name: str = None,    
            start_date: date = None,
            end_date: date = None,
            team_name: str = None
        ):
        
        self.event_name = event_name
        self.event_type = event_type
        self.tournament_name = tournament_name 
        self.start_date = start_date
        self.end_date = end_date
        self.team_name = team_name # 16 liði
        
