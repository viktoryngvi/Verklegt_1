from models.tournament import Tournament
from csv import DictReader


class Tournament_IO(Tournament):
    def __init__(self):
        self.file_path = "data/Tournament.csv"

    def read_tournament_file(self):
        with open(self.file_path, "r", encoding="utf-8") as Tournament_file:
            csv_reader = DictReader(Tournament_file)
            tournament_data = list(csv_reader)
        return tournament_data
    
    def write_into_file(self, tournament_data):
        with open(self.file_path, "w", encoding="utf-8") as new_tournament_data:
            new_tournament_data.write("id,tournament_name,event_list,tournament_location,start_date,end_date,event_list")
            for every_line in tournament_data:
                new_tournament_data.write(f'{",".join(every_line.values())}\n')
        return True


   