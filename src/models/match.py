from models.team import Team

class Match():
    def __init__(
            self,
            tournament_name: str = None, 
            event_name: str = None ,
            game_type: str = None,
            server_id: str = None,
            match_id: str = None,
            bracket_nr: int = None,
            date_of_match: str = None,
            time_of_match: str = None,
            teams: list[Team] = None,
            team_a: Team = None,
            team_b: Team = None,
            team_a_score: int = None,
            team_b_score: int = None,
            winner: Team = None

        ):

        self.tournament_name = tournament_name
        self.event_name = event_name
        self.game_type = game_type
        self.server_id = server_id
        self.match_id = match_id
        self.bracket_nr = bracket_nr
        self.date_of_match = date_of_match
        self.time_of_match = time_of_match
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = team_a_score
        self.team_b_score = team_b_score
        self.teams = teams
        self.winner = winner
