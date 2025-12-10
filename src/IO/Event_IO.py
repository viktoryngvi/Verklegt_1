from csv import DictReader
from models.event import Event
from IO.Teams_IO import Team_IO
from IO.Knockout_IO import Knockout
import uuid

class Event_IO(Event):
    def __init__(self):
        self.file_path = "data/event_blueprint.csv"
        self.knockout_file = "data/knockout.csv"
        self.Last_team_file = "data/last_team_standing.csv"
        self.public_event_file = "data/puclic_event.csv"
        self.knockout = Knockout()

    def read_file_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            event_data = list(DictReader(event_file))
        return event_data
    
    def write_into_event_blueprint(self, event_data):
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write(event_data)



    def move_to_knockout(self, public_data):
        with open(self.file_path, "a", encoding="utf-8") as schedule_file:
            schedule_file.write("tournament_name,server_id,match_id,time_of_match,game_name,game_type,team_a,team_b,team_a_score,team_b_score,winner,match_result")              
            schedule_file.write(f'{self.tournament_name}{self.server_id},{int(self.get_match_id())},{self.schedule_time},{dict_list["game_name"]},{dict_list["game_type"]}{team_a},{team_b},team_a_score,team_b_score,winner,')
        return "done!" 
        
    def move_to_last_team_standing(self, public_data):
        with open(self.Last_team_file, "a", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            last_team_file.write(public_data)
        return "done"
















    def find_next_useable_id(self):
        """checks the next id that has no team associated with it"""
        event_file = self.read_file_as_list_of_dict()
        for line in event_file:
            useable_id = int(line["id"])
            if line["team_name"] == "":
                return useable_id
    
    def get_server_id(self):
        return str(uuid.uuid4())


# laga þetta
    def create_empty_event(self, tournament_name):
        """takes event details and rewrites the event blueprint file to have all the details of the event in
        the file"""
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write("id,team_name,tournament_name,event_name,event_type,")
            # láta event name og type mögulega bara koma einusinni til að gera þetta fallegt
            team_id = 1
            for team in range(self.teams):
                event_file.write(f"{team_id},\n")
                team_id += 1
        return "Event created!"
    
# #############################################
    def write_team_into_empty_event(self, tournament_name, event, team):
        """takes a team name and writes it into the blueprint"""
        event_data = self.read_file_as_list_of_dict()        
        next_id = self.find_next_useable_id()
        for line in event_data:
            if line["id"] == next_id:
                line["team_name"] = f"{team},"
                line["tournament"] = f"{tournament_name}"
                line["event_name"] = f"{event},"
                line["event_type"] = self.game_type

        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write("id,team_name,event_name,event_type,")
            for teams in event_data:
                values = teams.values()
                values = [str(v) for v in values]
                event_file.write(f'{",".join(values) },\n')
                event_file.write("\n")
        return f"{team} is now a part of this event!"

    def check_if_team_in_event(self, team):
        """takes team name and checks if the team is in the event"""
        event_data = self.read_file_as_list_of_dict()
        for line in event_data:
            if line["team_name"] == team:
                return True
        return False
            
    def make_event_public(self):
        blueprint_file = self.read_file_as_list_of_dict()
        for line in blueprint_file:
            if line["id"] == 1:
                type_of_event = line["event_type"]
        if type_of_event == "knockout":
            return self.move_blueprint_to_knockout()
        if type_of_event == "last_team_standing":
            return self.move_blueprint_to_last_team_standing()
        # if type_of_event == "double_elimination":
        #     return self.move_blueprint_to_double_elimination()

    def move_blueprint_to_knockout(self):
        """should take the filled event_blueprint and make a knockout schedule in the event file for that"""
        with open(self.file_path, "r", encoding="utf-8") as event_blueprint:
            event_blueprint = list(DictReader(event_blueprint))

        with open(self.public_event_file, "w", encoding="utf-8") as public_event_file:
            public_event_file.write("id,team_name,event_name,event_type")
            for every_line in event_blueprint:
                public_event_file.write(f'{",".join(every_line.values())}\n')
        return "Event is now public"

    def move_blueprint_to_last_team_standing(self):
        with open(self.file_path, "r", encoding="utf-8") as event_blueprint:
            event_blueprint = list(DictReader(event_blueprint))
        
        list_of_teams = []
        for teams in event_blueprint:
            list_of_teams.append(teams["team_name"])

        with open(self.Last_team_file, "w", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            last_team_file.write(f"{self.name},{self.game_type},{self.get_server_id},{self.time_of_match},winner,match_result{list_of_teams},")
        return "Event is now public"
    
    def input_last_team_standing_result(self, team_that_won):
        with open(self.Last_team_file, "r", encoding="utf-8") as read_last_team_file:
            read_last_team_file = list(DictReader(read_last_team_file))
        
        for line in read_last_team_file:
            if int(line["match_id"]) == 1:
                line["winner"] = team_that_won
########################## á eftir að velja score!!!!!!!!!!!!!!!!!
        with open(self.Last_team_file, "w", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            for every_line in read_last_team_file:
                last_team_file.write(f'{",".join(every_line.values())}')
        return f"{team_that_won}, is the winner of {self.name}"
        # hvað er time of match??????????????????????????????????????#TODO

    def check_if_last_team_has_winner(self):
        with open(self.Last_team_file, "r", encoding="utf-8") as read_last_team_file:
            read_last_team_file = list(DictReader(read_last_team_file))
        for line in read_last_team_file:
            if int(line["match_id"]) == 1:
                if line["winner"] != "winner":
                    final_string = f"Game winner is {line['winner']}"
                    return final_string
        return "Game is not finnished"

    def move_blueprint_to_double_elimination(self):
        pass
