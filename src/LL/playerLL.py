from datetime import datetime
from models.player import Player
from IO.data_wrapper import DLWrapper

class PlayerLL:
    """
    The Player Logical Layer (LL) handles business logic and validation 
    for Player objects before data is passed to or from the Data Layer (DL).
    """
    def __init__(self, dl_wrapper):
        # Stores the DLWrapper instance, which is the gateway to data persistence.
        self._dl_wrapper = dl_wrapper


    def create_player(self, player: Player):
        """
        Validates the Player object and, if successful, passes it to the DL 
        for creation/storage.
        """
        validate_errors = self.validate_player(player)

        if validate_errors:
            return validate_errors
        
        self._dl_wrapper.create_player(player)
        return "Success"


    def check_player_team(player: Player):
        """
        Checks if the provided team name already exists in the system.
        NOTE: This assumes DLWrapper.check_if_team_exists is implemented 
              to perform a check against stored data.
        """
        team_str = player.team

        if DLWrapper.check_if_team_exists(team_str):
            print("Team does not exists")

    
    def check_player_handle(player: Player):
        """
        Checks if the player's unique handle already exists in the system.
        NOTE: This assumes DLWrapper.check_if_handle_exists is implemented.
        """
        handle_str = player.handle

        if DLWrapper.check_if_handle_exists(handle_str):
            print("Handle does not exists")
        

    def check_player_address(player: Player):
        """
        Validates the player's address format.
        - Must not be empty.
        - Must contain at least one digit (for house/street number).
        - Must not contain consecutive spaces.
        """
        address_str = player.address.strip()

        if not address_str:
            return "Address cannot be empty"
        
        if not any(char.isdigit() for char in address_str):
            return "Address must contain a number"
        
        if "  " in address_str:
            return "Adress cannot contain consecutive spaces"
        
        return True


    def check_player_dob(player: Player): 
        """
        Validates the player's Date of Birth (DOB).
        - Must be in the exact YYYY-MM-DD format.
        - Must be a valid date (e.g., no Feb 30th).
        """
        dob_str  = player.dob.strip()

        try:
            birth_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
        
        except ValueError:
            return "DOB must be in the valid YYYY-MM-DD format"
        
        return True


    def check_player_name(player: Player):
        """
        Validates the player's full name.
        - Must not be empty.
        - Must contain only letters and spaces.
        - Must not already exist in the data layer.
        - Must be between 2 and 60 characters long.
        - Must not contain consecutive spaces.
        - Must be capitalized correctly (Title case).
        - Must have between 2 and 5 parts (first name, last name, etc.).
        """
        raw_name = player.name
        stripname = raw_name.strip()
        name_parts = stripname.split()
        
        if not raw_name:
            return "Not allow"

        if not raw_name.replace(" ","").isalpha():
            return "Not allow"

        if DLWrapper.check_if_player_exists(raw_name):
             return "Already in Data" 

        if len(raw_name) < 2 or len(raw_name) > 60:
            return "Not valid"

        if '  ' in stripname:
            return "Name cannot contain consecutive spaces."

        if raw_name != raw_name.title():
            return "Name must contain Capitalize letters"
        
        if len(name_parts) < 2 or len (name_parts) > 5:
            return "Not valid" 
        
        return True


    def check_player_phone(player: Player):
        """
        Validates the player's phone number format.
        - Must not be empty.
        - Must be exactly 8 characters long.
        - Must contain a hyphen ('-') specifically at the 4th position.
        - All non-hyphen characters must be digits.
        - Example 444-4444
        """
        phone_str = player.phone

        if not phone_str:
            return "Not valid"

        if len(phone_str) != 8:
            return "Not valid"

        if phone_str[3] != "-":
            return "Not valid"
        
        part1 = phone_str[:3]
        part2 = phone_str[4:]

        if not (part1.isdigit() and part2.isdigit()):
            return "Not valid"

        return True


    def check_player_email(player: Player):
        """
        Validates the player's email address using a series of specific checks.
        """
        email = player.email
        lenemail = len(email)

        att_symbol = email.find("@")
        email_split = email.split("@")
        two_dots = email.find("..")
        size = email.count("@")
        pat = email.find(".@")

        if "@" not in email:
            return ("@ symbol is missing.")

        if size > 1:
            second_at = email.find("@", att_symbol+1)
            return f"{email}\n{' '*second_at}^--there is an extra @ symbol here."
        
        if email[0] == "@" and att_symbol == 0:
            return "There is nothing before the @ symbol."
        
        if att_symbol == lenemail - 1:
            return f'{email}\n{" "*att_symbol + " "}^--there is nothing after the @ symbol.'
        
        if email[0] == ".":
            return "Email address starts with a dot."
        
        if ".." in email:
            return f"{email}\n{' '*two_dots}^--there are consecutive dots here."
        
        if ".@" in email:
            return f"{email}\n{' '*pat}^--there is an extra dot here."
        
        if "." not in email_split[1]:
            return "Top-level-domain is missing."
        
        return True


    def validate_player(self, player: Player) -> None:
        """
        Aggregates all individual validation checks.
        Returns a LIST of error strings if any check fails, or None if the player is valid.
        """
        errors_list = [] # A list to hold all error messages

        check_name = PlayerLL.check_player_name(player)
        check_email = PlayerLL.check_player_email(player)
        check_phone = PlayerLL.check_player_phone(player)
        check_dob = PlayerLL.check_player_dob(player)
        check_address = PlayerLL.check_player_address(player)
        check_handle = PlayerLL.check_player_handle(player)
        check_team = PlayerLL.check_player_team(player)

        if check_name is not True:
            errors_list.append(f"Name : {check_name}")

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

        # If the errors_list is not empty, return it
        if errors_list:
            return errors_list
        
        # Otherwise, all checks passed
        return None

         
    def edit_player(player: Player):
        id = player.id
        phone_str = player.phone
        address_str = player.address
        email_str = player.email
        handle = player.handle 

        

    
    
    
    
    