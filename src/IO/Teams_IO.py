from models.team import Team
from csv import DictReader
from IO.Player_IO import Player_IO

class Team_IO(Team):
    def __init__(self,):
        self.file_path = "data/teams.csv"

    def create_team(self, name, captain_id, list_of_player_ids):
        """Takes three variables team_name, team_captain-in id, list af player_id´s and writes it into 
        the teams.csv file"""
        with open(self.file_path, "a", encoding="utf-8") as teams_file:
            captain_handle = Player_IO.take_id_return_handle(captain_id)
            teams_file.write(f"{name},{captain_handle},")
            for player_id in list_of_player_ids:
                player_handle = Player_IO.take_id_return_handle(player_id)
                teams_file.write(player_handle)
            teams_file.write("\n")
        return "Done!"


    # def take_player_ids_return_handles(self, player_list_of_ids):
    #     player_list = Player_IO.load_all_player_info()
    #     list_of_handles = []
    #     for id in player_list_of_ids:
    #         for player in player_list:
    #             if id == int(player["id"]):
    #             list_of_handles.append(player["handle"])
    #     return list_of_handles
    # TODO nota ég þetta eitthvað?????????

        






    def change_team_captain(self, find_team, new_captain):
        """This checks all team captains and compares them with the inputted captains, then updates
        the captain value and finds the inputted new team captain in the team and makes him the new captain"""
        with open(self.file_path, "r", encoding="utf-8") as teams_file:
            csv_reader = DictReader(teams_file)
            teams_list = list(csv_reader)
        # býr til lista af dicts af liðunum
            for each_dict in teams_list:
                team_name =str(each_dict["team"])
                if team_name == find_team:
                    each_dict["captain"] = new_captain
        # finnur réttan captain og breytir honum í capteinin

        with open(self.file_path, "w", encoding="utf-8") as teams_file:
            teams_file.write("team,captainhandle,player1handle,player2handle,player3handle,player4handle,player5handle")
            for each_dict in teams_list:
                teams_file.write(",".join(each_dict.values()))
                teams_file.write("\n")
        # skrifar það aftur í skránna
        return "Successfully changed team captain"



    def view_all_teams(self):
        """checks all teams and their captain and returns a list of dicts of teams""" #TODO
        with open (self.file_path, "r", encoding="utf-8") as teams_file:
            csv_reader = DictReader(teams_file)
            teams_list = list(csv_reader)
        return teams_list


    def view_all_teams_name_and_captains(self):
        all_teams = self.view_all_teams()
        list_of_team_name_and_captain_name = []
        for team in all_teams:
            list_of_team_name_and_captain_name.append({"team": team["team"], "captain": team["captain"]})
        return list_of_team_name_and_captain_name


    def players_team_none(self):
        """opens a file and returns a list of players short info
            that have not yet been assigned to a team"""
        list_of_non_team_players_short_info = []
        all_players = Player_IO.load_all_player_info()
        for players in all_players:
            if players["team"] == None:
                filtered_player = {"id":players["id"], "name": players["name"], "handle": players["handle"]}
                list_of_non_team_players_short_info.append(filtered_player)
        return list_of_non_team_players_short_info
            
            
    def view_all_players_in_team(self, team_find_name):
        """views_all_teams() and select a team and returns all players in  said team"""
        all_teams = self.view_all_teams()
        for team in all_teams:
            if team["team"] == team_find_name:
                return team
    
    def check_if_team_name_exists(self, team_name):
        all_teams = self.view_all_teams()
        for teams in all_teams:
            if teams["team"] == team_name:
                return True
        return False
    
    def check_if_player_handle_in_team(self, team, handle):
        players_in_team = self.view_all_players_in_team(team)
        for handles_in_team in players_in_team[2:]:
            if handles_in_team == handle:
                return True
        return False