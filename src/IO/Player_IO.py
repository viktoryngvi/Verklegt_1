from models.player import Player
from csv import DictReader

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def create_player(self, player: Player):
        if not self.check_if_player_exists(player):
            with open(self.file_path, "a", encoding="utf-8") as player_file:
                id = self.check_last_id()
                player_file.write(f"{id},{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.handle},{player.team},{player.captain}\n")
            return "Player created successfully"
        else:
            return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self, player: Player):
        with open(self.file_path, "r") as player_file:
            for line in player_file:
                if line.split(",")[1] == (player.name):
                    return True
            return False
                # checkar hverja línu og skoðar hvort það er "name" sem passar við inslegið nafn

    def edit_player_info(self):
        if not self.check_if_player_exists():
            with open (self.file_path, "r", encoding="utf-8") as player_file:
                csv_reader = DictReader(player_file)

          

    def load_all_player_short_info(self):
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list: list[dict[str, any]] = []
            short_list = []
            for line in csv_reader:
                filtered_player = {"id": line["id"], "name": line["name"], "handle": line["handle"]}
                short_list.append(filtered_player)
        return short_list
    #býr til lista af dicts af id, name og handle hjá öllum players

    def load_all_player_info(self):
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list: list[dict[str, any]] = []
            for line in csv_reader:
                player_list.append(line)
            if len(player_list) == 0:
                return "No players exists"
        return player_list
    

    def check_if_handle_exists():
        return True or False
    
    def check_last_id(self):
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            list_of_dicts = list(DictReader(player_file))
            last_id = int(list_of_dicts[-1]["id"])
        return last_id

    

# Viktor Yngvi Ísaksson
# 849-0903
# blöndós 5
# 2004-25-70
# viktor@gamil.is
# vikkman