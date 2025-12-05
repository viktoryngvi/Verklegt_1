from datetime import datetime
from models.player import Player
from IO.data_wrapper import DLWrapper
from models.person import Person

class PlayerLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper

        
    def create_player(self, player: Player):

        validate_errors = self.validate_player(player)

        if validate_errors:
            return validate_errors
        
        self._dl_wrapper.create_player(player)
        return "Success"


    def edit_player(self, player_name: str, email: str, phone: str, player_data: Player) -> str:
        
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


    def check_player_name(self, Player: Player):
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


    def check_player_dob(self, player: Player):
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


    def validate_player(self, player: Player):
        self.errors = []

        self.check_name = self.check_player_name(player)
        self.check_email = self.check_player_email(player)
        self.check_phone = self.check_player_phone(player)
        self.check_dob = self.check_player_dob(player)

        if self.check_name is not True:
            self.errors.append(f"Name: {self.check_name}")

        if self.check_email is not True:
            self.errors.append(f"Email: {self.check_email}")

        if self.check_phone is not True:
            self.errors.append(f"Phone: {self.check_phone}")

        if self.check_dob is not True:
            self.errors.append(f"DOB: {self.check_dob}")

        return self.errors if self.errors else None