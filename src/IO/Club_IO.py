from csv import DictReader
from IO.Teams_IO import Team_IO
from models.club import Club

class Club_IO:
    """Reads, adds, registers, views clubs from/to a csv file and checks if a club name is already in use."""
    
    def __init__(self):
        self.file_path = "data/clubs.csv"


    def read_club_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as club_file:
            return list(DictReader(club_file))

        
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


    def add_team_to_club(self, clubs):
        with open(self.file_path, "w", encoding="utf-8") as club_file_out:
            club_file_out.write("club_id,club_name,club_home_town,club_country,club_colors,teams\n")
            for club in clubs:
                club_file_out.write(
                    f"{getattr(club, 'id', '')},"
                    f"{club.name},"
                    f"{club.home_town},"
                    f"{club.country},"
                    f"{';'.join(club.color) if club.color else ''},"
                    f"{';'.join(club.teams) if club.teams else ''}\n"
                )
        return "Club file updated"

    
    def view_clubs(self):
        club_file = self.read_club_file_as_list_of_dict()
        club_list = []
        for row in club_file:
            attributes = row.split(",")
            club = Club()
            club.name = str(attributes[0])
            club.home_town = str(attributes[1])
            club.country = str(attributes[2])
            club.color = str(attributes[3].split(","))
            club.teams = str(attributes[4].split(","))
            
            club_list.append(club)
        
        return club_list
    

    def view_club_information(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                return Club(
                    name=line["club_name"],
                    home_town=line["club_home_town"],
                    country=line["club_country"],
                    color=line["club_colors"].split(";") if line["club_colors"] else [],
                    teams=line["teams"].split(";") if line["teams"] else [],
                )
        return None

            
    def check_if_club_name_in_use(self, club_name):
        club_file = self.read_club_file_as_list_of_dict()
        for line in club_file:
            if line["club_name"] == club_name:
                return True
        return False
    