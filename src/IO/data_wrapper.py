from models.modules import Modules

class DLWrapper:
    def load_tournaments() -> list[Modules.Tournament]:
        pass

    def save_tournaments(tournaments: list[Modules.Tournament]):
        pass

    def load_matches() -> list[Modules.Match]:
        pass

    def save_matches(matches: list[Modules.Match]):
        pass

    def load_teams() -> list[Modules.Team]:
        pass

    def save_teams(teams: list[Modules.Team]):
        pass

    def load_clubs() -> list[Club]:
        pass

    def save_clubs(clubs: list[Club]):
        pass

    def load_players() -> list[Player]:
        pass

    def save_players(players: list[Player]):
        pass

