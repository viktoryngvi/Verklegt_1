from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from LL.validate import Validate
from LL.teamLL import TeamLL
from LL.clubLL import ClubLL
from LL.captainLL import CaptainLL
from LL.TournamentLL import TournamentLL   # ← FIXED IMPORT
from models.club import Club
from models.player import Player
from models.tournament import Tournament
from models.event import Event

class LLWrapper:
   def __init__(self):
      self.dl_wrapper = DLWrapper()
      self.validate = Validate(self.dl_wrapper)
      self.team_ll = TeamLL(self.dl_wrapper)
      self.club_ll = ClubLL(self.dl_wrapper, self.validate)
      self.captain_ll = CaptainLL(self.dl_wrapper, self.validate)
      self.player_ll = PlayerLL(self.dl_wrapper, self.validate)
      self.tournament_ll = TournamentLL(self.dl_wrapper)

   #PLAYER METHODS   
      
   def create_player(self, player: Player): 
      return self.player_ll.create_player(player)
   
   def edit_player_email(self, handle: str, email: str) -> str: 
      return self.player_ll.edit_player_email(handle, email)

   def edit_player_phone(self, handle: str, phone: str) -> str:
      return self.player_ll.edit_player_phone(handle, phone)

   def edit_player_address(self, handle: str, address: str) -> str:
      return self.player_ll.edit_player_address(handle, address)

   def edit_player_handle(self, handle: str, handle_str: str) -> str:
      return self.player_ll.edit_player_handle(handle, handle_str)
   
   def load_player_info(self, handle):
      return self.player_ll.load_player_info(handle)
   
   #CAPTAIN METHODS
   
   def edit_player_email_captain(self, team: str, handle: str, email: str) -> str: 
      return self.captain_ll.edit_player_email_cap(team, handle, email)

   def edit_player_phone_captain(self, team: str, handle: str, phone: str) -> str:
      return self.captain_ll.edit_player_phone_cap(team, handle, phone)

   def edit_player_address_captain(self, team: str, handle: str, address: str) -> str:
      return self.captain_ll.edit_player_address_cap(team, handle, address)

   def edit_player_handle_captain(self, team: str, handle: str, handle_str: str) -> str:
      return self.captain_ll.edit_player_handle_cap(team, handle, handle_str)

   def view_all_players_in_team(self, team_name): # Players in captains team
      return self.captain_ll.view_all_players_in_team(team_name)
   
   def update_team_captain(self, team_name, handle):
      return self.captain_ll.update_team_captain(team_name, handle)
   
   #TEAM METHODS

   def create_team(self, cap_id: int, team_name: str, players_id: list): 
      return self.team_ll.create_team(cap_id, team_name, players_id)
   
   def load_player_short_info(self): # Id, Name, Handle, Team PUBLIC INFO
      return self.team_ll.load_player_short_info()
   
   def view_all_teams(self):
      return self.team_ll.view_all_teams()
   
   def get_players_in_team(self, team_name):
      return self.team_ll.view_all_players_in_team(team_name)
   
   #MATCH METHODS

   def enter_match_result(self):
      pass

   #CLUBS METHODS

   def load_clubs(self):
      return self.club_ll.load_clubs()
   
   def create_club(self, club: Club):
      return self.club_ll.create_club(club)
   
   #TOURNAMENT METHODS

   def create_tournament(self, tournament: Tournament):
      return self.tournament_ll.create_tournament(tournament)
   
   def get_tournament_list(self):
      return self.tournament_ll.get_tournament_list()
   
   def get_events_in_tournament(self, tournament_name):
      return self.tournament_ll.get_events_in_tournament(tournament_name)
   

   def generate_schedule(tournament: Tournament, event: Event):
      pass

   def get_tournament_schedule(self, tournament_name, event_in_tournament):
      return self.tournament_ll.get_tournament_schedule(tournament_name, event_in_tournament)
   

   def assign_point(self):
      pass
   
   def get_statistics(self, ptc: str): #PTC = Player Team Club
      pass
   

# ----------------------------------------------------------------------
# date validation
# ----------------------------------------------------------------------   

   def get_event_types(self):
        return [
            "Single Elimination",
            "Double Elimination",
            "Last Team Standing"]