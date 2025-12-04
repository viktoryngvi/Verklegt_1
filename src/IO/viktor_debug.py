from csv import DictReader

# with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
#     csv_reader = DictReader(player_file)
#     player_list: list[dict[str, any]] = []
#     short_list = []
#     for line in csv_reader:
#        filtered_player = {"id": line["id"], "name": line["name"], "handle": line["handle"]}
#        short_list.append(filtered_player)

# print(short_list)

with open ("data/player_info.csv", "r", encoding="utf-8") as player_file:
    csv_reader = DictReader(player_file)
    player_list: list[dict[str, any]] = []
    for line in csv_reader:
        player_list.append(line)

print(player_list)