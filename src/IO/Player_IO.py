from models.player import Player
import csv

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    def __init__(self, name, date_of_birth, address, phone_number, email, link, handle, team):
        file_path = "data/player_info.csv"
        self.file_path = file_path

    def create_player(self):
        if not self.check_if_player_exists():
            with open(self.file_path, "a", encoding="utf-8") as player_file:
                player_file.write(f"{self.id},{self.name},{self.phone},{self.address},{self.dob},{self.email},{self.handle},{self.team}{self.captain}\n")
            return "Player created successfully"
        else:
            return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self):
        with open(self.file_path, "r") as player_file:
            for line in player_file:
                if line.startswith(self.name):
                    return True
                # if self.name in line.split(",")[0]:

            return False
                # checkar hverja línu og skoðar hvort það er "name" sem passar við inslegið nafn

    def edit_player_info(self):
        pass  #TODO

    def load_all_player_short_info(self):
        pass
    #loada bara þa name, id og handle
