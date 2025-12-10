from models.team import Team
from models.event import Event

class Match(Event):
    def __init__(self, id: int = None, teams: list[Team] = None, result_score: str = None, winner: Team = None,
                 schedule_time: str = "" , server_id: str = "" ):
        super().__init__(tournament_name = None, name = None)
        self.id = id
        self.teams = teams
        self.result_score = result_score
        self.winner = winner
        self.schedule_time = schedule_time
        self.server_id = server_id
        self.tournament_name = tournament_name  