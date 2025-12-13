from models.team import Team
from models.event import Event
from datetime import date


class Match():
    """MATCH CLASS REPRESENTS TOURNAMENT, EVENT, GAME TYPE, SERVER, TEAMS, SCORES, WINNER, AND MATCH DETAILS."""

    def __init__(
            self,
            tournament_name: str = None, 
            event_name: str = None ,
            game_type: str = None,
            server_id: str = None,
            match_id: str = None,
            bracket_nr: int = None,
            date_of_match: date = None,
            time_of_match: str = None,
            teams: list[str] = None,
            team_a: str = None,
            team_b: str = None,
            team_a_score: int = 0,
            team_b_score: int = 0,
            winner: str = None

        ):

        self.tournament_name = tournament_name
        self.event_name = event_name
        self.game_type = game_type
        self.server_id = server_id
        self.match_id = match_id
        self.bracket_nr = bracket_nr

        if date_of_match is None:
            self.date_of_match = date.today()
        else:
            self.date_of_match = date_of_match
        self.time_of_match = time_of_match
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = team_a_score
        self.team_b_score = team_b_score
        if  teams is None:
            self.teams = []
        else:
            self.teams = teams

        self.winner = winner

