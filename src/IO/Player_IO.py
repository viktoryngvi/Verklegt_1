from IO.data_wrapper import DLWrapper
from models.player import Player
#TODO

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    # def __init__(self, name="name", date_of_birth="date_of_birth", address="address", phone_number="phone_number", email="email", link="link", handle="handle", team="team"):

    def __init__(self):
        self.file_path = "src/IO/player_info.csv"


    def create_player(self):
        if not self.check_if_player_exists():
            with open(self.file_path "a") as player_file:
                player_file.write(f"{self.name},{self.phone},{self.address},{self.dob},{self.email},{self.id},{self.handle},{self.captain}\n")
            return "Player created successfully"
        else:
            return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self):
        with open(self.file_path "r") as player_file:
            for line in player_file:
                if line.startswith(self.name):
                    return True
                # if self.name in line.split(",")[0]:

            return False
                # checkar hverja línu og skoðar hvort það er "name" sem passar við inslegið nafn
