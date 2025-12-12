import uuid
from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.event import Event
from models.match import Match
from models.team import Team
from models.tournament import Tournament
from datetime import datetime
import random



class EventLL:
    """HANDLES EVENT OPERATIONS: CREATE EVENTS, MANAGE MATCHES, DECLARE WINNERS"""

    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper
        self.validate = Validate(dl_wrapper)
    
    # ----------------------------------------------------------------------
    # CREATE EVENT
    # ----------------------------------------------------------------------

    def create_empty_event(self, event: Event):
        """CREATES AN EMPTY EVENT AND SAVES IT"""
    
        validate_errors = self.validate.validate_event(event)

        if validate_errors:
            return validate_errors
    
        
        self.write_event_into_tournament(event)

        return self._dl_wrapper.create_empty_event_blueprint(event)

    # ----------------------------------------------------------------------
    # EVENT TYPES 
    # ----------------------------------------------------------------------

    def event_types(self):
        """RETURNS LIST OF POSSIBLE EVENT TYPES"""
    
        return [
            "Single Elimination",
            "Last Team Standing"
            ] 
    


    def append_team_into_blue_print(self, team):
        event_list_blue: list[Event] = self._dl_wrapper.load_event_blueprint()

        for event in event_list_blue:
            if event.team_name == "None":
                event.team_name = team
                break

        return self._dl_wrapper.append_team_into_blueprint(event_list_blue)
        
    

    # ----------------------------------------------------------------------
    # WRITE EVENT INTO TOURNAMENT
    # ----------------------------------------------------------------------

    def write_event_into_tournament(self, event: Event):
        """ADDS EVENT TO ITS TOURNAMENT'S EVENT LIST"""
    
        tournament_file: list[Tournament] = self._dl_wrapper.read_tournament_file()
    
        for tournament in tournament_file:
            if tournament.tournament_name == event.tournament_name:
                tournament.event_list.append(event.event_name)

        return self._dl_wrapper.edit_tournament_file(tournament_file)

    # ----------------------------------------------------------------------
    # CHECK IF TEAM IN EVENT
    # ----------------------------------------------------------------------

    def check_if_team_in_event(self, team):
        """CHECKS IF A TEAM IS ALREADY IN THE EVENT"""
    
        event_data: list[Event] = self._dl_wrapper.load_event_blueprint()

        for line in event_data:
            if line.team_name == team:
                return True
    
        return False

    
    # # ----------------------------------------------------------------------
    # # MAKE EVENT PUBLIC
    # # ----------------------------------------------------------------------

    def move_from_blueprint_to_match(self):
        """MOVES EVENT DATA TO PUBLIC FILE OR KNOCKOUT"""
    
        blueprint_file: list[Match] = self._dl_wrapper.load_event_blueprint()
    
        for line in blueprint_file:
            if line.event_id == 1:
                type_of_event = line.game_type
    
        if type_of_event == "knockout":
            return self.move_blueprint_to_match_file()
    
        if type_of_event == "last_team_standing":
            return self._dl_wrapper.edit_match_file()
 
    # ----------------------------------------------------------------------
    # MOVE BLUEPRINT TO Match
    # ----------------------------------------------------------------------
 
    def move_blueprint_to_match_file(self):
        """CREATES Match STRUCTURE FROM EVENT BLUEPRINT"""
        list_events:list[Event] = self._dl_wrapper.load_event_blueprint()

        if list_events[-1].team_name == "None":
            return "Not enough teams registered"
        
        self._dl_wrapper.override_match_file()
        self.create_first_rounds()
    
        return "Done!"
    
    # ----------------------------------------------------------------------
    # GET SERVER ID
    # ----------------------------------------------------------------------
 
    def get_server_id(self):
        """GENERATES A UNIQUE SERVER ID"""
    
        return str(uuid.uuid4())
    

    def get_match_id(self):
        schedule_file: list[Match] = self._dl_wrapper.load_match_file()
        last_id = int(schedule_file[-1].match_id)
        return last_id + 1
    
    def get_bracket_id(self):
        """DETERMINES NEXT BRACKET NUMBER"""
    
        match_file: list[Match] = self._dl_wrapper.load_match_file()
    
        if not match_file[-1].bracket_nr:
            return 1
        else:
            new_bracket_nr = match_file[-1].bracket_nr + 1
            return new_bracket_nr
        
    def get_date_of_match(self):
        # first day, 
        pass

    def get_time_of_match(self):
        pass

    # ----------------------------------------------------------------------
    # INPUT MATCH RESULTS
    # ----------------------------------------------------------------------
 
    def input_match_results(self, match_id, team_a_score, team_b_score):
        """UPDATES MATCH SCORES AND DETERMINES WINNER"""
    
        schedule_file: list[Match] = self._dl_wrapper.load_match_file()
    
        for match in schedule_file:
    
            if match.match_id == match_id:
                match.team_a_score = team_a_score
                match.team_b_score = team_b_score

                if team_a_score == team_b_score:
                    match.winner = "Tie!"
    
                if team_a_score > team_b_score:
                    match.winner = match.team_a
    
                if team_a_score < team_b_score:
                    match.winner = match.team_b
                break
        self._dl_wrapper.edit_match_file(schedule_file)
        return f"Winner for match{match_id} is {match.winner}"
    
    # ----------------------------------------------------------------------
    # CREATE FIRST ROUND
    # ----------------------------------------------------------------------
  
    def create_first_rounds(self):
        """CREATES FIRST ROUND MATCHUPS FOR TEAMS"""
        public_file: list[Event] = self._dl_wrapper.load_event_blueprint()

        # the_event = public_file[0]
        all_team_list = []
        for line in public_file:
            all_team_list.append(line.team_name)
        random.shuffle(all_team_list)

        bracket_id = 1
        #for lööp sem býr til lista af tuples (team_a, team_b)
        for i in range(0, 16, 2):
            team_a = all_team_list[i]
            team_b = all_team_list[i+1]
            for teamsvs in all_team_list: # iterates tuple teams list
                the_event = public_file[1]
                server_id = self.get_server_id()
                match_id = self.get_match_id()
                date_of_match = self.get_date_of_match()
                time_of_match = self.get_time_of_match()
                match: Match = Match(
                    tournament_name=the_event.tournament_name,
                    event_name=the_event.event_name,
                    game_type=the_event.event_type,
                    team_a=team_a,
                    team_b=team_b,
                    server_id=server_id,
                    match_id=match_id,
                    bracket_nr=bracket_id,
                    date_of_match=date_of_match,
                    time_of_match=time_of_match,
                    teams= all_team_list,
                    team_a_score=None,
                    team_b_score=None,
                    winner=None,
                    )
                self._dl_wrapper.append_to_match_file(match)                

    # ----------------------------------------------------------------------
    # CREATE ROUND 2, 3, AND 4
    # ----------------------------------------------------------------------
  
    def create_round_2_3_and_4(self, round_nr: int):
        """CREATES SUBSEQUENT ROUNDS BASED ON PREVIOUS WINNERS"""  
        
        schedule_file: list[Match] = self._dl_wrapper.load_match_file()
        list_of_winners_from_bracket = []
        
        for match in schedule_file[round_nr:]:
            list_of_winners_from_bracket.append(match.winner)

        match.bracket_nr = self.get_bracket_id()

        for i in range(0, len(list_of_winners_from_bracket), 2):
            team_a_new = list_of_winners_from_bracket[i]
            team_b_new = list_of_winners_from_bracket[i+1]

            match.date_of_match = self.get_date_of_match()
            match.time_of_match = self.get_time_of_match()
            match.team_a = team_a_new
            match.team_b = team_b_new
            match.server_id = self.get_server_id()
            self._dl_wrapper.append_to_match_file(match)
        
        return "Round created"
            
    # ----------------------------------------------------------------------
    # CREATE SECOND ROUND
    # ----------------------------------------------------------------------
   
    def create_second_round(self):
        """CREATES SECOND ROUND MATCHUPS"""
        
        round_nr = int(0)
        self.create_round_2_3_and_4(round_nr)
        
        return "Round created"

    # ----------------------------------------------------------------------
    # CREATE THIRD ROUND
    # ----------------------------------------------------------------------
    
    def create_third_round(self):
        """CREATES THIRD ROUND MATCHUPS"""
        
        round_nr = int(9)
        
        self.create_round_2_3_and_4(round_nr)
        
        return "Round created"
    
    # ----------------------------------------------------------------------
    # CREATE FOURTH ROUND
    # ----------------------------------------------------------------------
    
    def create_fourth_round(self):
        """CREATES FOURTH ROUND MATCHUPS"""
        
        round_nr = int(13)
        
        self.create_round_2_3_and_4(round_nr)
        
        return "Round created"

    #######################################################################


    def move_blueprint_to_last_team_standing(self):
        blueprint: list[Event] = self._dl_wrapper.load_event_blueprint()
        
        list_of_teams = []
        server_id = self.get_server_id()
        for teams in blueprint:
            list_of_teams.append(teams.team_name)
        the_event = blueprint[1]

        server_id = self.get_server_id()
        match_id = self.get_match_id()
        date_of_match = self.get_date_of_match()
        time_of_match = self.get_time_of_match()            
        match: Match = Match(
            tournament_name=the_event.tournament_name,
            event_name=the_event.event_name,
            game_type=the_event.event_type,
            team_a=None,
            team_b=None,
            server_id=server_id,
            match_id=match_id,
            bracket_nr=None,
            date_of_match=date_of_match,
            time_of_match=time_of_match,
            teams= list_of_teams,
            team_a_score=None,
            team_b_score=None,
            winner=None,
            )

        self._dl_wrapper.append_to_match_file()

        return "Event is now public"

    # ----------------------------------------------------------------------
    # DECLARE WINNER
    # ----------------------------------------------------------------------
  
    def find_winner(self):
        """RETURNS THE FINAL WINNER OF THE EVENT"""
        
        knockout_file: list[Match] = self._dl_wrapper.load_match_file()
        
        winner = knockout_file[-1].winner        
        return winner



    def move_match_to_result(self):
        matches_to_append: list[Match] = self._dl_wrapper.load_match_file()
        return self._dl_wrapper.append_into_results(matches_to_append)



    # ----------------------------------------------------------------------
    # HOW MANY MATCHES HAVE WINNERS
    # ----------------------------------------------------------------------
    
    def how_many_matches_have_winners(self):
        """COUNTS MATCHES THAT HAVE A WINNER"""
        
        match_file: list[Match] = self._dl_wrapper.load_match_file()
        
        winners = 0
        
        for line in match_file:
            if line.winner != "winner":
                winners +=1
        
        return winners
    
    # ----------------------------------------------------------------------
    # VIEW GAMES
    # ----------------------------------------------------------------------
    
    def view_games(self, tournament, event_nam):
        """RETURNS ALL MATCHES """  
        result_file: list[Match] = self._dl_wrapper.read_results_file()
        results_list = []
        for line in result_file:
            if line.tournament_name == tournament:
                if line.event_name == event_nam:
                    results_list.append(line)
        if results_list:
            return results_list
        
        match_file: list[Match] = self._dl_wrapper.load_match_file()
        unfinnished_games = []
        if match_file[1].tournament_name == tournament:
            if match_file[1].event_name == event_nam:
                for match in match_file:
                    if match.winner is None:
                        unfinnished_games.append(match)
                return unfinnished_games
    
