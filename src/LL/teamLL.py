from IO.data_wrapper import DLWrapper

class TeamLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper

    def create_team(self, cap_id: int, team_name: str, players_id: list):
        last_id = self._dl_wrapper.check_last_id
        if cap_id > last_id:
            return "Captain id does not exist "
        
        for player_id in players_id:
            if not self._dl_wrapper.check_if_player_id_in_team(players_id): # check if the id of the player is not in the list of valid id 
                return "Player's id does not exist" 
            
        create_team = self._dl_wrapper.create_team(cap_id, team_name, players_id)

    def load_player_short_info(self):
        return self._dl_wrapper.load_all_player_short_info()
