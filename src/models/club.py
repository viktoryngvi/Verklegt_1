from models.team import Team
class Club:
    def __init__(self, name: str, home_town: str, country: str, color: list, teams: list[Team]):
        self.name = name
        self.home_town = home_town
        self.country = country
        self.color = color
        self.teams = teams

