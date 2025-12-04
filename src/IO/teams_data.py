from models.team import Team
from csv import DictReader

class Team_IO(Team):
    def __init__(self, name, captain, players):
        file_path = "data/teams.csv"
        self.file_path = file_path

    def create_team(self):
        with open(self.file_path, "a", encoding="utf-8") as teams_file:
            teams_file.write(f"{self.name},{self.captain},{self.players}")
        
        

    def change_team_captain(self):#############TODO
        with open(self.file_path, "w", encoding="utf-8") as teams_file:
            for line in teams_file:
                if team_name == self.name:

        return players in team

    def view_all_teams(self):
        with open ("data/teams.csv", "r", encoding="utf-8") as teams_file:
            teams_list = []
            for line in teams_file:
                 teams_list.append(line.split(",")[0])
        return teams_list
            
    def view_all_players_in_teams(self):

    
























# from typing import List


# class TeamsData:
#     """
#     Minimal data-layer class for loading teams from a local CSV/text file.
#     """

#     def __init__(self, filepath: str) -> None:
#         self.filepath: str = filepath
#         self.teams: List[str] = []

#     def load_teams(self) -> List[str]:
#         """Load team names from the local file and return them as a list."""
#         self.teams = []  # reset in case loaded before

#         with open(self.filepath, "r", encoding="utf-8") as file:
#             for line in file:
#                 name: str = line.strip()
#                 if name:  # ignore empty lines
#                     self.teams.append(name)

#         return self.teams
