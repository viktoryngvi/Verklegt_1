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
    def create_player(self, player : Player_IO):
        """takes all player info and appends that into the player file"""
        return self.playerio.create_player(player)

    def edit_player_info(self, handle, str_to_change, new_change):
        """takes new value and changes the old value to the new desired input"""
        return self.playerio.edit_player_info(handle, str_to_change, new_change)

    def load_all_player_info(self):
        """returns a list of dictionarys of all players"""
        return self.playerio.load_all_player_info(self)

    def load_all_player_short_info(self):
        """loads all the players and gives a list of dictionarys of each players id, name, handle and team name"""
        return self.playerio.load_all_player_short_info(self)

    def check_if_handle_exists_with_handle(self, handle):
        """takes handle and checks player_list if that handle is in use"""
        return self.playerio.check_if_handle_in_use(handle)

    def check_if_handle_exists_with_player(self, player: Player_IO):
        """takes player object and gets the handle and checks if that handle is in use"""
        return self.playerio.check_if_handle_exists_with_player(player)

    def check_last_id(self):
        """checks the last players id (used to check how many players have been created)"""
        return self.playerio.check_last_id(self)

    # team methods

    def create_team(self, team_name, captain_id, list_of_player_ids):
        """takes team_name, team_captain_id and a list of player_ids and creates the team in the csv file"""
        return self.teamio.create_team(team_name, captain_id, list_of_player_ids)

    def check_if_team_name_exists(self, team_name):
        """takes a team name and checks if that team name is in use"""
        return self.teamio.check_if_team_name_exists(self, team_name)
    
    def change_team_captain(self, find_team, new_captain):
        """takes the team name, new captain and changes the captain of the team"""
        return self.teamio.change_team_captain(self, find_team, new_captain)
    
    def view_all_teams(self):
        """returns a list of dictionarys of all teams"""
        return self.teamio.view_all_teams(self)
    
    def players_team_none(self):
        """returns a list of players(id, name and handle) that dont have a team"""
        return self.teamio.players_team_none(self)
    
    def view_all_players_in_team(self, team_name):
        """takes a team name and returns a list of dictionary containing: team_name, team_captain and a list of all players in team"""
        return self.teamio.view_all_players_in_team(self, team_name)
    
    def view_all_team_names_and_captains(self):
        """gives only team_name and team_captain of all teams in file"""
        return self.teamio.view_all_team_names_and_captains(self)

    def check_if_player_handle_in_team(self, team, handle):
        """takes team_name and handle and checks if the handle is in in the team"""
        return self.teamio.check_if_player_handle_in_team(self, team, handle)
    
    def view_captains_team(self, find_captains_handle):
        """takes a captains handle and gives all the information of the team"""
        return self.teamio.view_captains_team(self, find_captains_handle)
    
    def view_captain_team_by_team_name(self, team_name):
        return self.teamio.view_captain_team_by_team_name(self, team_name)


    # event blueprint methods:

    def create_empty_event(self):
        """creates an empty event for organizer to fill out before making public"""
        return self.event_blueprintio.create_empty_event(self)
    
    def write_team_into_empty_event(self, team):
        """takes team name and puts into the event"""
        return self.event_blueprintio.write_team_into_empty_event(self, team)
    
    def check_if_team_in_event(self, team):
        """checks if the team is already in the event_blueprint"""
        return self.event_blueprintio.check_if_team_in_event(self, team)
    
    def how_many_teams_in_event(self):
        """checks how many teams have been registered intp the event_blueprint returns int"""
        return self.event_blueprintio.how_many_teams_in_event(self)
    
    def move_blueprint_to_knockout(self):
        return self.event_blueprintio.move_blueprint_to_knockout(self)
    
    def move_blueprint_to_last_team_standing(self):
        return self.event_blueprintio.move_blueprint_to_last_team_standing()

    # knockout style mothods:

    def input_match_result(self, match_id, team_a_score, team_b_score):
        return self.knockoutio.input_match_results(self, match_id, team_a_score, team_b_score)

    def create_first_round(self):
        return self.knockoutio.create_first_round(self)

    def create_second_round(self):
        return self.knockoutio.create_second_round(self)
    
    def create_third_round(self):
        return self.knockoutio.create_second_round(self)

    def create_fourth_round(self):
        return self.knockoutio.create_fourth_round(self)
    
    def declare_winner(self):
        return self.knockoutio.declare_winner(self)
    
    def how_many_matches_have_winners(self):
        return self.knockoutio.how_many_matches_have_winners(self)
    

    # tournament methods

    def create_tournament(self, tournament: Tournament_IO):
        return self.tournamentio.create_tournament(tournament)
    
    def put_event_into_tournament(self, torunament_name, event_name):
        return self.tournamentio.put_event_into_tournament(self, torunament_name, event_name)
    
    def view_tournaments(self):
        return self.tournamentio.view_tournaments()
    
    def view_events_in_tournaments(self, tournament_name):
        return self.tournamentio.view_events_in_tournament(tournament_name)
    
    # club methods:

    def register_club(self, club: Club_IO):
        return self.clubio.register_club(club)
    
    def add_team_to_club(self, club_name, team_name):
        return self.clubio.add_team_to_club(club_name, team_name)
    
    def view_clubs(self):
        return self.clubio.view_clubs(self)
    
    def view_club_information(self, club_name):
        return self.clubio.view_club_information(club_name)
    
    def check_if_club_name_in_use(self, club_name):
        return self.clubio.check_if_club_name_in_use(club_name)