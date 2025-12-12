from models.match import Match
from models.event import Event
from datetime import date

class Event_IO(Match, Event):
    """HANDLES READING, WRITING AND UPDATING EVENT, MATCH AND RESULT FILES"""

    def __init__(self):
        self.blueprint_file = "data/event_blueprint.csv"
        self.match_file = "data/match.csv"
        self.public_event_file = "data/puclic_event.csv"
        self.results_file = "data/results.csv"

    # ----------------------------------------------------------------------
    # CEATE EMPTY EVENT 
    # ----------------------------------------------------------------------

    def create_empty_event_blueprint(self, event: Event):
        """CREATES A NEW EMPTY EVENT BLUEPRINT AND SAVES IT TO FILE"""


        with open(self.blueprint_file, "w", encoding="utf-8") as blueprint_file:
            blueprint_file.write("event_name,event_type,tournment_name,start_date,end_date,team_name,id\n")

            for line in range(16):
                blueprint_file.write(
                    f'{event.event_name},'
                    f'{event.event_type},'
                    f'{event.tournament_name},'
                    f'{date.isoformat(event.start_date)},'
                    f'{date.isoformat(event.end_date)},'
                    f'{event.team_name},'
                    f'{event.event_id},'
                    f'\n'
                    )
                
        return "Empty event created"
    
    # ----------------------------------------------------------------------
    # LOAD EVENT BLUE PRINT
    # ----------------------------------------------------------------------

    def load_event_blueprint(self):
        """LOADS ALL EVENT BLUEPRINT INFORMATION FROM CSV FILE"""

        event_list = []
        
        with open(self.blueprint_file, "r", encoding="utf-8") as blueprint_file:
        
            headers = blueprint_file.readline().split(",")
        
            for row in blueprint_file:
                attributes = row.split(",")
                event = Event()
                event.event_name = str(attributes[0])
                event.event_type = str(attributes[1])
                event.tournament_name = str(attributes[2])
                event.start_date = date.fromisoformat(attributes[3])
                event.end_date = date.fromisoformat(attributes[4])
                event.team_name = str(attributes[5])
                event.event_id = int(attributes[6])
                event_list.append(event)
        
        return event_list
    
    # ----------------------------------------------------------------------
    # APPEND TEAM INTO BLUEPRINT
    # ----------------------------------------------------------------------

    def append_team_into_blueprint(self, team_data: list[Event]):
        """APPENDS A TEAM INTO THE EXISTING EVENT BLUEPRINT FILE"""
        
        with open(self.blueprint_file, "w", encoding="utf-8") as blueprint_file:
    
            blueprint_file.write("event_name,event_type,tournment_name,start_date,end_date,team_name,id")
    
            for teams in team_data:
                blueprint_file.write(
                f'{teams.event_type},'
                f'{teams.tournament_name},'
                f'{date.isoformat(teams.start_date)},'
                f'{date.isoformat(teams.end_date)},'
                f'{teams.team_name},'
                f'{teams.event_id},'
                f'\n'
                )
        return "Match has been added to file"


    # ----------------------------------------------------------------------
    # LOAD MATCH FILE
    # ----------------------------------------------------------------------

    def load_match_file(self):
        """LOADS ALL MATCHES FROM MATCH CSV FILE"""

    
        knockout_list = []
    
        with open(self.match_file, "r", encoding="utf-8") as match_file:
    
            headers = match_file.readline().split(",")
    
            for row in match_file:
                attributes = row.split(",")
                match = Match
                match.tournament_name = str(attributes[0])
                match.event_name = str(attributes[1])
                match.game_type = str(attributes[2])
                match.server_id = str(attributes[3])
                match.match_id = int(attributes[4])
                match.bracket_nr = int(attributes[5])
                match.date_of_match = date.isoformat(attributes[6])
                match.time_of_match = str(attributes[7])
                match.teams = list(attributes[8].split(";"))
                match.team_a = str(attributes[9])
                match.team_b = int(attributes[10])
                match.team_a_score = str(attributes[11])
                match.team_b_score = str(attributes[12])
                match.winner = str(attributes[13])
                knockout_list.append(match)
    
        return knockout_list
    
    # ----------------------------------------------------------------------
    # APPEND MATH FILE
    # ----------------------------------------------------------------------

    def append_to_match_file(self, match: Match):
        """APPENDS A NEW MATCH ENTRY INTO THE MATCH FILE"""

        with open(self.match_file, "a", encoding="utf-8") as match_file:
            teams_str = ";".join(str(t) for t in match.teams)
            match_file.write(
                    f'{match.tournament_name},'
                    f'{match.event_name},'
                    f'{match.game_type},'
                    f'{match.server_id},'
                    f'{match.match_id},'
                    f'{match.bracket_nr},'
                    f'{date.isoformat(match.date_of_match)},'
                    f'{match.time_of_match},'
                    f'{teams_str},'
                    f'{match.team_a},'
                    f'{match.team_b},'
                    f'{match.team_a_score},'
                    f'{match.team_b_score},'
                    f'{match.winner},'
                    f'\n'
                )
    
        return "Match has been added to file"
    
    # ----------------------------------------------------------------------
    # EDIT MATCH FILE
    # ----------------------------------------------------------------------

    def override_match_file(self):
        with open(self.match_file, "w", encoding="utf-8") as match_file:
            match_file.write("tournament,event_name,game_type,server_id,match_id,date_of_match,time_of_match,teams,team_a,team_b,team_a_score,team_b_score,winner\n")
        return True


    def edit_match_file(self, matches: list[Match]):
        """OVERWRITES MATCH FILE WITH UPDATED MATCH INFORMATION"""
    
        with open(self.match_file, "w", encoding="utf-8") as match_file:
            match_file.write("tournament,event_name,game_type,server_id,match_id,date_of_match,time_of_match,teams,team_a,team_b,team_a_score,team_b_score,winner\n")


            for match in matches:
                teams_str = ";".join(str(t) for t in match.teams)
                match_file.write(
                    f'{match.tournament_name},'
                    f'{match.event_name},'
                    f'{match.game_type},'
                    f'{match.server_id},'
                    f'{match.match_id},'
                    f'{match.bracket_nr},'
                    f'{date.isoformat(match.date_of_match)},'
                    f'{match.time_of_match},'
                    f'{teams_str},'
                    f'{match.team_a},'
                    f'{match.team_b},'
                    f'{match.team_a_score},'
                    f'{match.team_b_score},'
                    f'{match.winner},'
                    f'\n'
                )
    
        return "Match has been edited"
    
    # ----------------------------------------------------------------------
    # READ RESULT FILE 
    # ----------------------------------------------------------------------

    def read_results_file(self):
        """READS ALL FINISHED MATCH RESULTS FROM RESULTS FILE"""

    
        results_list = []
    
        with open(self.results_file, "r", encoding="utf-8") as results_file:
    
            headers = results_file.readline().split(",")
    
            for row in results_file:
                attributes = row.split(",")
                match = Match
                match.tournament_name = str(attributes[0])
                match.event_name = str(attributes[1])
                match.game_type = str(attributes[2])
                match.server_id = str(attributes[3])
                match.match_id = int(attributes[4])
                match.bracket_nr = int(attributes[5])
                match.date_of_match = date.fromisoformat(attributes[6])
                match.time_of_match = str(attributes[7])
                match.teams = list(attributes[8].split(";"))
                match.team_a = str(attributes[9])
                match.team_b = int(attributes[10])
                match.team_a_score = str(attributes[11])
                match.team_b_score = str(attributes[12])
                match.winner = str(attributes[13])
                results_list.append(match)
    
        return results_list
            
    # ----------------------------------------------------------------------
    # APPEND INTO RESULTS
    # ----------------------------------------------------------------------

    def append_into_results(self, matches_to_append: list[Match]):
        """APPENDS NEW RESULTS INTO THE RESULTS FILE"""

    
        with open(self.match_file, "a", encoding="utf-8") as results_file:
    
            for match in matches_to_append:
                teams_str = ";".join(str(t) for t in match.teams)
    
                results_file.write(
                        f'{match.tournament_name},'
                        f'{match.event_name},'
                        f'{match.game_type},'
                        f'{match.server_id},'
                        f'{match.match_id},'
                        f'{match.bracket_nr},'
                        f'{match.date_of_match},'
                        f'{match.time_of_match},'
                        f'{teams_str},'
                        f'{match.team_a},'
                        f'{match.team_b},'
                        f'{match.team_a_score},'
                        f'{match.team_b_score},'
                        f'{match.winner},'
                        f'\n'
                    )
    
            return "Match has been added to file"

            # það þarf ekki að vera edit results function af því við
            # erum aldrei að breyta leikjum sem eru liðnir

