from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from LL.teamLL import TeamLL
from models.team import Team
from models.player import Player
# viktor setti Team til að prófa

class CaptainLL:
    """HANDLES CAPTAIN OPERATIONS: EDIT PLAYERS, VIEW TEAMS, UPDATE CAPTAIN"""
    
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate, team: TeamLL):
        self._dl_wrapper = dl_wrapper
        self._validate = validate
        self._team = team

    # ----------------------------------------------------------------------
    # EDIT PLAYE PHONE FOR CAPTAIN
    # ----------------------------------------------------------------------

    def edit_player_phone_cap(self, team_name: str, handle: str, phone: str) -> str:
        """UPDATES A PLAYER'S PHONE NUMBER IN A TEAM"""

        existing_player = self._validate.check_if_handle_in_use(handle)
        
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._team.check_if_player_handle_in_team(team_name, handle)
        
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        validate_error = self._validate.validate_phone(phone)
        
        if validate_error:
            return validate_error
        
        list_player: list[Player] = self._dl_wrapper.load_all_player_info()
        
        for player in list_player:
            if player.handle == handle:
                player.phone = phone
        
        updated = self._dl_wrapper.edit_player_file(list_player)
        
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"

    # ----------------------------------------------------------------------
    # EDIT PLAYE R EMAIL FOR CAPTAIN
    # ----------------------------------------------------------------------

    def edit_player_email_cap(self, team: str, handle: str, email: str) -> str:
        """UPDATES A PLAYER'S EMAIL IN A TEAM"""
        
        existing_player = self._validate.check_if_handle_in_use(handle)
        
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._team.check_if_player_handle_in_team(team, handle)
        
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        

        validate_error = self._validate.validate_email(email)

        if validate_error:
            return validate_error
        
        list_player: list[Player] = self._dl_wrapper.load_all_player_info()

        for player in list_player:
            if player.handle == handle:
                player.email == email
        
        updated = self._dl_wrapper.edit_player_file(list_player)

        if updated:
            return "Success: Player information updated"

        return "Error: Failed to update player"


    # ----------------------------------------------------------------------
    # EDIT PLAYER ADDRESS FOR CAPTAIN
    # ----------------------------------------------------------------------

    def edit_player_address_cap(self, team: str, handle: str, address: str) -> str:
        """UPDATES A PLAYER'S ADDRESS IN A TEAM"""

        existing_player = self._validate.check_if_handle_in_use(handle)
 
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._team.check_if_player_handle_in_team(team, handle)
 
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        validate_error = self._validate.validate_address(address)
        
        if validate_error:
            return validate_error
        
        list_player: list[Player] = self._dl_wrapper.load_all_player_info()
        
        for player in list_player:
            if player.handle == handle:
                player.address == address
        
        updated = self._dl_wrapper.edit_player_file(list_player)
        
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"

    # ----------------------------------------------------------------------
    # EDIT PLAYER HANDLE CAPTAIN
    # ----------------------------------------------------------------------

    def edit_player_handle_cap(self, team: str, handle: str, handle_str: str) -> str:
        """CHANGES A PLAYER'S HANDLE AND ENSURES IT IS UNIQUE"""

        existing_player = self._validate.check_if_handle_in_use(handle)


        if not existing_player:
            return "Error: Player handle does not exists"
        

        existing_player_team = self._team.check_if_player_handle_in_team(team, handle)

        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        existing_new_handle = self._validate.check_if_handle_in_use(handle_str)

        if existing_new_handle:
            return "Error: New handle already exists"
        
        list_player: list[Player] = self._dl_wrapper.load_all_player_info()

        for player in list_player:
            if player.handle == handle:
                player.phone == handle_str
        
        updated = self._dl_wrapper.edit_player_file(list_player)

        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"
        
    # ----------------------------------------------------------------------
    # VIEW ALL PLAYERS IN THE TEAM
    # ----------------------------------------------------------------------
        
    def view_all_players_in_team(self, team_name):
        """RETURNS ALL PLAYERS IN A TEAM"""

        existing_team = self._team.check_if_team_name_exists(team_name)

        if not existing_team:
            return "Error: Team does not exists"
        
        return self._team.view_all_players_in_team(team_name)
    
    # ----------------------------------------------------------------------
    # VIEW CAPTAIN TEAMS
    # ----------------------------------------------------------------------

    def view_captain_teams(self, handle):
        """RETURNS ALL TEAMS FOR WHICH THE HANDLE IS THE CAPTAIN"""

        existing_handle = self._validate.check_if_handle_in_use(handle)

        if not existing_handle:
            return "Error: Captain does not exists"

        team_file: list[Team] = self._dl_wrapper.view_all_teams()

        for teams in team_file:
            if teams.captain == handle:
                return teams.name
            
    # ----------------------------------------------------------------------
    # UPDATE TEAM CAPTAIN
    # ----------------------------------------------------------------------
    
    def update_team_captain(self, team_name, handle):
        """UPDATES THE TEAM CAPTAIN AND MOVES OLD CAPTAIN TO PLAYER LIST"""

        existing_team = self._team.check_if_team_name_exists(team_name)

        if not existing_team:
            return "Error: Team does not exists"
        
        existing_handle_in_team = self._team.check_if_player_handle_in_team(team_name, handle)

        if not existing_handle_in_team:
            return "Error: Player's handle is not in team"
        
        team_list: list[Team] = self._dl_wrapper.view_all_teams()

        for team in team_list:

            if team.name == team_name:
                team.players.append(team.captain)
                team.captain = handle

                for player_handle in team.players:

                    if player_handle == handle:
                        team.players.remove(handle)
                            
        return self._dl_wrapper.edit_teams_file(team_list)
    






