from models.player import Player
#TODO

class Player_IO(Player):
    def __init__():
        pass

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
    def check_all_players_for_organizer(self):
        with open("src/IO/player_info.csv", "r") as player_file:
            for line in player_file:
                #TODO
                print(line)
        # prentar id, name, og handle hjá öllum players

    def edit_specific_player_for_captain(self):
        