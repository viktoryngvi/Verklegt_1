from datetime import date
from models.tournament import Tournament
from csv import DictReader


class Tournament_IO(Tournament):
    def __init__(self):
        self.file_path = "data/Tournament.csv"

    def read_tournament_file(self):
        tournament_list = []
        with open(self.file_path, "r", encoding="utf-8") as Tournament_file:
            headers = Tournament_file.readline().split(",")
            for row in Tournament_file:
                attributes = row.split(",")
                tournament = Tournament()
                tournament.tournament_id = (attributes[0])
                tournament.tournament_name = str(attributes[1])
                tournament.tournament_location = str(attributes[2])
                tournament.start_date = date.fromisoformat(attributes[3])
                tournament.end_date = date.fromisoformat(attributes[4])
                tournament.event_list = list(attributes[5].split(";"))
                tournament.contact_name = str(attributes[6])
                tournament.contact_email = str(attributes[7])
                tournament.contact_phone = str(attributes[8])

                tournament_list.append(tournament)
        return tournament_list

    def write_into_file(self, tournament: Tournament):
        with open(self.file_path, "a", encoding="utf-8") as new_tournament_data:

            new_tournament_data.write(
                f'{tournament.tournament_id},'
                f'{tournament.tournament_name},'
                f'{tournament.tournament_location},'
                f'{(tournament.start_date)},'
                f'{(tournament.end_date)},'
                f'{tournament.event_list},'
                f'{tournament.contact_name},'
                f'{tournament.contact_email},'
                f'{tournament.contact_phone},'
                f'\n'
            )
        return True

    def edit_tournament_file(self, tournaments: list[Tournament]):
        with open(self.file_path, "w", encoding="utf-8") as tournament_file:
            tournament_file.write("id,tournament_name,tournament_location,start_date,end_date,event_list,contact_name,contact_email,contact_phone\n")
            for tournament in tournaments:
                tournament_file.write(
                    f'{tournament.tournament_id},'
                    f'{tournament.tournament_name},'
                    f'{tournament.tournament_location},'
                    f'{date.isoformat(tournament.start_date)},'
                    f'{date.isoformat(tournament.end_date)},'
                    f'{tournament.event_list},'
                    f'{tournament.contact_name},'
                    f'{tournament.contact_email},'
                    f'{tournament.contact_phone},'
                    f'\n'
                )
        return "tournament has been edited"