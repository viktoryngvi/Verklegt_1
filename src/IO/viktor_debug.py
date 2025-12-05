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
# def check_if_player_exists():
#     with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
#         csv_reader = DictReader(player_file)
#         player_list = list(csv_reader)
#     return player_list


# # check_if_player_exists()
# player_list = check_if_player_exists()
# list_of_names = []
# for players in player_list:
#     names = str(players["name"])
#     list_of_names.append(names)




# Edit player function
def edit_player_function(find_player_id, what_to_edit):
    with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
        csv_reader = DictReader(player_file)
        player_list = list(csv_reader)
        player_list

    for player in player_list:
        id = int(player["id"])
        if find_player_id == id:
            player_to_edit = player
    return "player does not exist"
    

    with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
        pl



find_player_id = int(input("hvaða id viltu finna: "))
finna_player = edit_player_function(find_player_id)
print(finna_player)