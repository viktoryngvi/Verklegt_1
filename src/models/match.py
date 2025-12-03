from models.team import Team

class Match:
    def __init__(self, id: int, team_a: Team, team_b: Team, winner: Team, result_score: str, schedule_time: str, server_id: str ):
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.winner = winner 
        self.result_score = result_score
        self.schedule_time = schedule_time
        self.server_id = server_id