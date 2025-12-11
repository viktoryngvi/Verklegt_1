from IO.data_wrapper import DLWrapper
from LL.playerLL import PlayerLL
from LL.validate import Validate
from LL.teamLL import TeamLL
from LL.clubLL import ClubLL
from LL.captainLL import CaptainLL
from LL.TournamentLL import TournamentLL 
from LL.eventLL import EventLL  
from LL.matchLL import MatchLL
from models.club import Club
from models.player import Player
from models.tournament import Tournament
from models.event import Event


class LLWrapper:
   def __init__(self):
      self.dl_wrapper = DLWrapper()
      self.validate = Validate(self.dl_wrapper)
      self.club_ll = ClubLL(self.dl_wrapper, self.validate)
      self.player_ll = PlayerLL(self.dl_wrapper, self.validate)
      self.team_ll = TeamLL(self.dl_wrapper, self.player_ll)
      self.captain_ll = CaptainLL(self.dl_wrapper, self.validate, self.team_ll)
      self.tournament_ll = TournamentLL(self.dl_wrapper)
      self.event_ll = EventLL(self.dl_wrapper)
      self.match_ll = MatchLL(self.dl_wrapper)
      self.get_team_captain_ll = self.captain_ll
      self.load_all_player_ll = self.player_ll

   #PLAYER METHODS   
      
   def create_player(self, player: Player): 
      return self.player_ll.create_player(player)
   
   def captain_handle(self, handle):
      return self.validate.check_if_handle_in_use(handle)
   
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
   
   def players_team_none(self):
      return self.team_ll.players_team_none()
   
   def take_id_return_handle(self, id):
      return self.player_ll.take_id_return_handle(id)
   
   def take_handle_return_id(self, handle):
      return self.player_ll.take_handle_retrun_id(handle)
   
   def take_list_of_players_return_list_of_ids(self, list_of_players: str):
      return self.player_ll.take_str_of_players_return_list_of_ids(list_of_players)
   
   def load_player_by_handle(self, handle):
      return self.player_ll.load_player_by_handle(handle)

   #CAPTAIN METHODS
   
   def edit_player_email_captain(self, team: str, handle: str, email: str) -> str: 
      return self.captain_ll.edit_player_email_cap(team, handle, email)

   def edit_player_phone_captain(self, team: str, handle: str, phone: str) -> str:
      return self.captain_ll.edit_player_phone_cap(team, handle, phone)

   def edit_player_address_captain(self, team: str, handle: str, address: str):
      return self.captain_ll.edit_player_address_cap(team, handle, address)

   def edit_player_handle_captain(self, team: str, handle: str, handle_str: str) -> str:
      return self.captain_ll.edit_player_handle_cap(team, handle, handle_str)

   def view_all_players_in_team(self, team_name): # Players in captains team
      return self.captain_ll.view_all_players_in_team(team_name)
   
   def view_captain_team(self, captain_handle : str):
      return self.captain_ll.view_captain_teams(captain_handle)
   
   def update_team_captain(self, team_name, handle):
      return self.captain_ll.update_team_captain(team_name, handle)
   
   #TEAM METHODS

   def create_team(self, team_name: str, cap_id: int, players_id: list): 
      return self.team_ll.create_team(team_name, cap_id,  players_id)
   
   def load_player_short_info(self): # Id, Name, Handle, Team PUBLIC INFO
      return self.team_ll.load_player_short_info()
   
   def load_all_player_short_info(self):
      return self.load_all_player_ll.load_all_player_short_info()
   
   def view_all_teams(self):
      return self.team_ll.view_all_teams()
   
   def get_players_in_team(self, team_name):
      return self.team_ll.view_all_players_in_team(team_name)
   
   def get_team_list(self):
      return self.team_ll.view_all_teams()
    
   def check_if_team_exists(self, captains_team: str) -> bool:
      return self.team_ll.check_if_team_name_exists(captains_team)
   

   #MATCH METHODS
   def enter_match_results(self):
      pass

   #CLUBS METHODS

   def load_clubs(self):
      return self.club_ll.load_clubs()
   
   def create_club(self, club: Club):
      return self.club_ll.create_club(club)
   
   def register_club(self, club: Club):
      return self.club_ll.create_club(club)
   
   def view_club_information(self, club_name: str):
      return self.club_ll.view_club_information(club_name)
   

   #TOURNAMENT METHODS

   def create_tournament(self, tournament: Tournament):
      return self.tournament_ll.create_tournament(tournament)
   
   def get_tournament_list(self):
      return self.tournament_ll.get_tournament_list()
   
   def get_events_in_tournament(self, tournament_name) :
      return self.tournament_ll.get_events_in_tournament(tournament_name)
   

   def generate_schedule(tournament: Tournament, event: Event):
      pass

   def get_tournament_schedule(self, tournament_name, event_in_tournament):
      return self.tournament_ll.get_tournament_schedule(tournament_name, event_in_tournament)
   
   def assign_point(self):
      pass
   
   def get_statistics(self, ptc: str): #PTC = Player Team Club
      pass

   #EVENT METHODS

   def create_empty_event(self, event: Event):
      return self.event_ll.create_empty_event(event)

   def get_team_captain(self, team_name, handle):
      return self.captain_ll.get_team_captain(team_name, handle)
   
   def event_types(self):
      return self.event_ll.event_types()


