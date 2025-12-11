from IO.Player_IO import Player_IO
from IO.Teams_IO import Team_IO
from IO.Event_IO import Event_IO
from IO.Tournament_IO import Tournament_IO
from IO.Club_IO import Club_IO
from models.event_blueprint import Event_blueprint
from models.match import Match

class DLWrapper:
    def __init__(self):
        self.playerio = Player_IO()
        self.teamio = Team_IO()
        self.event_blueprintio = Event_IO()
        self.tournamentio = Tournament_IO()
        self.clubio = Club_IO()
        self.match = Match()
        self.event_blueprint = Event_blueprint()

    # Player methods

    def load_all_player_info(self):
        return self.playerio.load_all_player_info()

    def create_player(self, player_data :Player_IO):
        """takes all player info and appends that into the player file"""
        return self.playerio.create_player(player_data)
    
    def edit_player_file(self, player_data):
        return self.playerio.edit_player_file(player_data)
    # team methods

    def view_all_teams(self):
        """returns a list of dictionarys of all teams"""
        return self.teamio.view_all_teams()
    
    def append_team_into_file(self, team):
        return self.teamio.append_team_into_file(team)
    
    def write_team_into_file(self, teams_file):
        return self.teamio.write_team_into_file(teams_file)
    # er ekki tengt!!!!!!!!!!!!!!!!

    
    
    # tournament methods

    def read_tournament_file(self):
        return self.tournamentio.read_tournament_file()
    
    def write_into_file(self, tournament_data):
        return self.tournamentio.write_into_file(tournament_data)



   # Event methods:

    def create_empty_event(self, event_blueprint: Event_blueprint):
        return self.event_blueprintio.create_empty_event(event_blueprint)

    def load_event_blueprint(self):
        return self.event_blueprintio.load_event_blueprint()
    
    def append_team_into_blueprint(self, team_data: Event_blueprint):
        return self.event_blueprintio.append_team_into_blueprint(team_data)
    
    def load_match_file(self):
        return self.event_blueprintio.load_match_file()
    
    def append_to_match_file(self, match: Match):
        return self.event_blueprintio.append_to_match_file(match)
    
    def edit_match_file(self, matches: list[Match]):
        return self.event_blueprintio.edit_match_file(matches)
    
    def read_results_file(self):
        return self.event_blueprintio.read_results_file()
    
    def append_into_results(self, matches_to_append: list[Match]):
        return self.event_blueprintio.append_into_results(matches_to_append)

    

"""    # club methods:

    def register_club(self, club: Club):
        with open(self.file_path, "a", encoding="utf-8") as club_file:
            club_file.write(
                f"{self.add_club_id()},"
                f"{club.name},"
                f"{club.home_town},"
                f"{club.country},"
                f"{','.join(club.colors) if club.color else ''},"
                f"{','.join(club.teams) if club.teams else ''}\n"
            )
    
    def add_team_to_club(self, club_name, team_name):
        return self.clubio.add_team_to_club(club_name, team_name)
    
    def view_clubs(self):
        club_file = self.read_club_file_as_list_of_dict()
        club_list = []
        for line in club_file:
            club = Club(
                name=line["club_name"],
                home_town=line["Club_home_town"],
                country=line["club_country"],
                colors=line["club_colors"].split(","),    
                teams=line["teams"].split(",") if line["teams"] else []
            )
            club_list.append(club)
        return club_list
    
    def view_club_information(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                 club = Club(
                     name=line["club_name"],
                     home_town=line["Club_home_town"],
                     country=line["club_country"],
                     colors=line["club_colors"].split(","),    
                     teams=line["teams"].split(",") if line["teams"] else []
                 )
                 return club
            return None
    def check_if_club_name_in_use(self, club_name):
        return self.clubio.check_if_club_name_in_use(club_name)
    
"""