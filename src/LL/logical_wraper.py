from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from LL.validate import Validate
from models import tournament
from models.player import Player
from models.tournament import Tournament
from models.event import Event

class LLWrapper:
   def __init__(self):
      self.dl_wrapper = DLWrapper()
      self.validate = Validate(self.dl_wrapper)
      self.player_ll = PlayerLL(self.dl_wrapper, self.validate)

   def create_player(self, player: Player):
      return self.player_ll.create_player(player)

   def create_tournament(self, tournament_name: Tournament):
      return self.dl_wrapper.create_tournament(tournament)
   
   def generate_schedule(tournament: Tournament, event: Event):
      pass
   
   def enter_match_result(self):
      pass
   
   def change_team_captain(self):
      pass
   

   
   def assign_point(self):
      pass
   
   def get_statistics(self, ptc: str): #PTC = Player Team Club
      pass
   