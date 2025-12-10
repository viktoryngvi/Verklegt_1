from csv import DictReader


class Event_IO:
    def __init__(self):
        self.file_path = "data/event_blueprint.csv"
        self.knockout_file = "data/knockout.csv"
        self.Last_team_file = "data/last_team_standing.csv"
        self.public_event_file = "data/puclic_event.csv"
        self.results_file = "data/results.csv"

    def read_public_file_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as event_file:
            event_data = list(DictReader(event_file))
        return event_data
    
    def read_knockout_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as knockout_file:
            event_data = list(DictReader(knockout_file))
        return event_data
    
    def read_last_team_standing_as_list_of_dict(self):
        """shortcut for reusable code"""
        with open(self.file_path, "r", encoding="utf-8") as last_team_file:
            event_data = list(DictReader(last_team_file))
        return event_data
    
    def write_into_event_blueprint(self, event_data):
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write(event_data)

    def move_to_knockout(self, public_data):
        with open(self.file_path, "w", encoding="utf-8") as schedule_file:
            schedule_file.write(public_data)
        return "done!" 
        
    def move_to_last_team_standing(self, public_data):
        with open(self.Last_team_file, "w", encoding="utf-8") as last_team_file:
            last_team_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            last_team_file.write(public_data)
        return "done"
    
    def read_results_file(self):
        with open(self.results_file, "r", encoding="utf-8") as results_file:
            new_results_file = list(DictReader(results_file))
            return new_results_file
            
    
    def write_into_results(self, new_results_file):
        with open(self.results_file, "w", encoding="utf-8") as results_file:
            results_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            results_file.write(new_results_file)

