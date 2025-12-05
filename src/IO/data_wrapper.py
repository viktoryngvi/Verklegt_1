
import csv
import os
from IO.Player_IO import Player_IO
from IO.event_io import EventIO
from IO.tournament_io import TournamentIO
from models.tournament import Tournament

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.eventio = EventIO()
        self.tournamentio = TournamentIO()

    # -------------------------
    # Existing Player Methods
    # -------------------------
    def create_player(self, player : Player_IO):
         return self.playerio.create_player(player)

    def check_if_player_exists(self, player : Player_IO):
        return self.playerio.check_if_player_exists(player)
    
    def edit_player_info(self, player: Player_IO):
        return self.playerio.edit_player_info(player)
    
    def load_all_player_short_info(self, player: Player_IO):
        return self.playerio.load_all_player_short_info(player)
    
    def load_all_player_info(self, player: Player_IO):
        return self.playerio.load_all_player_info(player)
    


    def check_if_team_exists(self, player : Player_IO):
        return self

    def check_if_player_in_team(self, player : Player_IO):
        return self
    #TODO

    def check_if_handle_exists(self, player : Player_IO):
        return self.playerio.check_if_handle_exists(player)



    # -------------------------
    # Event / Schedule Methods
    # -------------------------
    def save_event(self, tournament_name, event):
        """Save Event + Matches into CSV (delegated to EventIO)."""
        return self.eventio.save_event(tournament_name, event)

    def load_event(self, tournament_name):
        """Load Event + Matches from CSV (delegated to EventIO)."""
        return self.eventio.load_event(tournament_name)

    # ---- TOURNAMENT METHODS ----
    def create_tournament(self, tournament: Tournament):
        return self._tournament_io.create_tournament(tournament)

    def load_all_tournaments(self):
        return self._tournament_io.load_all_tournaments()
    
    def save_match_result(self):
        pass #TODO Match Result
    

    