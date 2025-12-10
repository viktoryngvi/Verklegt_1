from models.player import Player

class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def load_all_player_info(self):
        player_list = []
        with open(self.file_path, "r", encoding="utf-8") as player_data:
            headers = player_data.readline().split(",")
            for row in player_data:
                attributes = row.split(",")
                player = Player()
                for i in range(len(headers)):
                    setattr(player, headers[i], attributes[i])

                player_list.append(player)

            return player_list

    def write_into_player_file(self, player: Player):
        player_data:list[Player] = self.load_all_player_info()
        player_data.append(player)

        with open(self.file_path, "w", encoding="utf-8") as new_player_file:
            new_player_file.write(player_data)

        return True
