from csv import DictReader


# Edit player function
# def edit_player_function(find_player_id, what_to_edit, new_information):
#     with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
#         csv_reader = DictReader(player_file)
#         player_list = list(csv_reader)

#     for player in player_list:
#         id = int(player["id"])
#         if find_player_id == id:
#             player_to_edit = player
#             break
#     player_to_edit[what_to_edit] = new_information

#     with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
#         player_file.write("id,name,phone,address,dob,email,handle,team,captain\n")
#         for players in player_list:
#             values = players.values()
#             values = [str(v) for v in values]
#             player_file.write(",".join(values))
#             player_file.write("\n")

#     print("Done!")

#     with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
#         for correct_editing_value in player_to_edit:
#             if what_to_edit == correct_editing_value:
#                 player_to_edit[correct_editing_value] = new_information
#                 for players in player_list:
#                     player_file.write(f"{player_list[players]},")
#                 player_file.write("\n")
#     return "búið að breyta"

# find_player_id = int(input("hvaða id viltu finna: "))
# what_to_change = str(input("hverju viltu breyta?: "))
# new_change = str(input("nýja breytan: "))
# edit_player_function(find_player_id, what_to_change, new_change)
# finna_player = edit_player_function(find_player_id, what_to_change, new_change)
# print(finna_player)





# def view_all_teams(self):
#     with open (self.file_path, "r", encoding="utf-8") as teams_file:
#         csv_reader = DictReader(teams_file)
#         teams_list = list(csv_reader)
#         teams_list = []
#         for line in teams_file:
#                 teams_list.append(line.split(",")[0])
#     return teams_list

# load_all_player_info()
# for players in player_list:
#     values = players.values()
#     values = [str(v) for v in values]
#     player_file.write(",".join(values))
#     player_file.write("\n")

# def create_team(name, captain, players):
#     with open("data/teams_test.csv", "a", encoding="utf-8") as teams_file:
#         teams_file.write(f"{name},{captain},")
#         for player in players:
#             values_of_players = player.values()
#             values_of_players = [str(value)for value in values_of_players]
#             teams_file.write(f"{",".join(values_of_players)},")
#         teams_file.write("\n")
#     print("Done!")




# def create_team(name, captain_id, list_of_player_ids):
#     """Takes three variables team_name, team_captain-in id, list af player_id´s and writes it into 
#     the teams.csv file"""
#     with open("data/teams_test.csv", "a", encoding="utf-8") as teams_file:
#         captain_handle = Player_IO.take_id_return_handle(captain_id)
#         teams_file.write(f"{name},{captain_handle},")
#         for player_id in list_of_player_ids:
#             player_handle = Player_IO.take_id_return_handle(player_id)
#             teams_file.write(player_handle)
#         teams_file.write("\n")
#     print("Done!")



# def take_player_ids_return_handles(player_list_of_ids):
#     player_list = Player_IO.load_all_player_info()
#     list_of_handles = []
#     for id in player_list_of_ids:
#         for player in player_list:
#             if id == int(player["id"]):
#                 list_of_handles.append(player["handle"])
#     print(list_of_handles)

# player_list_of_ids = [2, 6, 20]
# take_player_ids_return_handles(player_list_of_ids)

# player_ids = [1, 5, 2]
# name = input("input name of team::")
# captain_id = input("input id of captain: ")


# created_team = create_team(name, captain_id, player_ids)



# from Player_IO import Player_IO

# def players_team_none():
#     list_of_non_team_players_short_info = []
#     all_players = Player_IO.load_all_player_info()
#     for players in all_players:
#         if players["team"] == None:
#             list_of_non_team_players_short_info.append({"id":["id"], "name": line["name"], "handle": line["handle"]})
#     return list_of_non_team_players_short_info





# def check_if_player_handle_exists(self, player: Player):
#     """checks if some player in the file has the same name as the inputted handle"""
#     player_list = self.load_all_player_info()
#     list_of_handles = []
#     for players in player_list:
#         handle = str(players["handle"])
#         list_of_handles.append(handle)
#     if player.handle in list_of_handles:
#         return True
#     return False

# def check_if_handle_exists_with_player(self, player: Player):
#     """checks ef the inputted handle is in use in the player list"""
#     player_list = self.load_all_player_info()
#     list_of_handels = []
#     for players in player_list:
#         if player.handle
#         handles_of_existing_players = str(players["handle"])
#         list_of_handels.append(handles_of_existing_players)
#     if player.handle in list_of_handels:
#         return True
#     else:
#         return False
        

# def check_if_handle_exists_with_handle(self, handle):
#     """checks ef the inputted handle is in use in the player list"""
#     player_list = self.load_all_player_info() 
#     list_of_handels = []
#     for players in player_list:
#         handles_of_existing_players = str(players["handle"])
#         list_of_handels.append(handles_of_existing_players)
#     if handle in list_of_handels:
#         return True
#     else:
#         return False