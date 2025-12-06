from csv import DictReader


# Edit player function
def edit_player_function(find_player_id, what_to_edit, new_information):
    with open("data/player_info.csv", "r", encoding="utf-8") as player_file:
        csv_reader = DictReader(player_file)
        player_list = list(csv_reader)

    for player in player_list:
        id = int(player["id"])
        if find_player_id == id:
            player_to_edit = player
            break
    player_to_edit[what_to_edit] = new_information

    with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
        for players in player_list:
            player_file.write(f"{players.values},")
            player_file.write("\n")
            # for values in players:
            #     player_file.write(f"{players.values},")
            #     player_file.write("\n")
    print("Done!")

    # with open ("data/player_info_new_test.csv", "w", encoding="utf-8") as player_file:
    #     for correct_editing_value in player_to_edit:
    #         if what_to_edit == correct_editing_value:
    #             player_to_edit[correct_editing_value] = new_information
    #             for players in player_list:
    #                 player_file.write(f"{player_list[players]},")
    #             player_file.write("\n")
    # return "búið að breyta"


find_player_id = int(input("hvaða id viltu finna: "))
what_to_change = str(input("hverju viltu breyta?: "))
new_change = str(input("nýja breytan: "))
edit_player_function(find_player_id, what_to_change, new_change)


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




