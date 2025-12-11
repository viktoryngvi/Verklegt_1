from csv import DictReader

class Event_IO:
    def __init__(self):
        self.file_path = "data/event_blueprint.csv"
        self.knockout_file = "data/knockout.csv"
        self.Last_team_file = "data/last_team_standing.csv"
        self.public_event_file = "data/puclic_event.csv"
        self.results_file = "data/results.csv"

    def load_event_blueprint(self):
        event_list = []
        with open(self.file_path, "r", encoding="utf-8") as player_data:
            headers = player_data.readline().split(",")
            for row in player_data:
                attributes = row.split(",")
                player.id = int(attributes[0])
                player.name = str(attributes[1])
                player.phone = str(attributes[2])
                player.address = str(attributes[3])
                player.dob = date.fromisoformat(attributes[4])
                player.email = str(attributes[5])
                player.handle = str(attributes[6])
                player.team = str(attributes[7])

                player_list.append(player)


















    def read_results_file(self):
        with open(self.results_file, "r", encoding="utf-8") as results_file:

            
    def write_into_results(self, new_results_file):
        with open(self.results_file, "w", encoding="utf-8") as results_file:
            results_file.write("game_name,game_type,server_id,time_of_match,winner,match_result,teams_list")
            results_file.write(new_results_file)

