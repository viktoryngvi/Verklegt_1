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



# # check_if_player_exists()

# with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     pass



#load all player info()
def check_if_player_exists():
    with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
        csv_reader = DictReader(player_file)
        player_list = list(csv_reader)
    return player_list


# check_if_player_exists()
player_list = check_if_player_exists()
list_of_names = []
for players in player_list:
    names = str(players["name"])
    list_of_names.append(names)
