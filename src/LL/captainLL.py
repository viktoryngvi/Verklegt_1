from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from LL.teamLL import TeamLL
from models.team import Team
# viktor setti Team til að prófa

class CaptainLL:
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate, team: TeamLL):
        self._dl_wrapper = dl_wrapper
        self._validate = validate
        self._team = team

    def edit_player_phone_cap(self, team: str, handle: str, phone: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._dl_wrapper.check_if_player_handle_in_team(team, handle)
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        # Validate the updated data
        validate_error = self._validate.validate_phone(phone)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "phone", phone)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"


    def edit_player_email_cap(self, team: str, handle: str, email: str) -> str:
        """
        existing_player_team = self._dl_wrapper.check_if_player_handle_in_team(team, handle)
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._dl_wrapper.check_if_player_handle_in_team(team, handle)
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        # Validate the updated data
        validate_error = self._validate.validate_email(email)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "email", email)
        if updated:
            return "Success: Player information updated"

        return "Error: Failed to update player"


    def edit_player_address_cap(self, team: str, handle: str, address: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_player_team = self._dl_wrapper.check_if_player_handle_in_team(team, handle)
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        # Validate the updated data
        validate_error = self._validate.validate_address(address)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "address", address)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"


    def edit_player_handle_cap(self, team: str, handle: str, handle_str: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        # Check if player exists
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        

        existing_player_team = self._dl_wrapper.check_if_player_handle_in_team(team, handle)
        if not existing_player_team:
            return "Error: Player handle does not exists in this team"
        
        existing_new_handle = self._dl_wrapper.check_if_handle_exists_with_handle(handle_str)
        if existing_new_handle:
            return "Error: New handle already exists"
        
        updated = self._dl_wrapper.edit_player_info(handle, "handle", handle_str)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"
        
    def view_all_players_in_team(self, team_name):
        existing_team = self._team.check_if_team_name_exists(team_name)
        if not existing_team:
            return "Error: Team does not exists"
        
        return self._team.view_all_players_in_team(team_name)
    
    def view_captain_teams(self, handle):
        existing_handle = self._validate.check_if_handle_in_use(handle)
        if not existing_handle:
            return "Error: Captain does not exists"
        team_file: list[Team] = self._dl_wrapper.view_all_teams()
        for teams in team_file:
            if teams.captain == handle:
                return teams.name
    
    def update_team_captain(self, team_name, handle):
        existing_team = self._dl_wrapper.check_if_team_name_exists(team_name)
        if not existing_team:
            return "Error: Team does not exists"
        
        existing_handle_in_team = self._dl_wrapper.check_if_player_handle_in_team(handle)
        if not existing_handle_in_team:
            return "Error: Player's handle is not in team"
        
        return self._dl_wrapper.change_team_captain(team_name, handle)
    






