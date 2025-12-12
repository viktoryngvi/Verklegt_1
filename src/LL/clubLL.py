from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.club import Club

class ClubLL:
    """HANDLES CLUB OPERATIONS: CREATE CLUBS, ADD TEAMS, VIEW CLUBS"""

    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self.dl_wrapper = dl_wrapper
        self.validate = validate
    
    # ----------------------------------------------------------------------
    # LOAD CLUBS
    # ----------------------------------------------------------------------

    def load_clubs(self):
        """LOADS ALL CLUBS FROM FILE"""
        return self.dl_wrapper.load_clubs()
    
    # ----------------------------------------------------------------------
    # CREATE CLUB
    # ----------------------------------------------------------------------

    def create_club(self, club: Club):
        """CREATES A NEW CLUB IF NAME IS UNIQUE AND VALID"""
    
        club_name = club.name
    
        if self.dl_wrapper.check_if_club_name_in_use(club_name):
            return "Error: Club name already exists"
        
        validate_errors = self.validate.validate_club(club)

        if validate_errors:
            return validate_errors

        return self.dl_wrapper.register_club(club)
    
    # ----------------------------------------------------------------------
    # ADD TEAM TO CLUB
    # ----------------------------------------------------------------------

    def add_team_to_club(self, club_name: str, team_name: str):
        """ADDS A TEAM TO AN EXISTING CLUB"""
    
        clubs = self.dl_wrapper.load_clubs()  # list[Club]
    
        target = next((c for c in clubs if c.name == club_name), None)
    
        if not target:
            return "Club not found"

        if team_name not in target.teams:
            target.teams.append(team_name)

        return self.dl_wrapper.add_team_to_club(clubs)  # writes full list
    
    # ----------------------------------------------------------------------
    # VIEW CLUB INFORMATION
    # ----------------------------------------------------------------------

    def view_club_information(self, club_name: str):
        """RETURNS INFORMATION FOR A SPECIFIC CLUB"""
    
        return self.dl_wrapper.view_club_information(club_name)


