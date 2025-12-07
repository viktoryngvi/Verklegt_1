from csv import DictReader
from models.event import Event
from IO.Teams_IO import Team_IO

class Event_IO_test(Event):
    def __init__(self, ):
        self.file_path = "data/tournament_blueprint.csv"
    
    def create_empty_event(self):
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write(f"{"id"}{self.name},{self.game_type},\n")
            team_id = 1
            for teams in range(len(self.teams) + 1):
                event_file.write(f"{team_id},\n")
                team_id += 1

    def write_into_team(self, team):
        with open(self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list = list(csv_reader)  

        for 

        for player in player_list:
            handle = str(player["handle"])
            if find_player_handle == handle:
                player_to_edit = player
                break
        player_to_edit[what_to_edit] = new_information

        with open (self.file_path, "w", encoding="utf-8") as player_file:
            player_file.write("id,name,phone,address,dob,email,handle,team,captain\n")
            for players in player_list:
                values = players.values()
                values = [str(v) for v in values]
                player_file.write(",".join(values))
                player_file.write("\n")
        return True
    
    find