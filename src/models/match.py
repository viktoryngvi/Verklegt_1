
from models.team import Team

class Match:
    def __init__(self, id: int, team_a: Team, team_b: Team, winner: Team = None,
                 schedule_time: str = "", server_id: str = ""):
        
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.winner = winner
        self.schedule_time = schedule_time
        self.server_id = server_id
