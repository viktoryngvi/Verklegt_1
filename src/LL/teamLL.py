from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from models.team import Team
from models.player import Player

class TeamLL:
    """LOGICAL LAYER FOR TEAM MANAGEMENT AND VALIDATION"""

    def __init__(self, dl_wrapper: DLWrapper, player_ll: PlayerLL):

        self._dl_wrapper = dl_wrapper
        self.player_ll = player_ll

    # ----------------------------------------------------------------------
    # CREATE TEAM
    # ----------------------------------------------------------------------
    
    def create_team(self, team_name: str, cap_id: int, players_id: list):
        """VALIDATES AND CREATES TEAM WITH CAPTAIN AND PLAYER IDS"""
    
        last_id = self.player_ll.get_new_player_id()
    
        if cap_id >= last_id:
            return "Captain id does not exist "
        
        check_team_name = self.check_if_team_name_exists(team_name)
    
        if check_team_name:
            return "Team name already exists"
        
        for player_id in players_id:
    
            if not self.player_ll.check_if_player_id_in_team(player_id):
                return "Player's id does not exist"
            
        create_team = self.create_team_to_data(team_name, cap_id, players_id)
    
        return create_team

    def create_team_to_data(self, name, captain_id, list_of_player_ids):
        """SAVES TEAM TO DATA LAYER AND UPDATES PLAYER TEAMS"""
    
        teams_file: list[Team] = self._dl_wrapper.view_all_teams()
    
        captain_handle = self.player_ll.take_id_return_handle(captain_id)
    
        if captain_handle is not True:
            return "Captain handle does not exist"
    
        list_of_player_handles = []
    
        for player_id in list_of_player_ids:
    
            self.player_ll.place_player_into_team(name, player_id)
            player_handle = self.player_ll.take_id_return_handle(player_id)
            list_of_player_handles.append(player_handle)
            
        id = self.get_last_team_id()
    
        team_model = Team(id, name, captain_handle, list_of_player_handles)

        list_player: list[Player] = self._dl_wrapper.load_all_player_info()
    
        for player in list_player:
    
            if player.handle == player_handle:
                player.team = name

        if self._dl_wrapper.append_team_into_file(team_model):
            return "Successfully created Team"
        
        return "Team was not created"

    # ----------------------------------------------------------------------
    # VIEW TEAMS
    # ----------------------------------------------------------------------
    
    def view_all_teams(self):
        """RETURNS ALL TEAMS FROM DATA LAYER"""
        return self._dl_wrapper.view_all_teams()

    def view_all_team_names_and_captains(self):
        """RETURNS LIST OF DICTIONARIES WITH TEAM NAMES AND CAPTAINS"""
    
        all_teams = self.view_all_teams()
    
        list_of_team_name_and_captain_name = []
    
        for team in all_teams:
            list_of_team_name_and_captain_name.append(
                {"team_name": team["team_name"], "captain": team["captain"]}
            )
    
        return list_of_team_name_and_captain_name

    # ----------------------------------------------------------------------
    # CHANGE TEAM CAPTAIN
    # ----------------------------------------------------------------------
    
    def change_team_captain(self, find_team, new_captain, team: Team):
        """CHANGES CAPTAIN OF A TEAM AND UPDATES DATA LAYER"""
    
        teams_list = self._dl_wrapper.view_all_teams()
    
        for row in teams_list:
            team_name = str(team.name)
    
            if team_name == find_team:
                team.captain = new_captain
    
                if self._dl_wrapper.write_team_into_file(teams_list):
                    return "Team Captain successfully changed"
    
        return "Team does not exists"

    # ----------------------------------------------------------------------
    # PLAYER MANAGEMENT
    # ----------------------------------------------------------------------
    
    def players_team_none(self):
        """RETURNS LIST OF PLAYERS NOT YET ASSIGNED TO A TEAM"""
    
        list_of_non_team_players_short_info = []
    
        all_players: list[Player] = self._dl_wrapper.load_all_player_info()
    
        for player in all_players:
    
            if player.team == "None":
                filtered_player = [player.id, player.name, player.handle]
                list_of_non_team_players_short_info.append(filtered_player)
    
        return list_of_non_team_players_short_info

    def view_all_players_in_team(self, team_name):
        """RETURNS ALL PLAYERS BELONGING TO A SPECIFIC TEAM"""
    
        list_players: list[Player] = self._dl_wrapper.load_all_player_info()
    
        players = []
    
        for player in list_players:
    
            if player.team == team_name:
                players.append(player)
    
        return players

    def view_captains_team(self, find_captain_handle, team: Team):
        """RETURNS THE TEAM ASSOCIATED WITH A CAPTAIN HANDLE"""
    
        all_teams = self.view_all_teams()
    
        for team in all_teams:
            if team.captain == find_captain_handle:
                return team

    # ----------------------------------------------------------------------
    # TEAM NAME VALIDATION
    # ----------------------------------------------------------------------
    
    def check_if_team_name_exists(self, team_name):
        """CHECKS IF A TEAM NAME IS ALREADY IN USE"""
    
        all_teams: list[Team] = self.view_all_teams()
    
        for team in all_teams:
            if team.name == team_name:
                return True
    
        return False

    def check_if_player_handle_in_team(self, find_team, handle):
        """CHECKS IF A PLAYER HANDLE BELONGS TO A TEAM"""
    
        players_in_team: list[Player] = self.view_all_players_in_team(handle)
    
        if not players_in_team:
            return "No players in this team"
    
        for player in players_in_team:
            if player.handle == handle:
                return True
    
        return False

    def view_captain_team_by_team_name(self, team_name, team: Team):
        """RETURNS CAPTAIN HANDLE GIVEN A TEAM NAME"""
    
        team_file = self.view_all_teams()
    
        for line in team_file:
            if team.name == team_name:
                return team.captain
    
        return "Team does not exist"

    # ----------------------------------------------------------------------
    # TEAM ID MANAGEMENT
    # ----------------------------------------------------------------------

    def get_last_team_id(self):
        """RETURNS THE NEXT AVAILABLE TEAM ID"""
    
        team_file: list[Team] = self._dl_wrapper.view_all_teams()
    
        if not team_file:
            return 1
    
        last_team: Team = team_file[-1]
        next_useable_id = int(last_team.id + 1)
    
        return next_useable_id
