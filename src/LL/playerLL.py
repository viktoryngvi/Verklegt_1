from models.player import Player
from IO.data_wrapper import DLWrapper
from LL.validate import Validate


class PlayerLL:
    """
    The Player Logical Layer (LL) class.
    
    This layer is responsible for handling business logic related to Player objects,
    including validation of data fields (e.g., name, email, DOB) and coordinating 
    data persistence by interacting with the Data Layer (DLWrapper).
    """
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        """
        Initializes the PlayerLL instance with a Data Layer wrapper.
        
        This dependency injection allows the PlayerLL to access storage functions 
        without knowing the underlying storage implementation (e.g., CSV, database).

        :param dl_wrapper: An instance of DLWrapper used for all data access operations.
        :type dl_wrapper: DLWrapper
        """
        self._dl_wrapper = dl_wrapper
        self._validate = validate

        
    def create_player(self, player: Player):
        """
        Validates the player data and, if valid, passes it to the Data Layer for storage.
        """
        validate_errors = self._validate.validate_player(player)

        if validate_errors:
            # If a list of errors is returned, stop and return the errors.
            return validate_errors
        
        # If valid, pass the player object to the Data Layer for creation.
        return self._dl_wrapper.create_player(player)


    def edit_player_phone(self, id: int, phone: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        last_id = self._dl_wrapper.check_last_id
        if id > last_id:
            return "Id does not Exist"
        # Validate the updated data
        validate_error = self._validate.validate_phone(phone)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(id, "phone", phone)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"


    def edit_player_email(self, id: int, email: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        last_id = self._dl_wrapper.check_last_id
        if id > last_id:
            return "Id does not Exist"
        # Validate the updated data
        validate_error = self._validate.validate_email(email)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(id, "email", email)
        if updated:
            return "Success: Player information updated"

        return "Error: Failed to update player"


    def edit_player_address(self, id: int, address: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        last_id = self._dl_wrapper.check_last_id
        if id > last_id:
            return "Id does not Exist"
        # Validate the updated data
        validate_error = self._validate.validate_address(address)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(id, "address", address)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"


    def edit_player_handle(self, id: int, handle: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        last_id = self._dl_wrapper.check_last_id
        if id > last_id:
            return "Id does not Exist"
        
        # Check if player exists
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if existing_player:
            return "Error: Player not found"

        updated = self._dl_wrapper.edit_player_info(id, "handle", handle)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"




















        

        

    
    
    
    
    