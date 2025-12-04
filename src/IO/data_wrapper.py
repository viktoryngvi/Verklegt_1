import csv
import os
from IO.Player_IO import Player_IO
from IO.event_io import EventIO   # <-- ADD THIS

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.eventio = EventIO()       # <-- ADD THIS

    # -------------------------
    # Existing Player Methods
    # -------------------------
    def create_player(self, player : Player_IO):
         return self.playerio.create_player(player)
<<<<<<<<< Temporary merge branch 1
    
=========

>>>>>>>>> Temporary merge branch 2
    def check_if_player_exists(self, player : Player_IO):
        return self.playerio.check_if_player_exists(player)
    
    def edit_player_info(self, player : Player_IO):
        return self.playerio.edit_player_info(player)
    
    def load_all_player_short_info(self, player : Player_IO):
        return self.playerio.load_all_player_short_info(player)
    
    def load_all_player_info(self, player : Player_IO):
        return self.playerio.load_all_player_info(player)
<<<<<<<<< Temporary merge branch 1
    
    def check_if_team_exists(self, player : Player_IO):
        return self
    
    def check_if_player_in_team(self, player : Player_IO):
        return self
    
    def check_if_handle_exists(self, player : Player_IO):
        return self
=========

    # -------------------------
    # NEW Tournament Schedule Methods
    # -------------------------
    def save_event(self, tournament_name, event):
        """
        Save Event + Matches into CSV (delegated to EventIO)
        """
        return self.eventio.save_event(tournament_name, event)

    def load_event(self, tournament_name):
        """
        Load Event + Matches from CSV (delegated to EventIO)
        """
        return self.eventio.load_event(tournament_name)
>>>>>>>>> Temporary merge branch 2
