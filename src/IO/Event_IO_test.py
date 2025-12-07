from csv import DictReader
from models.event import Event
from IO.Teams_IO import Team_IO

class Event_IO_test(Event):
    def __init__(self, ):
        self.file_path = "data/tournament_blueprint.csv"

    def read_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            csv_reader = DictReader(event_file)
            event_data = list(csv_reader)
            return event_data
    
    def create_empty_event(self):
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write(f"{"id"}{"team_name"}{self.name},{self.game_type},\n")
            team_id = 1
            for team in range(len(self.teams) + 1):
                event_file.write(f"{team_id},\n")
                team_id += 1
        return "Event created!"

    def write_team_into_empty_event(self, team):
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
    
    def find_next_useable_id(self):
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            for line in event_file:
                if line["team_name"] == None:
                    return line["id"]

    def check_if_team_in_event(self, team):
        event_data = self.read_file_as_list_of_dict()
        for line in event_data:
            if line["team_name"] == team:
                return True
        return False    

    def how_many_teams_in_event(self):
        event_data = self.read_file_as_list_of_dict()
        for line in event_data:
            if line["team_name"] == None:
                return line["id"]