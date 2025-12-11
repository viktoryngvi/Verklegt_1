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

        
    def add_club_id(self, club : Club):
        club_file= self.read_club_file_as_list_of_dict()
        if not club_file:
            return 1
        last_id = int(club_file[-1].id)
        return last_id + 1

                
    def register_club(self, club: Club):
        with open(self.file_path, "a", encoding="utf-8") as club_file:
            club_file.write(
                f"{self.add_club_id()},"
                f"{club.name},"
                f"{club.home_town},"
                f"{club.country},"
                f"{';'.join(club.color) if club.color else ''},"
                f"{club.teams}\n"
            )
        return True


    def add_team_to_club(self, club_name, team_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                teams = line["teams"].split(",") if line["teams"] else []
            # Add new team if not already there
            if team_name not in teams:
                teams.append(team_name)
                line["teams"] = ",".join(teams)
            break

        with open(self.file_path, "w", encoding="utf-8") as club_file:
            club_file.write("club_id,club_name,club_home_town,club_country,club_colors,teams\n")
            for club in club_file:
                club_file.write(f"{club['club_id']},{club['club_name']},{club['club_home_town']},{club['club_country']},{club['club_colors']},{club['teams']}\n")
        return "Team added to club"

    
    def view_clubs(self):
        club_file = self.read_club_file_as_list_of_dict()
        club_list = []
        for line in club_file:
            club = Club(
                name=line["club_name"],
                home_town=line["club_home_town"],
                country=line["club_country"],
                color=line["club_colors"].split(","),
                teams=line["teams"].split(",") if line["teams"] else []
            )
            club_list.append(club)
        return club_list

    def view_club_information(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                club = Club(
                    name=line["club_name"],
                    home_town=line["club_home_town"],
                    country=line["club_country"],
                    color=line["club_colors"].split(","),
                    teams=line["teams"].split(",") if line["teams"] else []
                )
                return club
        return None

            
    def check_if_club_name_in_use(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                return True
        return False
    