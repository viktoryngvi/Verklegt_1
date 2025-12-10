from IO.Player_IO import Player_IO
from IO.Teams_IO import Team_IO
from IO.Event_IO import Event_IO
from IO.Tournament_IO import Tournament_IO
from IO.Club_IO import Club_IO

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.teamio = Team_IO()
        self.event_blueprintio = Event_IO()
        self.tournamentio = Tournament_IO()
        self.clubio = Club_IO()

    # Player methods

    def create_player(self, player_data :Player_IO):
        """takes all player info and appends that into the player file"""
        return self.playerio.create_player(player_data)
    
    def load_all_player_info(self):
        return self.playerio.load_all_player_info()

    # team methods


    def view_all_teams(self):
        """returns a list of dictionarys of all teams"""
        return self.teamio.view_all_teams()
    
    def write_team_into_file(self, teams_file):
        return self.teamio._write_team_into_file

    # event blueprint methods:
    def read_public_file_as_list_of_dict(self):
        return self.event_blueprintio.read_public_file_as_list_of_dict()
    
    def read_knockout_as_list_of_dict(self):
        return self.event_blueprintio.read_knockout_as_list_of_dict
    
    def read_last_team_standing_as_list_of_dict(self):
        return self.event_blueprintio.read_knockout_as_list_of_dict
    
    def write_into_event_blueprint(self, event_data):
        return self.event_blueprintio.write_into_event_blueprint(event_data)

    def move_to_knockout(self, public_data):
        return self.event_blueprintio.move_to_knockout(public_data)
        
    def move_to_last_team_standing(self, public_data):
        return self.event_blueprintio.move_to_last_team_standing(public_data)

    def read_results_file(self):
        return self.event_blueprintio.read_results_file

    def write_into_results(self, results_file):
        return self.event_blueprintio.write_into_results(results_file)
    
    # tournament methods

    def read_tournament_file(self):
        return self.tournamentio.read_tournament_file()
    
    def write_into_file(self, tournament_data):
        return self.tournamentio.write_into_file(tournament_data)

    # def create_tournament(self, tournament: Tournament_IO):
    #     return self.tournamentio.create_tournament(tournament)
    
    # def put_event_into_tournament(self, torunament_name, event_name):
    #     return self.tournamentio.put_event_into_tournament(torunament_name, event_name)
    
    # def view_tournaments(self):
    #     return self.tournamentio.view_tournaments()
    
    # def view_events_in_tournaments(self, tournament_name):
    #     return self.tournamentio.view_events_in_tournament(tournament_name)
    
    # club methods:

    def register_club(self, club: Club_IO):
        return self.clubio.register_club(club)
    
    def add_team_to_club(self, club_name, team_name):
        return self.clubio.add_team_to_club(club_name, team_name)
    
    def view_clubs(self):
        return self.clubio.view_clubs()
    
    def view_club_information(self, club_name):
        return self.clubio.view_club_information(club_name)
    
    def check_if_club_name_in_use(self, club_name):
        return self.clubio.check_if_club_name_in_use(club_name)
    
    # Event methods:

    def create_event(self, event: Event_IO):
        pass