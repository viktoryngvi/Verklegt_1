from datetime import datetime,date
from models.player import Player
from models.club import Club
from models.event import Event
from models.team import Team
from IO.data_wrapper import DLWrapper
from models.tournament import Tournament


class Validate:  
    def __init__(self, dl_wrapper: DLWrapper):
          self._dl_wrapper = dl_wrapper
          
        # ----------------------------------------------------------------------
    # CHECKS AND VALIDATION METHODS FOR PLAYER
    # ----------------------------------------------------------------------

    def validate_player(self, player: Player):
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
    # VALIDATE PLAYER TEAM
    # ----------------------------------------------------------------------
   
    def check_player_team(self, player: Player):

        self.team_str = player.team

        if self.team_str is None:
            return True

        if not self._dl_wrapper.check_if_team_name_exists(self.team_str):
            return "Team does not exists"
        
        return True
    
        # ----------------------------------------------------------------------
    # VALIDATE PLAYER HANDLE
    # ----------------------------------------------------------------------


    def check_player_handle(self, player: Player):
        """
        Checks if the player's unique handle already exists in the system.
        NOTE: This assumes DLWrapper.check_if_handle_exists is implemented.
        """
        if self.check_if_handle_exists_with_player(player):
            return "Handle does exists"
        
        return True
    
        # ----------------------------------------------------------------------
    # VALIDATE PLAYER ADDRESS
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
    # VALIDATE PLAYER PHONE
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
    # VALIDATE PLAYER EMAIL
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
    # VALIDATE DOB
    # ----------------------------------------------------------------------

    def check_player_dob(self, player: Player):
        """
        Validates the player's Date of Birth (DOB) format and age constraints.
        """


        if not isinstance(player.dob,date):
            return "DOB must be in YYYY-MM-DD format."

        self.today = date.today()

        if player.dob >= self.today:
            return "DOB cannot be in the future."

        self.age = (self.today - player.dob).days // 365

        if self.age < 5:
            return "Player must be at least 5 years old."

        if self.age > 100:
            return "Player age cannot exceed 100."

        return True
    
        # ----------------------------------------------------------------------
    # VALIDATE PLAYER NAME
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

        name_no_spaces = self.name.replace(" ", "")
        
        if not name_no_spaces.isalpha():
            return "Name can only contain alphabetic characters."
        
        if " " not in self.name:
            return "Please input your full name."
        
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
        if not len(phone) != 8:
            return "Phone number must be in format 123-4567."

        if "-" not in phone:
            left = phone[:3]
            right= phone[3:]
            phone = left + "-" + right

        
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
    # VALIDATE HANDLE IN USE
    # ----------------------------------------------------------------------


    def check_if_handle_in_use(self, handle):
        """checks ef the inputted handle is in use in the player list"""
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_list:
            if handle == player.handle:
                return True
        return False
    
        # ----------------------------------------------------------------------
    # VALIDATE HANDLE EXISTS WITH PLAYER
    # ----------------------------------------------------------------------

    
    def check_if_handle_exists_with_player(self, player: Player):
        """checks ef the inputted handle is in use in the player list"""
        player_handle = self.check_if_handle_in_use(player.handle)
        return player_handle

    # def check_if_player_id_in_team(self, id):
    #     """takes id and check if that player is in a team"""
    #     player_list = self._dl_wrapper.load_all_player_info()
    #     for players in player_list:
    #         if id == int(players["id"]):
    #             if players["team"] is None:
    #                 return False
    #     return True
    
    # CHECKS AND VALIDATION METHODS FOR CLUB
    
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


    def validate_club_country(self, club_country: str):
        pass


    def validate_club_home_town(self, club_home_town: str):
        pass


    def validate_club_color(self, club_color: str):
        pass


    def validate_club_teams(self, club_teams: list):
        pass


    # CHECKS AND VALIpper)DATION METHODS FOR EVENT
    # ----------------------------------------------------------------------
    # CHECKS AND VALIDATION METHODS FOR EVENT
    # ----------------------------------------------------------------------



    def validate_event(self, event: Event):
        errors_list = []

        event_name = self.check_event_name(event.event_name)
        event_start = self.check_start_date_event(event.start_date, event.tournament_name)
        event_end = self.check_end_date_event(event.end_date, event.tournament_name)
        event_id = self.get_next_event_id()

        if event_name is not True:
            errors_list.append(f"Name: {event_name}")

        if event_start is not True:
            errors_list.append(f"Start date: {event_start}")

        if event_end is not True:
            errors_list.append(f"End date: {event_end}")

        if errors_list:
            return errors_list

        return None
    

    # ----------------------------------------------------------------------
    # get next match id
    # ----------------------------------------------------------------------

    def get_next_event_id(self):
        """checks the last match and returns the next usable id"""
        event_data: list[Event] = self._dl_wrapper.load_event_blueprint()
        if not event_data:
            return 1
        last_match: Event = event_data[-1]
        next_useable_id = int(last_match.event_id + 1)
        return next_useable_id
    
    # ----------------------------------------------------------------------
    # VALIDATE EVENT NAME
    # ----------------------------------------------------------------------


    def check_event_name(self, event_name: str):
        if not event_name or not event_name.strip():
            return "Event name cannot be empty."

        if not event_name[0].isupper():
            return "Event name must start with an uppercase letter."        

        if not event_name.isalpha():
            return "Event name must contain only letters"
        
        if len(event_name) > 20:
            return "Event name is too long (max 20 characters)."
        
        return True 
    
        # ----------------------------------------------------------------------
    # VALIDATE START DATE
    # ----------------------------------------------------------------------

    def check_start_date_event(self, start_date: str, tournament_name: str):
        try:
            start_date_event: datetime = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            return "Event must be in YYYY-MM-DD format."
                
        start_tournament = self.view_start_date_of_tournament(tournament_name)

        if isinstance(start_tournament, str):
            return start_tournament

        if start_date_event.date() < start_tournament:
            return f"Event cannot start before the tournament start date ({start_tournament})."

        return True

        # ----------------------------------------------------------------------
    # VALIDATE END DATE
    # ----------------------------------------------------------------------

    def check_end_date_event(self, end_date: str, tournament_name):
        try:
            end_date_event: datetime = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return "Event must be in YYYY-MM-DD format."

        end_tournament = self.view_end_date_of_tournament(tournament_name)

        if isinstance(end_tournament, str):
            return end_tournament

        if end_date_event.date() > end_tournament:
            return f"Event cannot end after the tournament end date ({end_tournament})."

        return True
    
    def view_start_date_of_tournament(self, tournament_name):
        tournament_list: list[Tournament] = self._dl_wrapper.read_tournament_file()
        for tournament in tournament_list:
            if tournament.tournament_name == tournament_name:
                return tournament.start_date
            
        return "Tournament not found"
    
    def view_end_date_of_tournament(self, tournament_name):
        tournament_list: list[Tournament] = self._dl_wrapper.read_tournament_file()
        for tournament in tournament_list:
            if tournament.tournament_name == tournament_name:
                return tournament.end_date
            
        return "Tournament not found"


    def check_event_name(self, event_name: str):
        if not event_name or not event_name.strip():
            return "Event name cannot be empty."

        if not event_name[0].isupper():
            event_name = event_name.capitalize()
                  

        if not event_name.isalpha():
            return "Event name must contain only letters"
        # ----------------------------------------------------------------------
    # VALIDATE REGISTERED TEAMS
    # ----------------------------------------------------------------------
        
        if len(event_name) > 20:
            return "Event name is too long (max 20 characters)."
        
        return True 

 
    def check_registered_teams(self, event : Event):
        return True
            # ----------------------------------------------------------------------
    # VALIDATE MATCHES
    # ----------------------------------------------------------------------
    def check_matches(self, event : Event):
        return True



    # ----------------------------------------------------------------------
    # VALIDATE TOURNAMENT 
    # ----------------------------------------------------------------------
    def validate_tournament(self, tournament: Tournament):
            errors = []

            check_name = self.check_tournament_name(tournament)
            #check_type = self.check_tournament_type(tournament.type)
            check_dates = self.check_dates(tournament)
            check_contact_name = self.check_contact_name(tournament)
            check_contact_email = self.check_contact_email(tournament)
            check_contact_phone = self.check_contact_phone(tournament)

            if check_name is not True:
                errors.append(f"Name: {check_name}")

            # if check_type is not True:
            #     errors.append(f"Type: {check_type}")

            if check_dates is not True:
                errors.append(f"Dates: {check_dates}")

            if check_contact_name is not True:
                errors.append(f"Dates: {check_contact_name}")

            if check_contact_email is not True:
                errors.append(f"Dates: {check_contact_email}")

            if check_contact_phone is not True:
                errors.append(f"Dates: {check_contact_phone}")

            return errors if errors else None
    # ----------------------------------------------------------------------    
     # tournament name validation
    # ----------------------------------------------------------------------
    
    def check_tournament_name(self, tournament: Tournament):
        tournament_name = tournament.tournament_name.strip()

        if len(tournament_name) == 0:
            return "Tournament name cannot be empty."

        if len(tournament_name) < 3 or len(tournament_name) > 60:
            return "Tournament name must be between 3–60 characters."

        return True


# ----------------------------------------------------------------------
 # tournament type validation
# ----------------------------------------------------------------------


    # def check_tournament_type(self, tournament_type: str):
    #     tournament_type_stripped = tournament_type.strip()

    #     allowed_names = ["Knockout", "Double Elimination"]

    #     if self.tournament_type not in allowed_names:
    #         return "Tournament type must be 'Knockout' or 'Double Elimination'."

    #     return True


    # ----------------------------------------------------------------------
     # date validation
    # ----------------------------------------------------------------------

    def check_dates(self, tournament: Tournament):
        try:
            self.start = datetime.strptime(tournament.start_date, "%Y-%m-%d")
            self.end = datetime.strptime(tournament.end_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use yyyy-mm-dd"

        if self.start >= self.end:
            return "Start date must be before end date."

        if (self.end - self.start).days < 4:
            return "Tournament must span more then 4 days."

        return True


    
# --------------------------------------------------------------------------
# VALIDATE CONTACT NAME
# --------------------------------------------------------------------------   

    def check_contact_name(self, tournament: Tournament):
        check_contact_name = tournament.contact_name.strip()

        if len(check_contact_name) == 0:
            return "Contact name cannot be empty."

        if len(check_contact_name) < 3:
            return "Contact name must be at least 3 characters."

        return True

# --------------------------------------------------------------------------
# VALIDATE CONTACT EMAIL
# --------------------------------------------------------------------------  
    def check_contact_email(self, tournament: Tournament):
        check_contact_email = tournament.contact_email.strip()

        result = self.validate_email(check_contact_email)

        if result is not None:
            return f"Invalid email: {result}"

        return True
    

# --------------------------------------------------------------------------
# VALIDATE CONTACT PHONE
# --------------------------------------------------------------------------  
    def check_contact_phone(self, tournament: Tournament):
        check_contact_phone = tournament.contact_phone.strip()

        result = self.validate_phone(check_contact_phone)

        if result is not None:
            return f"Invalid phone: {result}"

        return True
    