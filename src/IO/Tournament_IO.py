from models.tournament import Tournament
from csv import DictReader


class Tournament_IO(Tournament):
    def __init__(self):
        self.file_path = "data/Tournament.csv"

    def read_tournament_file(self):
        with open(self.file_path, "r", encoding="utf-8") as Tournament_file:
            headers = Tournament_file.readline().split(",")
            for row in Tournament_file:
                attributes = row.split(",")
                tournament = Tournament()
                for i in range(len(headers)):
                    setattr(tournament, headers[i], attributes[i])

        return tournament
    
    def write_into_file(self, tournament_data, tournament: Tournament):
        with open(self.file_path, "w", encoding="utf-8") as new_tournament_data:
            new_tournament_data.write("id,tournament_name,event_list,tournament_location,start_date,end_date,event_list")
            #new_tournament_data.write(f"{tournament.tournament_id},{tournament.name},{tournament_data.location},{tournament_data.start_date},{tournament_data.end_date},{f'{";".join(tournament.event_list)}'}
        return True


   