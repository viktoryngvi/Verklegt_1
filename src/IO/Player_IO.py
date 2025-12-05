from models.player import Player
from csv import DictReader
from models.player import Player

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def create_player(self, player: Player):
        """takes all inputted info and created a player, and checks the last players id and taked the next number"""
        if not self.check_if_player_exists(player):
            with open(self.file_path, "a", encoding="utf-8") as player_file:
                id = self.check_last_id() + 1
                player_file.write(f"{id},{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.handle},{player.team},{player.captain}\n")
                return True
        else:
            return False
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def check_if_player_exists(self, player: Player):
        """checks if some player in the file has the same name as the inputted name"""
        player_list = self.load_all_player_info()
        list_of_names = []
        for players in player_list:
            names = str(players["name"])
            list_of_names.append(names)
        if player.name in list_of_names:
            return True
        return False
        # checkar hverja línu í file-inum og skoðar hvort það er "name" sem passar við inslegið nafn

    def edit_player_info(self):
        """is supposed to edit a single players info in the csv file"""
        if not self.check_if_player_exists(self):
            with open (self.file_path, "r", encoding="utf-8") as player_file:
                csv_reader = DictReader(player_file)


    def load_all_player_info(self):
        """loads all player info in a list of dictionaries"""
        with open(self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list = list(csv_reader)
        return player_list
    
    def check_last_id(self):
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            list_of_dicts = list(DictReader(player_file))
            last_id = int(list_of_dicts[-1]["id"])
        return last_id


    def check_if_handle_exists(self, player: Player):
        """checks ef the inputted handle is in use in the player list"""
        player_list = self.load_all_player_info()
        list_of_handels = []
        for players in player_list:
            handles_of_existing_players = players["handle"]
            list_of_handels.append(handles_of_existing_players)
        return player.handle in list_of_handels
        
        
    def check_last_id(self):
        """checks the last player and returns the id of said player"""
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            list_of_dicts = list(DictReader(player_file))
            last_id = int(list_of_dicts[-1]["id"])
        return last_id