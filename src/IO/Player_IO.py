from models.player import Player
from datetime import date

class Player_IO(Player):
    """HANDLES READING, CREATING AND EDITING PLAYER INFORMATION IN CSV FILE"""


    def __init__(self):
        self.file_path = "data/player_info.csv"

    
    # ----------------------------------------------------------------------
    # LOAD ALL PLAYE INFO 
    # ----------------------------------------------------------------------

    def load_all_player_info(self):
        """LOADS ALL PLAYER INFORMATION FROM PLAYER CSV FILE"""


        player_list = []
        
        with open(self.file_path, "r", encoding="utf-8") as player_data:
        
            headers = player_data.readline().split(",")
        
            for row in player_data:
                attributes = row.split(",")
                player = Player()
                player.id = int(attributes[0])
                player.name = str(attributes[1])
                player.phone = str(attributes[2])
                player.address = str(attributes[3])
                player.dob = date.fromisoformat(attributes[4])
                player.email = str(attributes[5])
                player.handle = str(attributes[6])
                player.team = str(attributes[7])

                player_list.append(player)

        return player_list

    # ----------------------------------------------------------------------
    # CREATE PLAYER
    # ----------------------------------------------------------------------

    def create_player(self, player: Player):
        """APPENDS A NEW PLAYER AND SAVES THEIR INFORMATION INTO THE PLAYER FILE"""
 
        
        with open(self.file_path, "a", encoding="utf-8") as new_player_file:
        
                new_player_file.write(
                    f'{player.id},'
                    f'{player.name},'
                    f'{player.phone},'
                    f'{player.address},'
                    f'{date.isoformat(player.dob)},'
                    f'{player.email},'
                    f'{player.handle},'
                    f'{player.team}'
                    f'\n'
                )
        
        return True

    # ----------------------------------------------------------------------
    # EDIT PLAYER FILE 
    # ----------------------------------------------------------------------

    def edit_player_file(self, players: list[Player]):
        """OVERWRITES PLAYER FILE WITH UPDATED PLAYER INFORMATION"""

        
        with open(self.file_path, "w", encoding="utf-8") as player_file:
        
            player_file.write("id,name,phone,address,dob,email,handle,team\n")
        
            for player in players:
                player_file.write(
                    f'{player.id},'
                    f'{player.name},'
                    f'{player.phone},'
                    f'{player.address},'
                    f'{date.isoformat(player.dob)},'
                    f'{player.email},'
                    f'{player.handle},'
                    f'{player.team},'
                    f'\n'
                )
        
        return True