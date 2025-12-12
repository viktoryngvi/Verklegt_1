from IO.Player_IO import Player_IO
from IO.Teams_IO import Team_IO
from IO.Event_IO import Event_IO
from IO.Tournament_IO import Tournament_IO
from IO.Club_IO import Club_IO
from models.event_blueprint import Event_blueprint
from models.match import Match

class DLWrapper:
    """Central wrapper for all IO operations: 
    loads, creates, updates, and stores players, teams, events, matches, tournaments, and clubs."""



    def __init__(self):
        self.playerio = Player_IO()
        self.teamio = Team_IO()
        self.event_blueprintio = Event_IO()
        self.tournamentio = Tournament_IO()
        self.clubio = Club_IO()
        self.match = Match()
        self.event_blueprint = Event_blueprint()

    # ----------------------------------------------------------------------
    # PLAYER METHODS
    # ----------------------------------------------------------------------

    def load_all_player_info(self):
        """lOADS ALL PLAYER INFO FROM INPUT"""
        return self.playerio.load_all_player_info()

    def create_player(self, player_data :Player_IO):
        """TAKES ALL PLAYER INFO AND APPENDS THAT INTO THE PLAER FILE"""
        return self.playerio.create_player(player_data)
    
    def edit_player_file(self, player_data):
        """EDITS PLAYER INFORAMTION THAT WAS INPUTTED, AND UPATES IT"""
        return self.playerio.edit_player_file(player_data)
    
    # ----------------------------------------------------------------------
    # TEAM METHODS
    # ----------------------------------------------------------------------

    def view_all_teams(self):
        """returns a list of dictionarys of all teams"""
        return self.teamio.view_all_teams()
    
    def append_team_into_file(self, team):
        """APPENDING NEWLY CREATED TEAM"""
        return self.teamio.append_team_into_file(team)
    
    def edit_teams_file(self, teams_file):
        """UPDATES TEAM CAPTAIN"""
        return self.teamio.edit_teams_file(teams_file)
    # er ekki tengt!!!!!!!!!!!!!!!!

    # ----------------------------------------------------------------------
    # TOURNAMENT METHODS
    # ----------------------------------------------------------------------

    def read_tournament_file(self):
        """READ TOURNAMENT FILES AND RETURNS THE INFORMATION """
        return self.tournamentio.read_tournament_file()
    
    def write_into_file(self, tournament_data):
        """WRITE / APPEND INTO TOURNAMENT DATA FILE """
        return self.tournamentio.write_into_file(tournament_data)

    # ----------------------------------------------------------------------
    # EVENT METHODS
    # ----------------------------------------------------------------------

    def create_empty_event(self, event_blueprint: Event_blueprint):
        """CREATES EMPTY EVENT AND SAVES INFO INTO CSV"""
        return self.event_blueprintio.create_empty_event(event_blueprint)

    def load_event_blueprint(self):
        """LOADS ALL EVENT BLUEPRINT INFORMATION FROM FILE"""
        return self.event_blueprintio.load_event_blueprint()

    
    def append_team_into_blueprint(self, team_data: Event_blueprint):
        """APPENDS A TEAM INTO AN EXISTING EVENT BLUEPRINT"""
        return self.event_blueprintio.append_team_into_blueprint(team_data)

    
    def load_match_file(self):
        """LOADS ALL MATCHES FROM MATCH FILE"""
        return self.event_blueprintio.load_match_file()

    
    def append_to_match_file(self, match: Match):
        """APPENDS A NEW MATCH INTO THE MATCH FILE"""
        return self.event_blueprintio.append_to_match_file(match)

    
    def edit_match_file(self, matches: list[Match]):
        """UPDATES EXISTING MATCH INFORMATION IN THE MATCH FILE"""
        return self.event_blueprintio.edit_match_file(matches)

    
    def read_results_file(self):
        """READS ALL RESULTS FROM RESULTS FILE"""
        return self.event_blueprintio.read_results_file()

    
    def append_into_results(self, matches_to_append: list[Match]):
        """APPENDS NEW MATCH RESULTS INTO THE RESULTS FILE"""
        return self.event_blueprintio.append_into_results(matches_to_append)

    
    # ----------------------------------------------------------------------
    # CLUB METHODS
    # ----------------------------------------------------------------------

    def register_club(self, club):
        """REGISTERS A NEW CLUB INTO THE CLUB FILE"""
        return self.clubio.register_club(club)

    
    def add_team_to_club(self, clubs):
        """ADDS A TEAM UNDER THE SPECIFIED CLUB"""
        return self.clubio.add_team_to_club(clubs)

    
    def load_clubs(self):
        """LOADS ALL CLUBS FROM FILE"""
        return self.clubio.view_clubs()


    def view_clubs(self):
        """RETURNS A LIST OF ALL CLUBS"""
        return self.clubio.view_clubs()

    
    def view_club_information(self, club_name):
        """RETURNS DETAILED INFORMATION ABOUT A SPECIFIC CLUB"""
        return self.clubio.view_club_information(club_name)

    
    def check_if_club_name_in_use(self, club_name):
        """CHECKS IF A CLUB NAME IS ALREADY REGISTERED"""
        return self.clubio.check_if_club_name_in_use(club_name)

