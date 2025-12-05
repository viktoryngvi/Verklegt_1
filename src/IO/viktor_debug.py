from csv import DictReader

# with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     csv_reader = DictReader(player_file)
#     player_list: list[dict[str, any]] = []
#     short_list = []
#     for line in csv_reader:
#        filtered_player = {"id": line["id"], "name": line["name"], "handle": line["handle"]}
#        short_list.append(filtered_player)

# print(short_list)

# with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     csv_reader = DictReader(player_file)
#     player_list: list[dict[str, any]] = []
#     for line in csv_reader:
#         player_list.append(line)

# print(player_list)


# with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     csv_reader = DictReader(player_file)
#     player_list = list(csv_reader)

# for player in player_list:
#     #breyta því sem á að breyta
#     pass
     
# with open ("data/player_info", "w", encoding="utf-8") as player_file:
#     pass

# print(player)





# with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     list_of_dicts = list(DictReader(player_file))
#     last_id = int(list_of_dicts[-1]["id"])
#     print(last_id)


from models.player import Player
from csv import DictReader

file_path = "data/player_info.csv"

def create_player(self, player: Player):
    if not check_if_player_exists(player):
        with open(file_path, "a", encoding="utf-8") as player_file:
            id = 8
            player_file.write(f"{id},{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.handle},{player.team},{player.captain}\n")
        return "Player created successfully"
    else:
        return "Player already exists"
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið

def check_if_player_exists(self, player: Player):
    with open(file_path, "r", encoding="utf-8") as player_file:
        for line in player_file:
            if line.split(",")[1] == (player.name):
                return True
        return False
    
