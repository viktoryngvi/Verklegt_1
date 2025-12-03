from data_wrapper import DLWrapper
# það þarf að færa útfylltan clasa úr file til en til að fá gögnin úr clasanum þarf að importa objectinu?
#TODO

player = input("")
class Player:
    def __init__(self, name="name", date_of_birth="date_of_birth", address="address", phone_number="phone_number", email="email", link="link", handle="handle", team="team"):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.link = link
        self.handle = handle
        self.team = team
    def create_player(self):
        with open("src/IO/player_info.csv", "a") as player_file:
            player_file.write(f"{self.name},{self.date_of_birth},{self.address},{self.phone_number},{self.email},{self.link},{self.handle},{self.team} \n")
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self,name):
        with open("src/IO/player_info.csv", "r") as player_file:
            for line in player_file:
                if name in line:
                    return True
                else:
                    return False
                # checkar hverja línu og skoðar hvort það er "name" sem passar við inslegið nafn

                

while player != "q":
    new_player = Player(player)
    new_player.create_player()
    player = input("")


    