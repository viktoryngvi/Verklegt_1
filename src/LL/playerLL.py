from datetime import datetime
from models.player import Player
from IO.data_wrapper import DLWrapper
from models.person import Person

class PlayerLL:
    """
    The Player Logical Layer (LL) class.
    
    This layer is responsible for handling business logic related to Player objects,
    including validation of data fields (e.g., name, email, DOB) and coordinating 
    data persistence by interacting with the Data Layer (DLWrapper).
    """
    def __init__(self, dl_wrapper: DLWrapper):
        """
        Initializes the PlayerLL instance with a Data Layer wrapper.
        
        This dependency injection allows the PlayerLL to access storage functions 
        without knowing the underlying storage implementation (e.g., CSV, database).

        :param dl_wrapper: An instance of DLWrapper used for all data access operations.
        :type dl_wrapper: DLWrapper
        """
        self._dl_wrapper = dl_wrapper

        
    def create_player(self, player: Player):
        """
        Validates the player data and, if valid, passes it to the Data Layer for storage.
        """
        validate_errors = self.validate_player(player)

        if validate_errors:
            # If a list of errors is returned, stop and return the errors.
            return validate_errors
        
        # If valid, pass the player object to the Data Layer for creation.
        return self._dl_wrapper.create_player(player)


    def check_player_team(self, player: Player):
        """
        Checks if the provided team name already exists in the system.
        NOTE: This assumes DLWrapper.check_if_team_exists is implemented 
              to perform a check against stored data.
        """
        self.team_str = player.team

        if not self._dl_wrapper.check_if_team_exists(self.team_str):
            return "Team does not exists"
        
        return True

    def check_player_handle(self, player: Player):
        """
        Checks if the player's unique handle already exists in the system.
        NOTE: This assumes DLWrapper.check_if_handle_exists is implemented.
        """
        self.handle_str = player.handle

        if self._dl_wrapper.check_if_handle_exists(self.handle_str):
            return "Handle does exists"
        
        return True

    def check_player_address(self, player: Player):
        """
        Validates the player's address format.
        - Must not be empty.
        - Must contain at least one digit (for house/street number).
        - Must not contain consecutive spaces.
        """
        self.address_str = player.address.strip()

        if not self.address_str:
            return "Address cannot be empty"
        
        if not any(char.isdigit() for char in self.address_str):
            return "Address must contain a number"
        
        if "  " in self.address_str:
            return "Adress cannot contain consecutive spaces"
        
        return True



    def check_player_dob(self, player: Player):
        """
        Validates the player's Date of Birth (DOB) format and age constraints.
        """
        self.dob_str = player.dob

        try:
            self.dob: datetime = datetime.strptime(self.dob_str, "%Y-%m-%d")
        except ValueError:
            return "DOB must be in YYYY-MM-DD format."

        self.today = datetime.today()

        if self.dob >= self.today:
            return "DOB cannot be in the future."

        self.age = (self.today - self.dob).days // 365

        if self.age < 5:
            return "Player must be at least 5 years old."

        if self.age > 100:
            return "Player age cannot exceed 100."

        return True

    def check_player_name(self, Player: Player):
        """
        Validates the player's full name against length, formatting, and content rules.
        """
        self.name = Player.name.strip()
        parts = self.name.split()

        if len(self.name) < 2 or len(self.name) > 60:
            return "Name must be between 2 and 60 characters."

        if "  " in self.name:
            return "Name cannot contain consecutive spaces."

        if self.name != self.name.title():
        # Auto-capitalize each word in the full name and update the player object.
            corrected = ' '.join(part.capitalize() for part in parts)
            if self.name != corrected:
                self.name = corrected
        
        if self.name != self.name.isalpha() and " " not in self.name:
            return "Name can only contain alphabetic characters and spaces."
        
        if len(parts) < 2:
            return "Full name must have at least 2 words."

        if len(parts) > 5:
            return "Full name cannot have more than 5 words."

        return True

    def check_player_phone(self, person: Person):
        """
        Validates the player's phone number format (8 digits with a dash).
        """
        self.phone = person.phone

        if len(self.phone) != 8:
            return "Phone number must be in format 123-4567."

        if "-" not in self.phone:
            return "Invalid format. Example: 123-4567"
        
        left, right = self.phone.split("-")
    
        if not (left.isdigit() and right.isdigit()):
            return "Phone can only contain digits and one dash."
        if len(left) != 3 or len(right) != 4:
            return "Phone number must be in format 123-4567."
        
        return True


    def check_player_email(self, player: Player):
        """
        Validates the player's email format against common structural rules (e.g., @ symbol, dots).
        """
        self.email = player.email
        self.len_email = len(self.email)

        att_symbol = self.email.find("@")
        email_split = self.email.split("@")
        two_dots = self.email.find("..")
        size = self.email.count("@")
        pat = self.email.find(".@")

        if "@" not in self.email:
            return "@ symbol is missing."

        if size > 1:
            second_at = self.email.find("@", att_symbol+1)
            return f"{self.email}\n{' '*second_at}^--there is an extra @ symbol here."
        
        if self.email[0] == "@" and att_symbol == 0:
            return "There is nothing before the @ symbol."
        
        if att_symbol == self.len_email - 1:
            return f'{self.email}\n{" "*att_symbol}^--there is nothing after the @ symbol.'
        
        if self.email[0] == ".":
            return "Email address starts with a dot."
        
        if ".." in self.email:
            return f"{self.email}\n{' '*two_dots}^--there are consecutive dots here."
        
        if ".@" in self.email:
            return f"{self.email}\n{' '*pat}^--there is an extra dot here."
        
        if "." not in email_split[1]:
            return "Top-level domain is missing."
        
        return True


    def validate_player(self, player: Player) -> None:
        """
        Aggregates all individual validation checks.
        Returns a LIST of error strings if any check fails, or None if the player is valid.
        """
        errors_list = [] # A list to hold all error messages

        check_name = self.check_player_name(player)
        check_email = self.check_player_email(player)
        check_phone = self.check_player_phone(player)
        check_dob = self.check_player_dob(player)
        check_address = self.check_player_address(player) # This one must be updated to include 'self' in its definition (see below)
        check_handle = self.check_player_handle(player) # This one must be updated to include 'self' in its definition (see below)
        check_team = self.check_player_team(player)

        if check_name is not True:
            errors_list.append(f"Name: {check_name}")

        if check_email is not True:
            errors_list.append(f"Email : {check_email}")
        
        if check_phone is not True:
            errors_list.append(f"Phone : {check_phone}")
                
        if check_dob is not True:
             errors_list.append(f"DOB : {check_dob}")

        if check_address is not True:
            errors_list.append(f"Address: {check_address} ")

        if check_handle is not True:
            errors_list.append(f"Handle : {check_handle}")

        if check_team is not True:
            errors_list.append(f"Team : {check_team}")

        # If the errors_list is not emQpty, return it
        if errors_list:
            return errors_list
        
        # Otherwise, all checks passed
        return None

         
    def edit_player(self, player_name: str, email: str, phone: str, player_data: Player) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """

        # Check if player exists
        existing_player = self._dl_wrapper.check_if_player_exists(player_name)
        if not existing_player:
            return "Error: Player not found"

        # Build updated Player object
        updated_player = Player(
            name=player_name,
            email=email,
            phone=phone,
            dob=existing_player.dob
        )

        # Validate the updated data
        validate_errors = self.validate_player(updated_player)
        if validate_errors:
            return validate_errors
        
        updated = self._dl_wrapper.edit_player_info(player_name, email, phone)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"

















        

        

    
    
    
    
    