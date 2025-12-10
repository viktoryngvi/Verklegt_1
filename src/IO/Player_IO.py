from models.player import Player
from csv import DictReader

class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def read_player_file_as_list_of_dict(self):
        with open(self.file_path, "r", encoding="utf-8") as player_data:
            player_data = list(DictReader(player_data))
            return player_data

    def create_player(self, player: Player, id):
        """takes all inputted info and created a player, and checks the last players id and taked the next number"""

        #TODO er logic layer að gera þetta?
        with open(self.file_path, "a", encoding="utf-8") as player_file:
            player_file.write(f"{id},{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.handle},{player.team},\n")
            return "Player successfully created!"

        return "Player already exists"

    def edit_player_info(self, player_file):
        """takes new information from the user and updates the correct player in the file and writes everything back
        into the file"""

        with open ("data/player_new_try_file.csv", "w", encoding="utf-8") as player_file_new:
            player_file_new.write("id,name,phone,address,dob,email,handle,team,captain\n")
            for players in player_file:
                values = players.values()
                values = [str(v) for v in values]
                player_file.write(",".join(values))
                player_file.write("\n")
        return True

    def load_all_player_info(self):
        """loads all player info in a list of dictionaries"""
        player_data = self.read_player_file_as_list_of_dict()
        return player_data




    
