from IO.Teams_IO import Team_IO
from models.club import Club

class Club_IO:
    """Reads, adds, registers, views clubs from/to a csv file and checks if a club name is already in use."""
    
    
    def __init__(self):
        self.file_path = "data/clubs.csv"

    def load_all_clubs(self):
        clubs_list = []
        with open(self.file_path, "r", encoding="utf-8") as club_data:
            headers = club_data.readline().split(",")
            for row in club_data:
                attributes = row.split(",")
                club = Club()
                club.name = str(attributes[0])
                club.home_town = str(attributes[1])
                club.country = str(attributes[2])
                club.colors = list(attributes[3].split(";"))
                club.teams = list(attributes[4].split(";"))

                clubs_list.append(club)

        return clubs_list
                
    def register_club(self, club: Club):
        """ REGISTER CLUB APPEND IN CSV, RETURNS TRUE WHEN DONE """

        with open(self.file_path, "a", encoding="utf-8") as club_file:

            club_file.write(
                f'{club.name},'
                f'{club.home_town},'
                f'{club.country},'
                f'{";".join(club.colors)},'
                f'{";".join(club.teams)},'
                f'\n'
            )
            
        return True
    
    def edit_teamss_file(self, clubs: list[Club]):
        with open(self.file_path, "w", encoding="utf-8") as clubs_file:
            clubs_file.write("id,team,captain_handle,player_list\n")
            for club in clubs:
                teams = ";".join(str(t) for t in club.teams)
                clubs_file.write(
                    f'{club.name},'
                    f'{club.home_town},'
                    f'{club.country},'
                    f'{club.colors},'
                    f'{teams},'
                    f'\n'
                )
        return "team has been edited"




    

    