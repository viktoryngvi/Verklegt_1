from models.tournament import Tournament
from csv import DictReader


class Tournament_IO(Tournament):
    def __init__(self):
        self.file_path = "data/tournament.csv"

    def read_file_as_list_of_dicts(self):
        with open(self.file_path, "r", encoding="utf-8") as Tournament_file:
            csv_reader = DictReader(Tournament_file)
            tournament_data = list(csv_reader)
        return tournament_data

    def get_next_tournament_id(self):
        """checks the last player and returns the id of said player"""
        tournament_data = self.read_file_as_list_of_dicts()
        if not tournament_data:
            next_useable_id = 1
        else:
            next_useable_id = int(tournament_data[-1]["id"])
            next_useable_id += 1
        return next_useable_id

    def create_tournament(self, tournament: Tournament):
        """tournaments should have a list of tournaments that have event names"""
        id = self.get_next_tournament_id()
        with open(self.file_path, "a", encoding="utf-8") as tournament_file:
            tournament_file.write(f"{id},{tournament.name},{tournament.location},{tournament.start_date},{tournament.end_date},event_list\n")
        return "Tournament created!"

    def put_event_into_tournament(self, tournament_name, event_name):
        tournament_file = self.read_file_as_list_of_dicts()
        for line in tournament_file:
            if line["tournament_name"] == tournament_name:
                if line["event_list"] == "event_list":
                    line["event_list"] = []
                    line["event_list"].append(event_name)
                    return "Done!"
                else:
                    line["event_list"].append(event_name)
                    return "Done!"
    
        with open(self.file_path, "w", encoding="utf-8") as new_torunament_file:
            new_torunament_file.write("id,tournament_name,tournament_location, start_date, end_date,event_list")
            for line in tournament_file:
                new_torunament_file.write(f'{",".join(line.values())}\n')

        return "Done!"

    def view_tournaments(self):
        tournament_file = self.read_file_as_list_of_dicts()
        list_of_tournaments = []
        for line in tournament_file:
            list_of_tournaments.append(line["tournament_name"])
        return list_of_tournaments

    def view_events_in_tournament(self, tournament_name):
        tournament_file = self.read_file_as_list_of_dicts()
        for line in tournament_file:
            if line["tournament_name"] == tournament_name:
                return line["event_list"]
        return "No tournament with this name"