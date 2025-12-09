from models.team import Team

class Match:
    def __init__(self, id: int, teams: list[Team], result_score: str, winner: Team = None,
                 schedule_time: str = "", server_id: str = ""):
        
        self.id = id
        self.teams = teams
        self.result_score = result_score
        self.winner = winner
        self.schedule_time = schedule_time
        self.server_id = server_id