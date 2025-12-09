import random
from csv import DictReader
from models.match import Match

class Knockout(Match):
    def __init__(self):
        self.get_event_file = "data/event_blueprint.csv"
        self.file_path = "data/knockout.csv"
        self.public_file_path = "data/public_event.csv"

    def read_schedule_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as schedule_file:
            schedule_file = list(DictReader(schedule_file))
            return schedule_file

    def get_match_id(self):
        schedule_file = self.read_schedule_file_as_list_of_dict()
        last_id = int(schedule_file[-1]["match_id"])
        return last_id + 1

    def input_match_results(self, match_id, team_a_score, team_b_score):
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

    def create_first_round(self):
        with open(self.public_file_path, "r", encoding="utf-8") as public_event_file:
            dict_list = list(DictReader(public_event_file))

        all_team_list = []
        for team in dict_list:
            all_team_list.append(team["team_name"])
        
        with open(self.file_path, "a", encoding="utf-8") as schedule_file:
            schedule_file.write("server_id,match_id,time_of_match,game_name,game_type,team_a,team_b,team_a_score,team_b_score,winner,match_result")
        for teamsvs in all_team_list:
            team_a = random.choice(teamsvs)
            all_team_list.remove(team_a)
            team_b = random.choice(teamsvs)
            all_team_list.remove(team_b)
            with open(self.file_path, "a", encoding="utf-8") as schedule_file:
                schedule_file.write(f'{self.server_id},{int(self.get_match_id())},{self.schedule_time},{dict_list["game_name"]},{dict_list["game_type"]}{team_a},{team_b},team_a_score,team_b_score,winner,')

    def create_round_2_3_and_4(self, round: int):
        schedule_file = self.read_schedule_file_as_list_of_dict()
        list_of_winners_from_bracket = []
        for line in schedule_file[round:]:
            list_of_winners_from_bracket.append(line["winner"])
        for team in list_of_winners_from_bracket:
            team_a = list_of_winners_from_bracket[0]
            list_of_winners_from_bracket.pop(0)
            team_b = list_of_winners_from_bracket[0]
            list_of_winners_from_bracket.pop(0)

            with open(self.file_path, "a", encoding="utf-8") as schedule_file:
                schedule_file.write(f"{self.server_id},{int(self.get_match_id())},{self.schedule_time},{team_a},{team_b},team_a_score,team_b_score,winner")
        return "Round created"
            
    def create_second_round(self):
        round = int(0)
        second_round = self.create_round_2_3_and_4(round)
        return "second bracket created!"

    def create_third_round(self):
        round = int(9)
        third_round = self.create_round_2_3_and_4(round)
        return "third bracked created!"
    
    def create_fourth_round(self):
        round = int(13)
        fourth_round = self.create_round_2_3_and_4(round)
        return "final round created!"

    def declare_winner(self):
        schedule_file = self.read_schedule_file_as_list_of_dict()
        for line in schedule_file[15:]:
            winner = line["winner"] if line["winner"] else "No final winner yet"
        return winner

    def how_many_matches_have_winners(self):
        schedule_file = self.read_schedule_file_as_list_of_dict()
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

    def get_results_from_one_game