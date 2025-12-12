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
        
        if self.write_event_into_tournament(event):

            return self._dl_wrapper.create_empty_event(event)

    # ----------------------------------------------------------------------
    # EVENT TYPES 
    # ----------------------------------------------------------------------

    def event_types(self):
        """RETURNS LIST OF POSSIBLE EVENT TYPES"""
    
        return [
            "Single Elimination",
            "Last Team Standing"
            ] 
    


    # def find_next_useable_id(self):
    #     """checks the next id that has no team associated with it"""
    #     event_file = self._dl_wrapper.load_event_blueprint()
    #     for line in event_file:
    #         line:  = 
    #         useable_id = int(line.id
    #         if line. == "team":
    #             return useable_id
    


# laga þetta
    # def create_empty_event(self, event: Event):
    #     self._dl_wrapper.write_into_event_blueprint('id,team_name,event_name,event_type,tournment_name,start_date,end_date')

    #     for id in range(1,17):
    #         self._dl_wrapper.write_into_event_blueprint(f'{id},"team",{event.name},{event.game_type},{event.tournament_name},{event.start_date},{event.end_date}\n')
    #     return "Event created!"
    
# #############################################

    # ----------------------------------------------------------------------
    # WRITE EVENT INTO TOURNAMENT
    # ----------------------------------------------------------------------

    def write_event_into_tournament(self, event: Event):
        """ADDS EVENT TO ITS TOURNAMENT'S EVENT LIST"""
    
        tournament_file: list[Tournament] = self._dl_wrapper.read_tournament_file()
    
        for tournament in tournament_file:
            if tournament.tournament_name == event.tournament_name:
                tournament.event_list.append(event.event_name)
    
        return True

    # ----------------------------------------------------------------------
    # CHECK IF TEAM IN EVENT
    # ----------------------------------------------------------------------

    def check_if_team_in_event(self, team):
        """CHECKS IF A TEAM IS ALREADY IN THE EVENT"""
    
        event_data = self._dl_wrapper.load_all_player_info()

        for line in event_data:
            if line.team_name == team:
                return True
    
        return False

    
    # ----------------------------------------------------------------------
    # MAKE EVENT PUBLIC
    # ----------------------------------------------------------------------

    def make_event_public(self):
        """MOVES EVENT DATA TO PUBLIC FILE OR KNOCKOUT"""
    
        blueprint_file = self._dl_wrapper.load_event_blueprint()
    
        for line in blueprint_file:
            if line["id"] == 1:
                type_of_event = line["event_type"]
    
        if type_of_event == "knockout":
            return self.move_blueprint_to_knockout()
    
        if type_of_event == "last_team_standing":
            return self._dl_wrapper.edit_match_file()
 
    # ----------------------------------------------------------------------
    # MOVE BLUEPRINT TO KNOCKOUT
    # ----------------------------------------------------------------------
 
    def move_blueprint_to_knockout(self):
        """CREATES KNOCKOUT STRUCTURE FROM EVENT BLUEPRINT"""
    
        knockout_file = self._dl_wrapper.move_to_knockout("tournament,event_name,game_type,server_id,match_id,bracket_nr,date_of_match,time_of_match,team_a,team_b,team_a_score,team_b_score,winner,match_result")
    
        self.create_first_round()
    
        return "Done!"
    
    # ----------------------------------------------------------------------
    # GET SERVER ID
    # ----------------------------------------------------------------------
 
    def get_server_id(self):
        """GENERATES A UNIQUE SERVER ID"""
    
        return str(uuid.uuid4())

        


    

    # def get_match_id(self):
    #     schedule_file = self.read_schedule_file_as_list_of_dict()
    #     last_id = int(schedule_file[-1]["match_id"])
    #     return last_id + 1

    # ----------------------------------------------------------------------
    # INPUT MATCH RESULTS
    # ----------------------------------------------------------------------
 
    def input_match_results(self, match_id, team_a_score, team_b_score, match: Match):
        """UPDATES MATCH SCORES AND DETERMINES WINNER"""
    
        schedule_file: list(Match) = self._dl_wrapper.load_match_file()
    
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
    
        return f"Winner for match{match_id} is {match.winner}"
    
    # ----------------------------------------------------------------------
    # CREATE FIRST ROUND
    # ----------------------------------------------------------------------
  
    def create_first_rounds(self, event: Event, match: Match):
        """CREATES FIRST ROUND MATCHUPS FOR TEAMS"""
    
        public_file: list[Team] = self._dl_wrapper.view_all_teams()
    
        all_team_list = []
    
        for team in public_file:
            all_team_list.append(team.name)
    
        for teamsvs in all_team_list:
            team_a = random.choice(teamsvs)
            all_team_list.remove(team_a)
            team_b = random.choice(teamsvs)
            all_team_list.remove(team_b)
            server_id = self.get_server_id()
            bracket_id = self.get_bracket_id()
            ###############################Hvar eigum við að geyma server id??????? ég geri bara í match örsnöggt
            self._dl_wrapper.append_to_match_file(f'{match.tournament_name},{match.event_name},{match.game_type},{match.match_id}{server_id},{bracket_id},{match.date_of_match}{match.time_of_match},{team_a},{team_b},team_a_score,team_b_score,winner,')
            

    # ----------------------------------------------------------------------
    # GET BRACKET ID
    # ----------------------------------------------------------------------
 
    def get_bracket_id(self, current_bracket):
        """DETERMINES NEXT BRACKET NUMBER"""
    
        public_file: list[Match] = self._dl_wrapper.load_match_file()
    
        if not isinstance(public_file[-1].bracket_nr):
            return 1
        else:
            new_bracket_nr = public_file[-1].bracket_nr +1
            return new_bracket_nr



    # ----------------------------------------------------------------------
    # CREATE ROUND 2, 3, AND 4
    # ----------------------------------------------------------------------
  
    def create_round_2_3_and_4(self, round: int, match: Event):
        """CREATES SUBSEQUENT ROUNDS BASED ON PREVIOUS WINNERS"""  
        
        schedule_file = self._dl_wrapper.load_match_file()
        
        list_of_winners_from_bracket = []
        
        for line in schedule_file[round:]:
            list_of_winners_from_bracket.append(line["winner"])
        
        for team in list_of_winners_from_bracket:
            team_a = list_of_winners_from_bracket[0]
            list_of_winners_from_bracket.pop(0)
            team_b = list_of_winners_from_bracket[0]
            list_of_winners_from_bracket.pop(0)
            server_id = self.get_server_id
            self._dl_wrapper.move_to_knockout(f'{event.tournament_name},{event.name},{event.game_type},{server_id},{int(get_bracket_nr)},{date_of_match}{event.schedule_time},{team_a},{team_b},team_a_score,team_b_score,winner,')
        
        return "Round created"
            
    # ----------------------------------------------------------------------
    # CREATE SECOND ROUND
    # ----------------------------------------------------------------------
   
    def create_second_round(self):
        """CREATES SECOND ROUND MATCHUPS"""
        
        round = int(0)
        
        second_round = self.create_round_2_3_and_4(round)
        
        return "Round created"

    # ----------------------------------------------------------------------
    # CREATE THIRD ROUND
    # ----------------------------------------------------------------------
    
    def create_third_round(self):
        """CREATES THIRD ROUND MATCHUPS"""
        
        round = int(9)
        
        third_round = self.create_round_2_3_and_4(round)
        
        return "Round created"
    
    # ----------------------------------------------------------------------
    # CREATE FOURTH ROUND
    # ----------------------------------------------------------------------
    
    def create_fourth_round(self):
        """CREATES FOURTH ROUND MATCHUPS"""
        
        round = int(13)
        
        fourth_round = self.create_round_2_3_and_4(round)
        
        return "Round created"

    # ----------------------------------------------------------------------
    # DECLARE WINNER
    # ----------------------------------------------------------------------
  
    def declare_winner(self):
        """RETURNS THE FINAL WINNER OF THE EVENT"""
        
        knockout_file = self._dl_wrapper.load_match_file()
        
        for line in knockout_file[15:]:
            winner = line["winner"] if line["winner"] else "No final winner yet"
        
        return winner

    # ----------------------------------------------------------------------
    # HOW MANY MATCHES HAVE WINNERS
    # ----------------------------------------------------------------------
    
    def how_many_matches_have_winners(self):
        """COUNTS MATCHES THAT HAVE A WINNER"""
        
        schedule_file = self._dl_wrapper.load_match_file
        
        winners = 0
        
        for line in schedule_file:
            if line["winner"] != "winner":
                winners +=1
        
        return winners
    
    # ----------------------------------------------------------------------
    # VIEW UNFINISHED GAMES
    # ----------------------------------------------------------------------
    
    def view_unfinnised_games(self):
        """RETURNS ALL UNFINISHED MATCHES"""  
        pass
    
    # ----------------------------------------------------------------------
    # VIEW FINISHED GAMES
    # ----------------------------------------------------------------------
  
    def view_finnished_games(self):
        """RETURNS ALL FINISHED MATCHES"""
        
        return self._dl_wrapper.read_results_file()

    # ----------------------------------------------------------------------
    # GET RESULTS FROM ONE GAME
    # ----------------------------------------------------------------------
   
    def get_results_from_one_game(self):
        """RETRIEVES RESULTS FOR A SINGLE GAME"""

        result_from_one_game = self._dl_wrapper.read_results_file()
        
        return result_from_one_game
        
