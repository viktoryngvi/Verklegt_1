import uuid
from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.event import Event
from models.team import Team
from datetime import datetime
import random


class EventLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper
        self.validate = Validate(dl_wrapper)
    

    # ----------------------------------------------------------------------
    # CREATE EVENT
    # ----------------------------------------------------------------------



    def create_empty_event(self, event : Event):
        validate_errors = self.validate.validate_event(event)

        if validate_errors:
            return validate_errors
        
        return self._dl_wrapper.create_empty_event(event)



    # ----------------------------------------------------------------------
    # EVENT TYPES 
    # ----------------------------------------------------------------------

    def event_types(self):
        return [
            "Single Elimination",
            "Last Team Standing"
            ] 
    


    def find_next_useable_id(self):
        """checks the next id that has no team associated with it"""
        event_file = self._dl_wrapper.read_public_file_as_list_of_dict()
        for line in event_file:
            useable_id = int(line["id"])
            if line["team_name"] == "team":
                return useable_id
    
    def get_server_id(self):
        return str(uuid.uuid4())


# laga þetta
    # def create_empty_event(self, event: Event):
    #     self._dl_wrapper.write_into_event_blueprint('id,team_name,event_name,event_type,tournment_name,start_date,end_date')

    #     for id in range(1,17):
    #         self._dl_wrapper.write_into_event_blueprint(f'{id},"team",{event.name},{event.game_type},{event.tournament_name},{event.start_date},{event.end_date}\n')
    #     return "Event created!"
    
# #############################################
    def write_team_into_empty_event(self, event: Event, team):
        """takes a team name and writes it into the blueprint"""
        event_data = self._dl_wrapper.read_public_file_as_list_of_dict()        
        next_id = self.find_next_useable_id()
        for line in event_data:
            if line["id"] == next_id:
                line["team_name"] = f"{team},"

        self._dl_wrapper.write_into_event_blueprint(event_data)
        return f"{team} is now a part of this event!"

    def check_if_team_in_event(self, team):
        """takes team name and checks if the team is in the event"""
        event_data = self._dl_wrapper.read_public_file_as_list_of_dict()
        for line in event_data:
            if line["team_name"] == team:
                return True
        return False
            
    def make_event_public(self):
        blueprint_file = self._dl_wrapper.read_public_file_as_list_of_dict()
        for line in blueprint_file:
            if line["id"] == 1:
                type_of_event = line["event_type"]
        if type_of_event == "knockout":
            return self.move_blueprint_to_knockout()
        if type_of_event == "last_team_standing":
            return self.move_blueprint_to_last_team_standing()

    def move_blueprint_to_knockout(self):
        knockout_file = self._dl_wrapper.move_to_knockout("tournament,event_name,game_type,server_id,bracket_nr,date_of_match,time_of_match,team_a,team_b,team_a_score,team_b_score,winner,match_result")
        self.create_first_round()
        return "Done!"
        

    def move_blueprint_to_last_team_standing(self, event: Event):
        blueprint = self._dl_wrapper.read_public_file_as_list_of_dict
        
        list_of_teams = []
        server_id = self.get_server_id()
        for teams in blueprint:
            list_of_teams.append(teams["team_name"])
        self._dl_wrapper.move_to_last_team_standing("game_name,game_type,server_id,time_of_match,winner,teams_list")
        self._dl_wrapper.move_to_last_team_standing(f"{event.name},{event.game_type},{server_id},{event.time_of_match},winner,{list_of_teams},")

        return "Event is now public"
    
    def input_last_team_standing_result(self, team_that_won, event: Event):
        last_team_file = self._dl_wrapper.read_last_team_standing_as_list_of_dict()
        
        for line in last_team_file:
            # if int(line["match_id"]) == 1:  #TODO
                line["winner"] = team_that_won

        self._dl_wrapper.move_to_last_team_standing(last_team_file)
        return f"{team_that_won}, is the winner of {event.name}"
        # hvað er time of match??????????????????????????????????????#TODO

    # def check_if_last_team_has_winner(self):
    #     with open(self.Last_team_file, "r", encoding="utf-8") as read_last_team_file:
    #         read_last_team_file = list(DictReader(read_last_team_file))
    #     for line in read_last_team_file:
    #         if int(line["match_id"]) == 1:
    #             if line["winner"] != "winner":
    #                 final_string = f"Game winner is {line['winner']}"
    #                 return final_string
    #     return "Game is not finnished"
    

    # def get_match_id(self):
    #     schedule_file = self.read_schedule_file_as_list_of_dict()
    #     last_id = int(schedule_file[-1]["match_id"])
    #     return last_id + 1

    def input_match_results(self, match_id, team_a_score, team_b_score):
        schedule_file = self._dl_wrapper.read_knockout_as_list_of_dict()
        for line in schedule_file:
            if line["match_id"] == match_id:
                line["team_a_score"] = team_a_score
                line["team_b_score"] = team_b_score
                if team_a_score == team_b_score:
                    line["winner"] = "Tie!"
                if team_a_score > team_b_score:
                    line["winner"] = line["team_a"]
                if team_a_score < team_b_score:
                    line["winner"] = line["team_b"]
                break
        return f"Winner for match{match_id} is {line['winner']}"
    

    def create_first_round(self, event: Event):
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
            self._dl_wrapper.move_to_knockout(f'{event.tournament_name},{event.name},{event.game_type},{server_id},{int(get_bracket_nr)},{date_of_match}{event.schedule_time},{team_a},{team_b},team_a_score,team_b_score,winner,')
            
        # þarf schedule time name #TODO


    def create_round_2_3_and_4(self, round: int, event: Event):
        schedule_file = self._dl_wrapper.read_knockout_as_list_of_dict()
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
            
    def create_second_round(self):
        round = int(0)
        second_round = self.create_round_2_3_and_4(round)
        return "Round created"

    def create_third_round(self):
        round = int(9)
        third_round = self.create_round_2_3_and_4(round)
        return "Round created"
    
    def create_fourth_round(self):
        round = int(13)
        fourth_round = self.create_round_2_3_and_4(round)
        return "Round created"

    def declare_winner(self):
        knockout_file = self._dl_wrapper.read_knockout_as_list_of_dict()
        for line in knockout_file[15:]:
            winner = line["winner"] if line["winner"] else "No final winner yet"
        return winner

    def how_many_matches_have_winners(self):
        schedule_file = self._dl_wrapper.read_knockout_as_list_of_dict()
        winners = 0
        for line in schedule_file:
            if line["winner"] != "winner":
                winners +=1
        return winners
    
    def view_unfinnised_games(self):
        pass
    # 

    def view_finnished_games(self):
        pass

    def get_results_from_one_game():
        pass
