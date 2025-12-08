from IO.data_wrapper import DLWrapper
from LL.validate import Validate

class CaptainLL:
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self._dl_wrapper = dl_wrapper
        self._validate = validate

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


