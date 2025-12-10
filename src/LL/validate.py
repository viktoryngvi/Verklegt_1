from models.player import Player
from models.club import Club
from models.event import Event
from IO.data_wrapper import DLWrapper
from datetime import datetime
from models.club import Club
from models.event import Event

class Validate:  
    def __init__(self, dl_wrapper: DLWrapper):
          self._dl_wrapper = dl_wrapper

        # ----------------------------------------------------------------------
    # VALIDATE PLAYER
    # ----------------------------------------------------------------------

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
        check_address = self.check_player_address(player) 
        check_handle = self.check_player_handle(player) 
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

        # If the errors_list is not empty, return it
        if errors_list:
            return errors_list
        
        # Otherwise, all checks passed
        return None
    
    # ----------------------------------------------------------------------
    # CHECK PLAYER TEAM
    # ----------------------------------------------------------------------
   
    def check_player_team(self, player: Player):

        self.team_str = player.team

        if self.team_str is None:
            return True

        if not self._dl_wrapper.check_if_team_name_exists(self.team_str):
            return "Team does not exists"
        
        return True

    # ----------------------------------------------------------------------
    # CHECK PLAYER HANDLE
    # ----------------------------------------------------------------------

    def check_player_handle(self, player: Player):
        """
        Checks if the player's unique handle already exists in the system.
        NOTE: This assumes DLWrapper.check_if_handle_exists is implemented.
        """
        if self._dl_wrapper.check_if_handle_exists_with_player(player):
            return "Handle does exists"
        
        return True

        # ----------------------------------------------------------------------
    # CHECK PLAYER ADDRESS
    # ----------------------------------------------------------------------


    def check_player_address(self, player: Player):
        """
        Validates the player's address format.
        - Must not be empty.
        - Must contain at least one digit (for house/street number).
        - Must not contain consecutive spaces.
        """
        self.address_str = player.address.strip()

        if self.validate_address(self.address_str):
            return self.validate_address
        
        return True

    # ----------------------------------------------------------------------
    # CHECK PLAYER PHONE
    # ----------------------------------------------------------------------

    def check_player_phone(self, player: Player):
        """
        Validates the player's phone number format (8 digits with a dash).
        """
        self.phone = player.phone

        if self.validate_phone(self.phone):
            return self.validate_phone(self.phone)

        return True

    # ----------------------------------------------------------------------
    # CHECK PLAYER EMAIL
    # ----------------------------------------------------------------------

    def check_player_email(self, player: Player):
        """
        Validates the player's email format against common structural rules (e.g., @ symbol, dots).
        """
        self.email = player.email

        if self.validate_email(self.email):
            return self.validate_address(self.email)
        
        return True

    # ----------------------------------------------------------------------
    # CHECK PLAYER DOB
    # ----------------------------------------------------------------------

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
    
        # ----------------------------------------------------------------------
    # CHECK PLAYER NAME
    # ----------------------------------------------------------------------

    def check_player_name(self, player: Player):
        """
        Validates the player's full name against length, formatting, and content rules.
        """
        self.name = player.name.strip()
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
    

        # ----------------------------------------------------------------------
    # VALIDATE PHONE 
    # ----------------------------------------------------------------------

    def validate_phone(self, phone: str) -> None:
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
    
        # ----------------------------------------------------------------------
    # VALIDATE EMAIL
    # ----------------------------------------------------------------------

    def validate_email(self, email: str) -> None:
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
    
        # ----------------------------------------------------------------------
    # VALIDATE ADDRESS
    # ----------------------------------------------------------------------

    def validate_address(self, address: str) -> None:
        """
        Validates the new address format.
        """
        if not address:
            return "Address cannot be empty"
        
        if not any(char.isdigit() for char in address):
            return "Address must contain a number"
        
        if "  " in address:
            return "Adress cannot contain consecutive spaces"
        
        return None
    
        # ----------------------------------------------------------------------
    # VALIDATE CLUB 
    # ----------------------------------------------------------------------
    
    def validate_club(self, club: Club):
        errors_list = []

        club_country = self.validate_club_country(club.country)
        club_home_town = self.validate_club_home_town(club_home_town)
        club_color = self.validate_club_color(club_color)
        club_teams = self.validate_club_teams(club.teams)

        if club_country is not True:
            errors_list.append(f"Error: {club_country}") 
        
        if club_home_town is not True:
            errors_list.append(f"Error: {club_home_town}")

        if club_color is not True:
            errors_list.append(f"Error: {club_color}")

        if club_teams is not True:
            errors_list.append(f"Error: {club_teams}")
    # ----------------------------------------------------------------------
    # VALIDATE CLUB COUNTRY
    # ----------------------------------------------------------------------
    def validate_club_country(self, club_country: str):
        pass
        # ----------------------------------------------------------------------
    # VALIDATE CLUB HOME TOWN
    # ----------------------------------------------------------------------
    def validate_club_home_town(self, club_home_town: str):
        pass
        # ----------------------------------------------------------------------
    # VALIDATE CLUB COLOR
    # ----------------------------------------------------------------------
    def validate_club_color(self, club_color: str):
        pass
        # ----------------------------------------------------------------------
    # VALIDATE CLUB TEAMS
    # ----------------------------------------------------------------------
    def validate_club_teams(self, club_teams: list):
        pass
    

        # ----------------------------------------------------------------------
    # VALIDATE EVENT
    # ----------------------------------------------------------------------

    def validate_event(self, event : Event ):
        errors_list = []

        check_tournament_name = self.check_tournament_name(event)
        check_event_name = self.check_event_name(event)
        check_start_date = self.check_start_date(event)
        check_end_date = self.check_end_date(event)
        check_registered_teams = self.check_registered_teams(event)
        check_matches = True


        if check_tournament_name is not True:
            errors_list.append(f"Tournament Name: {check_tournament_name}")

        if check_event_name is not True:
            errors_list.append(f"Event Name: {check_event_name}")

        if check_start_date is not True:
            errors_list.append(f"Start Date: {check_start_date}")

        if check_end_date is not True:
            errors_list.append(f"End Date: {check_end_date}")

        if check_registered_teams is not True:
            errors_list.append(f"Registered Teams: {check_registered_teams}")

        if check_matches is not True:
            errors_list.append(f"Matches: {check_matches}")

        return errors_list if errors_list else None


    def check_tournament_name(self, event : Event):
        event_name = event.tournament_name.strip()

        if "  " in event_name:
            return "Name cannot contain consecutive spaces."
        
        if len(event.tournament_name) < 2 or len(event.tournament_name) > 60:
            return "Name must be between 2 and 60 characters."

        return True            


    def check_event_name(self, event : Event):
        event_name = event.event_name.strip()

        if "  " in event_name:
            return "Name cannot contain consecutive spaces."
        
        if len(event_name) < 2 or len(event_name) > 60:
            return "Name must be between 2 and 60 characters."

        return True    
    
    def check_start_date(self, event : Event):
        try:
            self.start = datetime.strptime(event.start_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use yyyy-mm-dd"
        
        return True

    def check_end_date(self, event : Event):
        try:
            self.end = datetime.strptime(event.end_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use yyyy-mm-dd"
        
        return True
        
    def check_registered_teams(self, event : Event):
        return True
    def check_matches(self, event : Event):
        return True
