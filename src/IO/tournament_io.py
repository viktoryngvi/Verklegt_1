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

    def create_tournament(self, name):
        """tournaments should have a list of tournaments that have event names"""
        with open(self.file_path, "a", encoding="utf-8") as tournament_file:
            

    
    def view_tournaments():
        pass

    def put_event_into_tournament():
        pass

