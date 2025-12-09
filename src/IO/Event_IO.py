from csv import DictReader
from models.event import Event
from IO.Teams_IO import Team_IO

class Event_IO(Event):
    def __init__(self):
        self.file_path = "data/tournament_blueprint.csv"
        self.public_file = "data/schedule.csv"

    def read_file_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            event_data = list(DictReader(event_file))
        return event_data
    
    def create_empty_event(self):
        """takes event details and rewrites the event blueprint file to have all the details of the event in
        the file"""
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            #event_file.write(f"{"id"}{"team_name"}{self.name},{self.game_type},\n")
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
                line["team_name"] = team

        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write("id,team_name,event_name,event_type,")
            for teams in event_data:
                values = teams.values()
                values = [str(v) for v in values]
                event_file.write(",".join(values))
                event_file.write("\n")
        return f"{team} is now a part of this event!"

    def check_if_team_in_event(self, team):
        """takes team name and checks if the team is in the event"""
        event_data = self.read_file_as_list_of_dict()
        for line in event_data:
            if line["team_name"] == team:
                return True
        return False

    def find_next_useable_id(self):
        """checks the next id that has no team associated with it"""
        event_file = self.read_file_as_list_of_dict()
        for line in event_file:
            if line["team_name"] == None:
                return line["id"]

    def how_many_teams_in_event(self):
        """checks how many teams are in the event"""
        next_empty_id = self.find_next_useable_id()
        return int(next_empty_id) - 1
    

    def move_blueprint_to_public(self):
        """should take the filled event_blueprint and make a knockout schedule in the event file for that"""
        with open(self.file_path, "r", encoding="utf-8") as event_blueprint:
            csv_reader = DictReader(event_blueprint)
            event_blueprint = list(csv_reader)
        
        with open(self.public_file, "w", encoding="utf-8") as public_event_file:
            public_event_file.write("id,team_name,event_name,event_type")
            for every_line in event_blueprint:
                public_event_file.write(",".join(every_line.values()))
                public_event_file.write("\n")
        return "Event is now public"
    # TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




    def if_type_is_last_team_standing(self):
        pass
    # mögulega þarf ekki að setja inn í schedule????????? #TODO
