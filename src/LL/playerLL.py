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


    def validate_phone(phone: str) -> None:
        """
        Validates the new updated phone number format (8 digits with a dash).
        """
        if len(phone) != 8:
            return "Phone number must be in format 123-4567."

        if "-" not in phone:
            return "Invalid format. Example: 123-4567"
        
        left, right = phone.split("-")
    
        if not (left.isdigit() and right.isdigit()):
            return "Phone can only contain digits and one dash."
        
        if len(left) != 3 or len(right) != 4:
            return "Phone number must be in format 123-4567."
        
        return None

    def validate_email(email: str) -> None:
        """
        Validates the new updated email format against common structural rules (e.g., @ symbol, dots).
        """
        len_email = len(email)

        att_symbol = email.find("@")
        email_split = email.split("@")
        two_dots = email.find("..")
        size = email.count("@")
        pat = email.find(".@")

        if "@" not in email:
            return "@ symbol is missing."

        if size > 1:
            second_at = email.find("@", att_symbol+1)
            return f"{email}\n{' '*second_at}^--there is an extra @ symbol here."
        
        if email[0] == "@" and att_symbol == 0:
            return "There is nothing before the @ symbol."
        
        if att_symbol == len_email - 1:
            return f'{email}\n{" "*att_symbol}^--there is nothing after the @ symbol.'
        
        if email[0] == ".":
            return "Email address starts with a dot."
        
        if ".." in email:
            return f"{email}\n{' '*two_dots}^--there are consecutive dots here."
        
        if ".@" in email:
            return f"{email}\n{' '*pat}^--there is an extra dot here."
        
        if "." not in email_split[1]:
            return "Top-level domain is missing."
        
        return None

    def validate_address(address: str) -> None:
        """
        Validates the new address format.
        - Must not be empty.
        - Must contain at least one digit (for house/street number).
        - Must not contain consecutive spaces.
        """
        if not address:
            return "Address cannot be empty"
        
        if not any(char.isdigit() for char in address):
            return "Address must contain a number"
        
        if "  " in address:
            return "Adress cannot contain consecutive spaces"
        
        return None


    def edit_player_phone(self, id: int, phone: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        # Validate the updated data
        validate_error = self.validate_phone(phone)
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
        # Validate the updated data
        validate_error = self.validate_email(email)
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
        # Validate the updated data
        validate_error = self.validate_address(address)
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
        # Check if player exists
        existing_player = self._dl_wrapper.check_if_handle_exists_with_handle(handle)
        if existing_player:
            return "Error: Player not found"

        updated = self._dl_wrapper.edit_player_info(id, "handle", handle)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"




















        

        

    
    
    
    
    