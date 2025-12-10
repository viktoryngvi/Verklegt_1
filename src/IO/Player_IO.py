from models.player import Player
from csv import DictReader

class Player_IO(Player):
    def __init__(self):
        self.file_path = "data/player_info.csv"

    def load_all_player_info(self)-> list[Player] :
        players: list[Player]=[]
        with open(self.file_path, "r", encoding="utf-8") as player_data:
            headers = player_data.readline().split(",")
            for row in player_data:
                attributes = row.split(",")
                player = Player()
                for i in range(len(headers)):
                    setattr(player, headers[i], attributes[i])
                players.append(player)
                

        return players

    def write_into_player_file(self, players: list[Player]):
        with open(self.file_path, "w", encoding="utf-8") as new_player_file:
            for player in players:

                new_player_file.write(f'{player.name},{player.phone},{player.address},{player.dob},{player.email},{player.id},{player.handle},{player.team}')
                

        return True
