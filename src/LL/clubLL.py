from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.club import Club

class ClubLL:
    """HANDLES CLUB OPERATIONS: CREATE CLUBS, ADD TEAMS, VIEW CLUBS"""

    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self.dl_wrapper = dl_wrapper
        self.validate = validate
    
    
    def create_club(self, club: Club):
        """CREATES A NEW CLUB IF NAME IS UNIQUE AND VALID"""
    
        club_name = club.name
        if self.check_if_club_name_in_user(club_name):
            return "Error: Club name already exists"
        
        validate_errors = self.validate.validate_club(club)

        if validate_errors:
            return validate_errors

        return self.dl_wrapper.register_club(club)
    

    # def add_team_to_club(self, club_name: str, team_name: str):
    #     list_clubs: list[Club] = self.dl_wrapper.load_all_clubs()  # list[Club]
    #     target = next((c for c in clubs if c.name == club_name), None)
    #     if not target:
    #         return "Club not found"

    #     if team_name not in target.teams:
    #         target.teams.append(team_name)

    #     return self.dl_wrapper.add_team_to_club(clubs)  # writes full list
    
    def view_club_information(self, club_name: str):
        list_clubs: list[Club] = self.dl_wrapper.load_all_clubs() 
        for club in list_clubs:
            if club.name == club_name:
                return Club
            
        return "Club Not found"

    
    def check_if_club_name_in_user(self, club_name):
        club_list: list[Club] = self.dl_wrapper.load_all_clubs()
        for club in club_list:
            if club.name == club_name:
                return True
        
        return False


