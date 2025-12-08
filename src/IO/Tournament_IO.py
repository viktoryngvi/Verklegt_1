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

    def create_tournament(self, tournament_name):
        """tournaments should have a list of tournaments that have event names"""
        with open(self.file_path, "a", encoding="utf-8") as tournament_file:
            tournament_file.write(f"{tournament_name},event_list")
        return  "Tournament created!"

    def put_event_into_tournament(self, tournament_name, event_name):
        tournament_file = self.read_file_as_list_of_dicts()
        for line in tournament_file:
            if line["tournament_name"] is tournament_name:
                if line["event_list"] == "event_list":
                    line["event_list"] = []
                    line["event_list"].append(event_name)
                    return "Done!"
                line["event_list"].append(event_name)
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