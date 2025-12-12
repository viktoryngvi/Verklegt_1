from datetime import datetime, date
from models.player import Player
from models.club import Club
from models.event import Event
from models.team import Team
from IO.data_wrapper import DLWrapper
from models.tournament import Tournament
from models.match import Match

class Validate:
    """ LOGICAL LAYER FOR DATA VALIDATION """

    def __init__(self, dl_wrapper: DLWrapper):
        """INITIALIZES Validate WITH DLWrapper INSTANCE"""
        self._dl_wrapper = dl_wrapper

    # ----------------------------------------------------------------------
    # PLAYER VALIDATION
    # ----------------------------------------------------------------------
    def validate_player(self, player: Player):
        """Returns a list of error strings if invalid, or None if valid."""
       
        errors_list = []


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
            errors_list.append(f"Address: {check_address}")
        
        if check_handle is not True:
            errors_list.append(f"Handle : {check_handle}")
        
        if check_team is not True:
            errors_list.append(f"Team : {check_team}")

        return errors_list if errors_list else None

    def check_player_team(self, player: Player):
        """VALIDATES THAT PLAYER'S TEAM EXISTS OR IS NONE"""
        
        self.team_str = player.team
        if self.team_str is None:
            return True
        
        if not self._dl_wrapper.check_if_team_name_exists(self.team_str):
            return "Team does not exists"
        
        return True

    def check_player_handle(self, player: Player):
        """VALIDATES THAT PLAYER HANDLE IS UNIQUE"""
        
        if self.check_if_handle_exists_with_player(player):
            return "Handle does exists"
        
        return True

    def check_player_address(self, player: Player):
        """VALIDATES PLAYER ADDRESS FORMAT"""
        
        self.address_str = player.address.strip()
        
        if self.validate_address(self.address_str):
            return self.validate_address
        
        return True

    def check_player_phone(self, player: Player):
        """VALIDATES PLAYER PHONE FORMAT"""
        
        self.phone = player.phone
        
        if self.validate_phone(self.phone):
            return self.validate_phone(self.phone)
        
        return True

    def check_player_email(self, player: Player):
        """VALIDATES PLAYER EMAIL FORMAT"""
        
        self.email = player.email
        
        if self.validate_email(self.email):
            return self.validate_address(self.email)
        
        return True

    def check_player_dob(self, player: Player):
        """VALIDATES PLAYER DATE OF BIRTH AND AGE CONSTRAINTS"""
        
        dob = player.dob
        
        if isinstance(dob, str):
            dob = dob.strip()
        
            try:
                dob = datetime.strptime(dob, "%Y-%m-%d").date()
            except ValueError:
                return "DOB must be in YYYY-MM-DD format."
        
        elif not isinstance(dob, date):
            return "DOB must be in YYYY-MM-DD format."

        today = date.today()
        
        if dob >= today:
            return "DOB cannot be in the future."

        age = (today - dob).days // 365
        
        if age < 5:
            return "Player must be at least 5 years old."
        if age > 100:
            return "Player age cannot exceed 100."

        player.dob = dob
        
        return True

    def check_player_name(self, player: Player):
        """VALIDATES PLAYER FULL NAME FORMAT"""
        
        self.name = player.name.strip()
        parts = self.name.split()

        if len(self.name) < 2 or len(self.name) > 60:
            return "Name must be between 2 and 60 characters."
        
        if "  " in self.name:
            return "Name cannot contain consecutive spaces."
        
        if self.name != self.name.title():
            corrected = ' '.join(part.capitalize() for part in parts)
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
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in self.name):
            return "Field contains invalid special characters."

        return True

    # ----------------------------------------------------------------------
    # PHONE / EMAIL / ADDRESS VALIDATION
    # ----------------------------------------------------------------------
    
    def validate_phone(self, phone: str) -> None:
        """VALIDATES PHONE NUMBER FORMAT 123-4567"""
    
        if "-" not in phone:
            phone = phone[:3] + "-" + phone[3:]
    
        if len(phone) != 8:
            return "Phone number must be in format 123-4567."
        left, right = phone.split("-")
    
        if not (left.isdigit() and right.isdigit()):
            return "Phone can only contain digits and one dash."
    
        if len(left) != 3 or len(right) != 4:
            return "Phone number must be in format 123-4567."
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in phone):
            return "Field contains invalid special characters."
    
        return None

    def validate_email(self, email: str) -> None:
        """VALIDATES EMAIL FORMAT"""
    
        len_email = len(email)
        att_symbol = email.find("@")
        email_split = email.split("@")
        two_dots = email.find("..")
        size = email.count("@")
        pat = email.find(".@")

        if "@" not in email:
            return "@ symbol is missing."
    
        if size > 1:
            second_at = email.find("@", att_symbol + 1)
            return f"{email}\n{' ' * second_at}^--there is an extra @ symbol here."
    
        if email[0] == "@" and att_symbol == 0:
            return "There is nothing before the @ symbol."
    
        if att_symbol == len_email - 1:
            return f'{email}\n{" " * att_symbol}^--there is nothing after the @ symbol.'
    
        if email[0] == ".":
            return "Email address starts with a dot."
    
        if ".." in email:
            return f"{email}\n{' ' * two_dots}^--there are consecutive dots here."
    
        if ".@" in email:
            return f"{email}\n{' ' * pat}^--there is an extra dot here."
    
        if "." not in email_split[1]:
            return "Top-level domain is missing."
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in email):
            return "Field contains invalid special characters."
    
        return None

    def validate_address(self, address: str) -> None:
        """VALIDATES ADDRESS FORMAT"""
    
        if not address:
            return "Address cannot be empty"
    
        if not any(char.isdigit() for char in address):
            return "Address must contain a number"
    
        if "  " in address:
            return "Adress cannot contain consecutive spaces"
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in address):
            return "Field contains invalid special characters."
    
        return None

    # ----------------------------------------------------------------------
    # HANDLE VALIDATION
    # ----------------------------------------------------------------------
    
    def check_if_handle_in_use(self, handle_str):
        """CHECKS IF A HANDLE IS ALREADY IN USE"""
    
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
    
        for player in player_list:
            if player.handle == handle_str:
                return True
    
        return False

    def check_if_handle_exists_with_player(self, player: Player):
        """CHECKS IF HANDLE EXISTS FOR A GIVEN PLAYER"""
    
        return self.check_if_handle_in_use(player.handle)

    # ----------------------------------------------------------------------

    def validate_club(self, club: Club):
        errors_list = []

        club_country = self.validate_club_country(club.country)
        club_home_town = self.validate_club_home_town(club.home_town)
        club_color = self.validate_club_color(club.colors)

        if club_country is not True:
            errors_list.append(f"Error: {club_country}") 
        
        if club_home_town is not True:
            errors_list.append(f"Error: {club_home_town}")

        if club_color is not True:
            errors_list.append(f"Error: {club_color}")

        if errors_list:
            return "\n".join(errors_list)
        return None


    def validate_club_country(self, club_country: str):
        if not club_country.isalpha():
            return "Country must be only letter"
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in club_country):
            return "Field contains invalid special characters."
        
        return True

    def validate_club_home_town(self, club_home_town: str):
        if not club_home_town.isalpha():
            return "Country must be only letter"
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in club_home_town):
            return "Field contains invalid special characters."

        return True

    def validate_club_color(self, club_colors: list[str]):
        for color in club_colors:
            if not color.isalpha():
                return "Color must be only letter"
            
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in color):
            return "Field contains invalid special characters."
            
        return True
            

    # CHECKS AND VALIpper)DATION METHODS FOR EVENT
    # ----------------------------------------------------------------------
    # CHECKS AND VALIDATION METHODS FOR EVENT
    # ----------------------------------------------------------------------
    def validate_event(self, event: Event):
        """VALIDATES EVENT NAME AND DATES"""
    
        errors_list = []
        event_name = self.check_event_name(event.event_name)
        event_start = self.check_start_date_event(event.start_date, event.tournament_name)
        event_end = self.check_end_date_event(event.end_date, event.tournament_name)

        if event_name is not True:
            errors_list.append(f"Name: {event_name}")
    
        if event_start is not True:
            errors_list.append(f"Start date: {event_start}")
    
        if event_end is not True:
            errors_list.append(f"End date: {event_end}")

        return errors_list if errors_list else None


    def check_event_name(self, event_name: str):
        """VALIDATES EVENT NAME"""
    
        if not event_name or not event_name.strip():
            return "Event name cannot be empty."
    
        if not event_name[0].isupper():
            event_name = event_name.capitalize()
    
        if not event_name.isalpha():
            return "Event name must contain only letters"
    
        if len(event_name) > 20:
            return "Event name is too long (max 20 characters)."

        special_char = r'!\"#%&/()='

        if any(char in special_char for char in event_name):
            return "Field contains invalid special characters."
    
        return True

    def check_start_date_event(self, start_date: str, tournament_name: str):
        """VALIDATES EVENT START DATE AGAINST TOURNAMENT"""
    
        try:
            start_date_event: datetime = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            return "Event must be in YYYY-MM-DD format."
                
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in start_date_event):
            return "Field contains invalid special characters."
    
        start_tournament = self.view_start_date_of_tournament(tournament_name)
    
        if isinstance(start_tournament, str):
            return start_tournament
    
        if start_date_event.date() < start_tournament:
            return f"Event cannot start before the tournament start date ({start_tournament})."
    
        return True

    def check_end_date_event(self, end_date: str, tournament_name):
        """VALIDATES EVENT END DATE AGAINST TOURNAMENT"""
    
        try:
            end_date_event: datetime = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return "Event must be in YYYY-MM-DD format."
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in end_date_event):
            return "Field contains invalid special characters."
    
        end_tournament = self.view_end_date_of_tournament(tournament_name)
    
        if isinstance(end_tournament, str):
            return end_tournament
    
        if end_date_event.date() > end_tournament:
            return f"Event cannot end after the tournament end date ({end_tournament})."
    
        return True

    def view_start_date_of_tournament(self, tournament_name):
        """RETURNS START DATE OF TOURNAMENT"""
    
        tournament_list: list[Tournament] = self._dl_wrapper.read_tournament_file()
    
        for tournament in tournament_list:
            if tournament.tournament_name == tournament_name:
                return tournament.start_date
    
        return "Tournament not found"

    def view_end_date_of_tournament(self, tournament_name):
        """RETURNS END DATE OF TOURNAMENT"""
    
        tournament_list: list[Tournament] = self._dl_wrapper.read_tournament_file()
    
        for tournament in tournament_list:
            if tournament.tournament_name == tournament_name:
                return tournament.end_date
    
        return "Tournament not found"

    # ----------------------------------------------------------------------
    # TOURNAMENT VALIDATION
    # ----------------------------------------------------------------------
    
    def validate_tournament(self, tournament: Tournament):
        """VALIDATES TOURNAMENT NAME, DATES, AND CONTACT INFO"""
    
        errors = []
        check_name = self.check_tournament_name(tournament)
        check_dates = self.check_dates(tournament)
        check_contact_name = self.check_contact_name(tournament)
        check_contact_email = self.check_contact_email(tournament)
        check_contact_phone = self.check_contact_phone(tournament)

        if check_name is not True:
            errors.append(f"Name: {check_name}")
    
        if check_dates is not True:
            errors.append(f"Dates: {check_dates}")
    
        if check_contact_name is not True:
            errors.append(f"Contact Name: {check_contact_name}")
    
        if check_contact_email is not True:
            errors.append(f"Contact Email: {check_contact_email}")
    
        if check_contact_phone is not True:
            errors.append(f"Contact Phone: {check_contact_phone}")

        return errors if errors else None

    def check_tournament_name(self, tournament: Tournament):
        """VALIDATES TOURNAMENT NAME"""
    
        tournament_name = tournament.tournament_name.strip()
    
        if len(tournament_name) == 0:
            return "Tournament name cannot be empty."
    
        if len(tournament_name) < 3 or len(tournament_name) > 60:
            return "Tournament name must be between 3–60 characters."
        

        special_char = r'!\"#¤%&/()='


        if any(char in special_char for char in tournament_name):
            return "Field contains invalid special characters."
    
        return True

    def check_dates(self, tournament: Tournament):
        """VALIDATES TOURNAMENT START AND END DATES"""
    
        try:
            self.start = datetime.strptime(tournament.start_date, "%Y-%m-%d")
            self.end = datetime.strptime(tournament.end_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use yyyy-mm-dd"
    
        if self.start >= self.end:
            return "Start date must be before end date."
    
        if (self.end - self.start).days < 4:
            return "Tournament must span more then 4 days."
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in self.start):
            return "Field contains invalid special characters."
        
        if any(char in special_char for char in self.end):
            return "Field contains invalid special characters."
    
        return True

    def check_contact_name(self, tournament: Tournament):
        """VALIDATES TOURNAMENT CONTACT NAME"""
    
        check_contact_name = tournament.contact_name.strip()
        if len(check_contact_name) == 0:
            return "Contact name cannot be empty."
    
        if len(check_contact_name) < 3:
            return "Contact name must be at least 3 characters."
        
        special_char = r'!\"#%&/()='

        if any(char in special_char for char in check_contact_name):
            return "Field contains invalid special characters."
    
        return True

    def check_contact_email(self, tournament: Tournament):
        """VALIDATES TOURNAMENT CONTACT EMAIL"""
    
        check_contact_email = tournament.contact_email.strip()
        result = self.validate_email(check_contact_email)
    
        if result is not None:
            return f"Invalid email: {result}"
    
        return True

    def check_contact_phone(self, tournament: Tournament):
        """VALIDATES TOURNAMENT CONTACT PHONE"""
    
        check_contact_phone = tournament.contact_phone.strip()
        result = self.validate_phone(check_contact_phone)
    
        if result is not None:
            return f"Invalid phone: {result}"
    
        return True
