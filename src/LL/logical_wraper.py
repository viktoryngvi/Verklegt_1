from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from models.player import Player
from models.tournament import Tournament
from models.event import Event

class LLWrapper:
   def __init__(self):
      self.dl_wrapper = DLWrapper()
      self.player_ll = PlayerLL(self.dl_wrapper)

      
   def create_player(self, player: Player):
      return self.player_ll.create_player(player)

   def create_tournament():
      pass
   
   def generate_schedule(tournament: Tournament, event: Event):
      pass
   
   def enter_match_result():
      pass
   
   def change_team_captain():
      pass
   

   
   def assign_point():
      pass
   
   def get_statistics(ptc: str): #PTC = Player Team Club
      pass