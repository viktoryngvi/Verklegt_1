import csv
import os
# from models.player import Player
from IO.Player_IO import Player_IO

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()

    def create_player(self, player : Player_IO):
         return self.playerio.create_player(player)
    
    def check_if_player_exists(self, player : Player_IO):
        return self.playerio.check_if_player_exists(player)
    
    def edit_player_info(self, player : Player_IO):
        return self.playerio.edit_player_info(player)
    
    def load_all_player_short_info(self, player : Player_IO):
        return self.playerio.load_all_player_short_info(player)
    
    def load_all_player_info(self, player : Player_IO):
        return self.playerio.load_all_player_info(player)
    
    def check_if_team_exists(self, player : Player_IO):
        return self
    
    def check_if_player_in_team(self, player : Player_IO):
        return self
    
    def check_if_handle_exists(self, player : Player_IO):
        return self