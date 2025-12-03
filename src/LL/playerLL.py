from models.player import Player

class PlayerLL:
    def __init__(self, dl_wrapper):
        self._dl_wrapper = dl_wrapper
        
    def create_player(self, player: Player):

        validate_errors = self.validate_player(player)

        if validate_errors:
            return validate_errors
        
        self._dl_wrapper.create_player(player)
        return "Success"



    def edit_player(id: int) -> id: # id, phone and location
        pass 

    # def check_player_dob(player: Player):
    #     dob = player.dob
    # TODO 

    def check_player_name(player: Player):
        raw_name = player.name
        stripname = raw_name.strip()
        name_parts = stripname.split()
        
        """""
        if not stripname.isalpha():
            return "Not allow"
        """""
        # if raw_name in Data:
        #     return "Already in Data" 
        # TODO data connection

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
        phone = player.phone

        if len(phone) != 8:
            return "not valid"

        if "-" not in phone:
            return "not valid"
        
        return True

    
    def check_player_email(player: Player):
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
        Validates a player object.
        Returns the player object if valid.
        Returns a LIST of error strings if invalid.
        """
        errors = [] # A list to hold all error messages

        check_name = PlayerLL.check_player_name(player)
        check_email = PlayerLL.check_player_email(player)
        check_phone = PlayerLL.check_player_phone(player)
        # check_dob = PlayerLL.check_player_dob(player)
        #TODO 


        if check_name is not True:
            errors.append(f"Name : {check_name}")

        
        if check_email is not True:
            errors.append(f"Email : {check_email}")

        
        if check_phone is not True:
            errors.append(f"Phone : {check_phone}")
        
        
        # if check_dob is not True:
        #     errors.append(f"DOB Error: {check_dob}")
        #TODO

        # If the errors list is not empty, return it
        if errors:
            return errors
        
        # Otherwise, all checks passed
        return None

         