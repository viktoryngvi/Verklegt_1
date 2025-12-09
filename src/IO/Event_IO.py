from csv import DictReader
from models.event import Event
from IO.Teams_IO import Team_IO
from IO.Knockout_IO import Knockout

class Event_IO(Event):
    def __init__(self):
        self.file_path = "data/event_blueprint.csv"
        self.knockout_file = "data/knockout.csv"
        self.Last_team_file = "data/last_team_standing.csv"
        self.knockout = Knockout()
        self.server_id = 0

    def read_file_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            event_data = list(DictReader(event_file))
        return event_data
    
    def find_next_useable_id(self):
        """checks the next id that has no team associated with it"""
        event_file = self.read_file_as_list_of_dict()
        for line in event_file:
            useable_id = int(line["id"])
            if line["team_name"] == "":
                return useable_id
    
    def find_next_server_id(self):
        pass
        
        
###############################################################



    def create_empty_event(self):
        """takes event details and rewrites the event blueprint file to have all the details of the event in
        the file"""
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write("id,team_name,event_name,event_type,")
            # láta event name og type mögulega bara koma einusinni til að gera þetta fallegt
            team_id = 1
            for team in range(len(self.teams) + 1):
                event_file.write(f"{team_id},\n")
                team_id += 1
        return "Event created!"

    def write_team_into_empty_event(self, team):
        """takes a team name and writes it into the blueprint"""
        event_data = self.read_file_as_list_of_dict()        
        next_id = self.find_next_useable_id()
        for line in event_data:
            if line["id"] == next_id:
                line["team_name"] = f"{team},"
                line["event_name"] = f"{self.name},"
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
            
    def how_many_teams_in_event(self):
        """checks how many teams are in the event"""
        next_empty_id = self.find_next_useable_id()
        return int(next_empty_id) - 1

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

        with open(self.knockout_file, "w", encoding="utf-8") as knockout_file:
            knockout_file.write("id,team_name,event_name,event_type")
            for every_line in event_blueprint:
                knockout_file.write(f'{",".join(every_line.values())}\n')
        return "Event is now public"

    def move_blueprint_to_last_team_standing(self):
        with open(self.file_path, "r", encoding="utf-8") as event_blueprint:
            event_blueprint = list(DictReader(event_blueprint))
        
        list_of_teams = []
        for teams in event_blueprint:
            list_of_teams.append(teams["team_name"])

        with open(self.Last_team_file, "w", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,match_id,time_of_match,winner,match_result,teams_list")
            last_team_file.write(f"{self.name},{self.game_type},{self.find_next_server_id()},1,{self.time_of_match},winner,match_result{list_of_teams},")
        return "Event is now public"
    
    def input_last_team_standing_result(self, team_that_won):
        with open(self.Last_team_file, "r", encoding="utf-8") as read_last_team_file:
            read_last_team_file = list(DictReader(read_last_team_file))
        
        for line in read_last_team_file:
            if int(line["match_id"]) == 1:
                line["winner"] = team_that_won
########################## á eftir að velja score!!!!!!!!!!!!!!!!!
        with open(self.Last_team_file, "w", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,match_id,time_of_match,winner,match_result,teams_list")
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
