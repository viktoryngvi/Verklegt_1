from IO.Player_IO import Player_IO
from IO.Teams_IO import Team_IO
from IO.Event_IO import Event_IO
from IO.Knockout_IO import Knockout
from IO.Tournament_IO import Tournament_IO
from IO.Club_IO import Club_IO

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.teamio = Team_IO()
        self.event_blueprintio = Event_IO()
        self.knockoutio = Knockout()
        self.tournamentio = Tournament_IO()
        self.clubio = Club_IO()

    # Player methods

    def create_player(self, player : Player_IO, id):
        """takes all player info and appends that into the player file"""
        return self.playerio.create_player(player, id)

    def edit_player_info(self, handle, str_to_change, new_change):
        """takes new value and changes the old value to the new desired input"""
        return self.playerio.edit_player_info(handle, str_to_change, new_change)

    def load_all_player_info(self):
        """returns a list of dictionarys of all players"""
        return self.playerio.load_all_player_info()

    def load_all_player_short_info(self):
        """loads all the players and gives a list of dictionarys of each players id, name, handle and team name"""
        return self.playerio.load_all_player_info()

    def check_if_handle_exists_with_handle(self, handle):
        """takes handle and checks player_list if that handle is in use"""
        return self.playerio.check_if_handle_in_use(handle)

    def check_if_handle_exists_with_player(self, player: Player_IO):
        """takes player object and gets the handle and checks if that handle is in use"""
        return self.playerio.check_if_handle_exists_with_player(player)

    def check_last_id(self):
        """checks the last players id (used to check how many players have been created)"""
        return self.playerio.check_last_id()

    def check_if_player_id_in_team(self, player_id):
        return self.playerio.check_if_player_id_in_team(player_id)
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