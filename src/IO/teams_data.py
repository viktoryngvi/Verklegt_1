from models.team import Team
from csv import DictReader
from IO.Player_IO import Player_IO

class Team_IO(Team):
    def __init__(self,):
        self.file_path = "data/teams.csv"

    def create_team(self):
        """Takes three variables team_name, team_captain, list af players and writes it into 
        the teams.csv file"""
        with open(self.file_path, "a", encoding="utf-8") as teams_file:
            teams_file.write(f"{self.name},{self.captain},{self.players}")
        
        






    def change_team_captain(self, find_team, new_captain):
        """This checks all team captains and compares them with the inputted captains, then updates
        the captain value and finds the inputted new team captain in the team and makes him the new captain"""
        with open(self.file_path, "w", encoding="utf-8") as teams_file:
            csv_reader = DictReader(teams_file)
            teams_list = list(csv_reader)

            for each_dict in teams_list:
                team_captain =str(each_dict[1])
                if self.captain == team_captain:
                    each_dict["captain"] = new_captain

            for each_dict in teams_list:
                teams_file.write(f"{teams_list[each_dict]},")
                teams_file.write("\n")
        return





        return players in team

    def view_all_teams(self):
        """checks all teams and their captain and returns a list""" #TODO
        with open (self.file_path, "r", encoding="utf-8") as teams_file:
            csv_reader = DictReader(teams_file)
            teams_list = list(csv_reader)
            teams_list = []
            for line in teams_file:
                 teams_list.append(line.split(",")[0])
        return teams_list
    
    def players_team_none(self):
        return list_of_non_team_players
            
    def view_all_players_in_team(self):
        """views_all_teams() and select a team and returns all players in  said team"""
        with open(self.file_path, "r", encoding="utf-8") as team_file:



    
























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
