from models.team import Team
class Club:
    def __init__(self, name: str = None, home_town: str = None, country: str = None, colors: list[str] = None, teams: list[str] = None):
        self.name = name
        self.home_town = home_town
        self.country = country
        self.colors = colors
        self.teams = teams
