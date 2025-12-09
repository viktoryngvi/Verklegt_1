from models.team import Team

class Match:
    def __init__(self, id: int, team_a: Team, team_b: Team, result_score: str, winner: Team = None,
                 schedule_time: str = "", server_id: str = ""):
        
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.result_score = result_score
        self.winner = winner
        self.schedule_time = schedule_time
        self.server_id = server_id
# breyta team_a og team_b bara í lista af liðum