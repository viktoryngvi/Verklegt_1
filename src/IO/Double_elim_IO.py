from csv import DictReader
import random
from models.match import Match

class Double_elim_IO(Match):
    def __init__(self):
        self.file_path = "data/double_elim.csv"
        self.blueprint_file = "data/event_blueprint.csv"

    def get_match_id(self):
        schedule_file = self.read_schedule_file_as_list_of_dict()
        last_id = int(schedule_file[-1]["match_id"])
        return last_id + 1
    
    def read_double_elim_file_as_list_of_dicts(self):
        with open(self.file_path, "r", encoding="utf-8") as double_elim_file:
            double_elim_data = list(DictReader(double_elim_file))
            return double_elim_data

    def create_first_round(self):
        with open(self.blueprint_file, "r", encoding="utf-8") as blueprint_file:
            dict_list = list(DictReader(blueprint_file))

        all_team_list = []
        for team in dict_list:
            all_team_list.append(team["team_name"])
        
        with open(self.file_path, "a", encoding="utf-8") as schedule_file:
            schedule_file.write("server_id,match_id,time_of_match,team_a,team_b,winner,match_result")
        for teamsvs in all_team_list:
            team_a = random.choice(teamsvs)
            all_team_list.remove(team_a)
            team_b = random.choice(teamsvs)
            all_team_list.remove(team_b)
            with open(self.file_path, "a", encoding="utf-8") as schedule_file:
                schedule_file.write(f"{self.server_id},{int(self.get_match_id())},{self.schedule_time},{team_a},{team_b},team_a_score,team_b_score,winner,")

    def second_round(self):
        pass

    def third_round(self):
        pass

    def fourth_round(self):
        pass
    
    def get_placement(self):
        pass

    def what_rounds_are_done(self):
        pass