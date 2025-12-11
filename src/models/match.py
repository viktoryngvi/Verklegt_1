from models.team import Team
from models.event import Event

class Match(Event):
    def __init__(self, id: int = None, teams: list[Team] = None, result_score: str = None, winner: Team = None,
                 schedule_time: str = "" , server_id: str = "",tournament_name: str = None, event_name: str = None ):
        self.id = id
        self.teams = teams
        self.result_score = result_score
        self.winner = winner
        self.schedule_time = schedule_time
        self.server_id = server_id
        self.tournament_name = tournament_name
        self.event_name = event_name


        # TODO skrifa þetta inn í event modelið
        # tournament,event_name,game_type,server_id,
        # match_id,date_of_match,time_of_match,team_a,team_b,
        # team_a_score,team_b_score,winner,match_result