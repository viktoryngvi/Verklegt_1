import random
from csv import DictReader
from models.match import Match

class Knockout_Schedule(Match):
    def __init__(self):
        self.get_event_file = "data/event_blueprint.csv"
        self.file_path = "data/schedule.csv"
        self.public_file_path = "data/public_teams.csv"

    def read_schedule_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as schedule_file:
            csv_reader = DictReader(schedule_file)
            schedule_file = list(csv_reader)
            return schedule_file
    
    def move_blueprint_to_public(self):
        """should take the filled event_blueprint and make a knockout schedule in the event file for that"""
        with open(self.get_event_file, "r", encoding="utf-8") as old_event_file:
            csv_reader = DictReader(old_event_file)
            old_event_file = list(csv_reader)
        
        with open(self.public_file_path, "w", encoding="utf-8") as public_event_file:
            public_event_file.write("id,team_name,event_name,event_type")
            for every_line in old_event_file:
                public_event_file.write(",".join(every_line.values()))
                public_event_file.write("\n")
        return "Event is now public"
    # TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def get_match_id(self):
        match_id = 0
        match_id +=1
        return match_id

    def create_first_round(self):
        with open(self.public_file_path, "r", encoding="utf-8") as public_event_file:
            csv_reader = DictReader(public_event_file)
            dict_list = list(csv_reader)

        all_remaining_team_list = []
        for team in dict_list:
            all_remaining_team_list.append(team["team_name"])
        
        with open(self.file_path, "w", encoding="utf-8") as schedule_file:
            schedule_file.write("server_id,match_id,time_of_match,team_a,team_b,winner,match_result")
        for teamsvs in all_remaining_team_list:
            team_a = random.choice()
            all_remaining_team_list.remove(team_a)
            team_b = random.choice()
            all_remaining_team_list.remove(team_b)

            with open(self.file_path, "a", encoding="utf-8") as schedule_file:
                schedule_file.write(f"{self.server_id},{int(self.get_match_id())},{self.schedule_time},{team_a},{team_b},team_a_score,team_b_score,{self.winner},{self.result_score}")
            # TODO
    
    def input_results(self, match_id, team_a_score, team_b_score):
        schedule_file = self.read_schedule_file_as_list_of_dict()
        for line in schedule_file:
            if line["match_id"] == match_id:
                line["team_a_score"] = team_a_score
                line["team_b_score"] = team_b_score
                if team_a_score == team_b_score:
                    line["winner"] = "Tie!"
                if team_a_score > team_b_score:
                    line["winner"] = self.team_a
                if team_a_score < team_b_score:
                    line["winner"] = self.team_b
                break
        return f"Winner for match{match_id} is {self.winner}"


        

    def create_second_round(self):
        schedule_file = self.read_schedule_file_as_list_of_dict()




        with open(self.file_path, "a", encoding="utf-8") as schedule_file:

        

    def create_third_round(self):
        pass

    def declare_winner(self):
        pass

    def get_first_round_results(self):