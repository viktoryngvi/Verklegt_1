from datetime import date
from models.tournament import Tournament
from csv import DictReader


class Tournament_IO(Tournament):
    """HANDLES READING, WRITING AND EDITING TOURNAMENT INFORMATION IN CSV FILE"""


    def __init__(self):
        self.file_path = "data/Tournament.csv"

    # ----------------------------------------------------------------------
    # READ TOURNAMENT FILE 
    # ----------------------------------------------------------------------

    def read_tournament_file(self):
        """LOADS ALL TOURNAMENTS FROM THE TOURNAMENT CSV FILE"""


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
    
    # ----------------------------------------------------------------------
    # WRITE INTO FILE
    # ----------------------------------------------------------------------

    def write_into_file(self, tournament: Tournament):
        """APPENDS A NEW TOURNAMENT AND SAVES IT INTO THE TOURNAMENT FILE"""

        with open(self.file_path, "a", encoding="utf-8") as new_tournament_data:
            event_list_str = ";".join(str(t) for t in tournament.event_list)

            new_tournament_data.write(
                f'{tournament.tournament_id},'
                f'{tournament.tournament_name},'
                f'{tournament.tournament_location},'
                f'{(date.isoformat(tournament.start_date))},'
                f'{(date.isoformat(tournament.end_date))},'
                f'{event_list_str},'
                f'{tournament.contact_name},'
                f'{tournament.contact_email},'
                f'{tournament.contact_phone},'
                f'\n'
            )

        return "Succefully created tournament"
    
    # ----------------------------------------------------------------------
    # EDIT TOURNAMENT FILE
    # ----------------------------------------------------------------------

    def edit_tournament_file(self, tournaments: list[Tournament]):
        """OVERWRITES THE TOURNAMENT FILE WITH UPDATED TOURNAMENT INFORMATION"""


        with open(self.file_path, "w", encoding="utf-8") as tournament_file:
            tournament_file.write("id,tournament_name,tournament_location,start_date,end_date,event_list,contact_name,contact_email,contact_phone\n")

            for tournament in tournaments:
                event_list_str = ";".join(str(t) for t in tournament.event_list)
                tournament_file.write(
                    f'{tournament.tournament_id},'
                    f'{tournament.tournament_name},'
                    f'{tournament.tournament_location},'
                    f'{date.isoformat(tournament.start_date)},'
                    f'{date.isoformat(tournament.end_date)},'
                    f'{event_list_str},'
                    f'{tournament.contact_name},'
                    f'{tournament.contact_email},'
                    f'{tournament.contact_phone},'
                    f'\n'
                )

        return "tournament has been edited"