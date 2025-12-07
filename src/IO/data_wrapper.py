import csv
import os
from IO.Player_IO import Player_IO
from Teams_IO import Team_IO
from IO.Tournament_Blueprint_IO import Tournament_Blueprint_IO
# from IO.event_io import EventIO
# from IO.tournament_io import TournamentIO
# from models.tournament import Tournament

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.teamio = Team_IO()
        self.empty_tournament = Tournament_Blueprint_IO()
        # self.eventio = EventIO()
        # self.tournamentio = TournamentIO()

    # Player methods
    def create_player(self, player : Player_IO):
         return self.playerio.create_player(player)

    def check_if_player_exists(self, player : Player_IO):
        return self.playerio.check_if_player_exists(player)
    
    def edit_player_info(self, handle, str_to_change, new_change):
        return self.playerio.edit_player_info(handle, str_to_change, new_change)
    
    def load_all_player_short_info(self):
        return self.playerio.load_all_player_short_info(self)
    
    def load_all_player_info(self):
        return self.playerio.load_all_player_info(self)
    
    def check_if_handle_exists_with_player(self, player : Player_IO):
        return self.playerio.check_if_handle_exists_with_player(player)
    
    def check_if_handle_exists_with_handle(self, handle):
        return self.playerio.check_if_handle_exists_with_handle(handle)
    
    def check_last_id(self):
        return self.playerio.check_last_id(self)
    
    def Check_if_specific_id_exists(self):
        pass
        


    # team methods

    def create_team(self, team_name, captain_id, list_of_player_ids):
        return self.teamio.create_team(self)

    def check_if_team_name_exists(self):
        return self.teamio.check_if_team_name_exists(self)

    # def check_if_player_in_team(self):
    #     return self
    
    def change_team_captain(self, find_team, new_captain):
        return self.teamio.change_team_captain(self)
    
    def view_all_teams(self):
        return self.teamio.view_all_teams(self)
    
    def players_team_none(self):
        """retruns a list of players(id, name and handle) that dont have a team"""
        return self.teamio.players_team_none(self)
    
    def view_all_players_in_team(self):
        return self.teamio.view_all_players_in_team(self)
    
    def view_all_teams_nae_and_captains(self):
        return self.teamio.view_all_players_in_team(self)

    def check_if_player_handle_in_team(self, handle):
        return self.teamio.check_if_player_handle_in_team(self)
    




    # -------------------------
    # Event / Schedule Methods
    # -------------------------
    def save_event(self, tournament_name, event):
        """Save Event + Matches into CSV (delegated to EventIO)."""
        return self.eventio.save_event(tournament_name, event)

    def load_event(self, tournament_name):
        """Load Event + Matches from CSV (delegated to EventIO)."""
        return self.eventio.load_event(tournament_name)

    # # ---- TOURNAMENT METHODS ----
    # def create_tournament(self, tournament: Tournament):
    #     return self._tournament_io.create_tournament(tournament)

    # def load_all_tournaments(self):
    #     return self._tournament_io.load_all_tournaments()
    
    # def save_match_result(self):
    #     pass #TODO Match Result
    

    