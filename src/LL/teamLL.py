from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from models.team import Team

class TeamLL:
    def __init__(self, dl_wrapper: DLWrapper, player_ll: PlayerLL):
        self._dl_wrapper = dl_wrapper
        self.player_ll = player_ll

    def create_team(self, cap_id: int, team_name: str, players_id: list):
        last_id = self.player_ll.check_last_id
        if cap_id > last_id:
            return "Captain id does not exist "
        
        check_team_name = self.check_if_team_name_exists(team_name)
        if check_team_name:
            return "Team name already exists"
        
        for player_id in players_id:
            if not self.player_ll.check_if_player_id_in_team(player_id): # check if the id of the player is not in the list of valid id 
                return "Player's id does not exist" 
            
        create_team = self.create_team_to_data(cap_id, team_name, players_id)
        return create_team

    def create_team_to_data(self, name, captain_id, list_of_player_ids):
        """Takes three variables team_name, team_captain-in id, list af player_id´s and writes it into 
        the teams.csv file"""
        teams_file = self._dl_wrapper.view_all_teams()
        captain_handle = self.player_ll.take_id_return_handle(captain_id)
        list_of_player_handles = []
        for player_id in list_of_player_ids:
            player_handle = self.player_ll.take_id_return_handle(player_id)
            list_of_player_handles.append(player_handle)
        team_model = Team(name, captain_handle, list_of_player_handles)
        teams_file.append(team_model)

        if self._dl_wrapper.write_team_into_file(teams_file):
            return "Successfully created Team"
        
        return "Team was not created"
    

    def view_all_teams(self):
        return self._dl_wrapper.view_all_teams()
   
    def view_all_players_in_team(self, team_name):
        return self.view_all_players_in_team(team_name)
    
    def change_team_captain(self, find_team, new_captain):
        teams_list = self._dl_wrapper.view_all_teams()
        for each_dict in teams_list:
            team_name =str(each_dict["team_name"])
            if team_name == find_team:
                each_dict["captain"] = new_captain
                if self._dl_wrapper.write_team_into_file(teams_list):
                    return "Team Captain successfully changed"
                
        return "Team does not exists"
    
    def view_all_team_names_and_captains(self):
        """returns all team names and cpatains of that team"""
        all_teams = self.view_all_teams()
        list_of_team_name_and_captain_name = []
        for team in all_teams:
            list_of_team_name_and_captain_name.append({"team_name": team["team_name"], "captain": team["captain"]})
        return list_of_team_name_and_captain_name

    def players_team_none(self):
        """opens a file and returns a list of players short info
            that have not yet been assigned to a team"""
        list_of_non_team_players_short_info = []
        all_players = self._dl_wrapper.load_all_player_info()
        for players in all_players:
            if players["team_name"] == None:
                filtered_player = {"id":players["id"], "name": players["name"], "handle": players["handle"]}
                list_of_non_team_players_short_info.append(filtered_player)
        return list_of_non_team_players_short_info

    def view_all_players_in_team(self, team_name):
        """views_all_teams() and select a team and returns all players in  said team"""
        all_teams = self.view_all_teams()
        players_in_team = []
        for team in all_teams:
            if team["team_name"] == team_name:
                for players in team["players"]:
                    players_in_team.append(players)
                return players_in_team

    def view_captains_team(self, find_captain_handle):
        """views_all_teams() and select a team and returns all players in  said team"""
        all_teams = self.view_all_teams()
        for team in all_teams:
            if team["handle"] == find_captain_handle:
                return team

    def check_if_team_name_exists(self, team_name):
        """takes a team name and checks if that team name is already in use"""
        all_teams = self.view_all_teams()
        for teams in all_teams:
            if teams["team_name"] == team_name:
                return True
        return False

    def check_if_player_handle_in_team(self, team, handle):
        """takes a player handle and checks if that player handle is in the team"""
        players_in_team = self.view_all_players_in_team(team)
        if not players_in_team:
            return "No players in this team"
        for handles_in_team in players_in_team[2:]:
            if handles_in_team == handle:
                return True
        return False
    
    def view_captain_team_by_team_name(self, team_name):
        team_file = self.view_all_teams()
        for line in team_file:
            if line["team_name"] == team_name:
                return line["captain"]
        return "Team does not exist"
    

