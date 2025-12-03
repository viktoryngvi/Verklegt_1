from models.club import Club
from models.tournament import Tournament
from models.match import Match
from models.team import Team
from models.player import Player

class DLWrapper:
    def __init__(self):
        pass
    
    def load_tournaments() -> list[Tournament]:
        pass

    def save_tournaments(tournaments: list[Tournament]):
        pass

    def load_matches() -> list[Match]:
        pass

    def save_matches(matches: list[Match]):
        pass

    def load_teams() -> list[Team]:
        pass

    def save_teams(teams: list[Team]):
        pass

    def load_clubs() -> list[Club]:
        pass

    def save_clubs(clubs: list[Club]):
        pass

    def load_players() -> list[Player]:
        pass

    def save_players(players: list[Player]):
        pass

    
