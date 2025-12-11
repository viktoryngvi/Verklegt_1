from csv import DictReader
from IO.Teams_IO import Team_IO
from models.club import Club

class Club_IO:
    """Reads, adds, registers, views clubs from/to a csv file and checks if a club name is already in use."""
    
    def __init__(self):
        self.file_path = "data/clubs.csv"


    def read_club_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as club_file:
            club_file = list(DictReader(club_file))
            return club_file

        
    def add_club_id(self):
        club_file= self.read_club_file_as_list_of_dict()
        if not club_file:
            return 1
        last_id = int(club_file[-1]["club_id"])
        return last_id + 1

                
    def register_club(self, club_name: str, club_home_town: str, club_country: str, club_colors: list[str] = None, teams: list[str] = None):
        club = Club(
            name=club_name,
            home_town=club_home_town,
            country=club_country,
            colors=club_colors.split(","),
            teams=teams
        )


    def add_team_to_club(self, club_name, team_name):
        with open(self.file_path, "r", encoding="utf-8") as club_file:
            csv_reader = DictReader(club_file)
            club_list = list(csv_reader)
        for line in club_list:
            if line["club_name"] == club_name:
                club_to_edit = club_name
                if line["teams"] == "teams":
                    line["teams"] = []
                line["teams"].append(team_name)
                break
        return "Team added to club"

    
    def view_clubs(self):
        club_file = self.read_club_file_as_list_of_dict()
        club_list = []
        for line in club_file:
            club_list.append(line["club_name"])
        return club_list

    def view_club_information(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                return line

            
    def check_if_club_name_in_use(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                return True
        return False
    