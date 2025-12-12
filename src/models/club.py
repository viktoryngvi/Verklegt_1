from models.team import Team
class Club:
    """ CLUB CLASS REPRESENTS NAME, HOME TOWN, COUNTRY, COLORS, AND TEAMS. """

    def __init__(self, name: str, home_town: str, country: str, color: list, teams: list):
        self.name = name
        self.home_town = home_town
        self.country = country
        self.color = color
        self.teams = teams
