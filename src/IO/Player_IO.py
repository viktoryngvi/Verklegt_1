from models.player import Player
from csv import DictReader

# player = input("insláðu nýjan player: ")
class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def create_player(self, player: Player):
        """takes all inputted info and created a player, and checks the last players id and taked the next number"""
        if not self.check_if_handle_in_use(player.handle):
            #TODO er logic layer að gera þetta?
            with open(self.file_path, "a", encoding="utf-8") as player_file:
                id = self.check_last_id() + 1
                player_file.write(f"{id},{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.handle},{player.team},\n")
                return "Player successfully created!"
        else:
            return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

    def edit_player_info(self, find_player_handle, what_to_edit, new_information):
        """takes new information from the user and updates the correct player in the file and writes everything back
        into the file"""
        with open(self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list = list(csv_reader)

        for player in player_list:
            handle = str(player["handle"])
            if find_player_handle == handle:
                player_to_edit = player
                break
        player_to_edit[what_to_edit] = new_information

        with open (self.file_path, "w", encoding="utf-8") as player_file:
            player_file.write("id,name,phone,address,dob,email,handle,team,captain\n")
            for players in player_list:
                values = players.values()
                values = [str(v) for v in values]
                player_file.write(",".join(values))
                player_file.write("\n")
        return True

    def load_all_player_info(self):
        """loads all player info in a list of dictionaries"""
        with open(self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list = list(csv_reader)
        return player_list

    def load_all_player_short_info(self):
        """loads a list of dictionarys containing only the id, name, handle and team of the player(public information)"""
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            csv_reader = DictReader(player_file)
            player_list = list(csv_reader)
            short_list = []
            for line in csv_reader:
                filtered_player = {"id": line["id"], "name": line["name"], "handle": line["handle"], "team": line["team"]}
                short_list.append(filtered_player)
        return short_list
    #býr til lista af dicts af id, name og handle hjá öllum players

    def check_last_id(self):
        """checks the last player and returns the id of said player"""
        with open (self.file_path, "r", encoding="utf-8") as player_file:
            list_of_dicts = list(DictReader(player_file))
            last_id = int(list_of_dicts[-1]["id"])
        return last_id
    
    def check_if_handle_in_use(self, handle):
        """checks ef the inputted handle is in use in the player list"""
        player_list = self.load_all_player_info()
        for players in player_list:
            if handle == str(players["handle"]):
                return True
        return False
    
    def check_if_handle_exists_with_player(self, player: Player):
        """checks ef the inputted handle is in use in the player list"""
        player_handle = self.check_if_handle_in_use(player.handle)
        return player_handle

    def check_if_player_id_in_team(self, id):
        """takes id and check if that player is in a team"""
        player_list = self.load_all_player_info()
        for players in player_list:
            if id == int(players["id"]):
                if players["team"] is None:
                    return False
        return True
    # notað til að checka hvort id passar við player sem er ekki í liði
    
    def turn_handle_into_id(self, handle: str):
        """takes handle and returns the players id"""
        player_list = self.load_all_player_info() 
        for players in player_list:
            if handle == str(players["handle"]):
                return int(players["id"])
        return False
    
    
    def take_id_return_handle(self, id: int):
        """takes an id and returns the players handle"""
        player_list = self.load_all_player_info() 
        for players in player_list:
            if id == int(players["id"]):
                return str(players["handle"])
        return False

        # return playerhandle in listofhandles
        