from csv import DictReader
from models.club import Club
from IO.Teams_IO import Team_IO

class Club_IO(Club):
    def __init__(self):
        self.file_path = "data/clubs.csv"

    def register_club(self):
        with open(self.file_path, "a", encoding="utf-8") as club_file:
            club_file.write(f"{self.name},{self.home_town},{self.country},{self.colors}")

    def add_team_to_club():
        pass