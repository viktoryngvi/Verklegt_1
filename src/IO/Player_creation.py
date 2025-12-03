from IO.data_wrapper import DLWrapper
from models.player import Player
# það þarf að færa útfylltan clasa úr file til en til að fá gögnin úr clasanum þarf að importa objectinu?
#TODO

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    # def __init__(self, name="name", date_of_birth="date_of_birth", address="address", phone_number="phone_number", email="email", link="link", handle="handle", team="team"):
        # self.name = name
        # self.date_of_birth = date_of_birth
        # self.address = address
        # self.phone_number = phone_number
        # self.email = email
        # self.link = link
        # self.handle = handle
        # self.team = team
    def create_player(self):
        if not self.check_if_player_exists():
            with open("src/IO/player_info.csv", "a") as player_file:
                player_file.write(f"{self.name},{self.phone},{self.address},{self.dob},{self.email},{self.id},{self.handle},{self.captain}\n")
            return "Player created successfully"
        else:
            return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self):
        with open("src/IO/player_info.csv", "r") as player_file:
            for line in player_file:
                if line.startswith(self.name):
                    return True
                # if self.name in line.split(",")[0]:
                    # return True
            return False
                # checkar hverja línu og skoðar hvort það er "name" sem passar við inslegið nafn

                

# while player != "q":
#     new_player = Player_IO(player)
#     new_player.create_player()
#     player = input("aftur: ")

# check_player = input("ok, núna ertu að gá hvort hann er til: ")
# while check_player != "Q":
#     print(new_player.check_if_player_exists())
#     check_player = input("aftur:): ")
