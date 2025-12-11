from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.club import Club

class ClubLL:
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self.dl_wrapper = dl_wrapper
        self.validate = validate
    
    def load_clubs(self):
        return self.dl_wrapper.load_clubs()
    
    def create_club(self, club: Club):
        club_name = club.name
        if self.dl_wrapper.check_if_club_name_in_use(club_name):
            return "Error: Club name already exists"
        
        validate_errors = self.validate.validate_club(club)

        if validate_errors:
            return validate_errors

        return self.dl_wrapper.register_club(club)
    
    def view_club_information(self, club_name: str):
        return self.dl_wrapper.view_club_information(club_name)






