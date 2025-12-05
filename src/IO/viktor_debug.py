from csv import DictReader


# # Edit player function
# def edit_player_function(find_player_id, what_to_edit, new_information):
#     with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
#         csv_reader = DictReader(player_file)
#         player_list = list(csv_reader)
#         player_list

#     for player in player_list:
#         id = int(player["id"])
#         if find_player_id == id:
#             player_to_edit = player
#             continue
#     if not player_to_edit:
#         return "player does not exist"
    

#     with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
#         for correct_editing_thing in player_to_edit:
#             if what_to_edit == correct_editing_thing:
#                 player_to_edit[correct_editing_thing] = new_information
#                 for players in player_list:
#                     player_file.write(f"{player_list[player]},")
#                 player_file.write("\n")
#     return "búið að breyta"


# find_player_id = int(input("hvaða id viltu finna: "))
# what_to_change = str(input("hverju viltu breyta?: "))
# new_change = str(input("nýja breytan: "))


# finna_player = edit_player_function(find_player_id, what_to_change, new_change)
# print(finna_player)





def load_all_player_info():
    """loads all player info in a list of dictionaries"""
    with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
        csv_reader = DictReader(player_file)
        player_list = list(csv_reader)
    print(player_list)

load_all_player_info()