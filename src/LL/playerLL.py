from models.player import Player
from IO.data_wrapper import DLWrapper
from LL.validate import Validate



class PlayerLL:
    """LOGICAL LAYER CLASS FOR PLAYER MANAGEMENT AND VALIDATION"""

    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        """INITIALIZES PlayerLL WITH DLWrapper AND VALIDATION INSTANCE"""
        self._dl_wrapper = dl_wrapper
        self._validate = validate

    # ----------------------------------------------------------------------
    # CREATE PLAYER
    # ----------------------------------------------------------------------
    
    def create_player(self, player: Player):
        """VALIDATES PLAYER DATA AND CREATES PLAYER IN DATA LAYER"""
        validate_errors = self._validate.validate_player(player)

        if validate_errors:
            return validate_errors
        
        id = self.get_new_player_id()
        player.id = id
        create_player = self.create_player_to_data(player)
        return create_player

    def create_player_to_data(self, player: Player):
        """SAVES PLAYER TO DATA LAYER AND RETURNS SUCCESS OR FAILURE"""
        if self._dl_wrapper.create_player(player):
            return "Player successfully created"
        return "Player was not created"

    # ----------------------------------------------------------------------
    # EDIT PLAYER INFORMATION
    # ----------------------------------------------------------------------

    def edit_player_phone(self, handle: str, phone: str) -> str:
        """UPDATES PLAYER PHONE AFTER VALIDATION"""
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        validate_error = self._validate.validate_phone(phone)
        if validate_error:
            return validate_error
        
        list_players: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in list_players:
            if player.handle == handle:
                player.phone = phone
        
        updated = self._dl_wrapper.edit_player_file(list_players)
        if updated:
            return "Success: Player information updated"
        return "Error: Failed to update player"

    def edit_player_email(self, handle: str, email: str) -> str:
        """UPDATES PLAYER EMAIL AFTER VALIDATION"""
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        validate_email = self._validate.validate_email(email)
        if validate_email:
            return validate_email

        # Validate the updated data
        list_players: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in list_players:
            if player.handle == handle:
                player.email = email
        
        updated = self._dl_wrapper.edit_player_file(list_players)
        if updated:
            return "Success: Player information updated"
        return "Error: Failed to update player"

    def edit_player_address(self, handle: str, address: str) -> str:
        """UPDATES PLAYER ADDRESS AFTER VALIDATION"""
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        validate_address = self._validate.validate_address(address)
        if validate_address:
            return validate_address

        # Validate the updated data
        list_players: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in list_players:
            if player.handle == handle:
                player.address = address
        
        updated = self._dl_wrapper.edit_player_file(list_players)
        if updated:
            return "Success: Player information updated"
        return "Error: Failed to update player"

    def edit_player_handle(self, old_handle: str, new_handle: str):
        players = self._dl_wrapper.load_all_player_info()

        # Validate new handle (IMPORTANT)
        if new_handle != old_handle and self.check_if_handle_in_use(new_handle):
            return False  # new handle already taken

        # Update
        for player in players:
            if player.handle == old_handle:
                player.handle = new_handle
                break

        # Save
        self._dl_wrapper.edit_player_file(players)
        return "Successfully changed player handle"

    
    def check_if_handle_in_use(self,handle):
        return self._validate.check_if_handle_in_use(handle)

    # ----------------------------------------------------------------------
    # LOAD PLAYER INFORMATION
    # ----------------------------------------------------------------------

    def load_player_info(self, handle: str):
        """LOADS PLAYER PUBLIC INFORMATION BY HANDLE"""
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        return self.load_all_player_short_info()

    def load_all_player_short_info(self):
        """RETURNS A LIST OF DICTIONARIES WITH PUBLIC PLAYER INFO (ID, NAME, HANDLE, TEAM)"""
        player_file: list[Player] = self._dl_wrapper.load_all_player_info()
        short_list = []
        for players in player_file:
            filtered_player = {players.id, players.name, players.handle, players.team}
            short_list.append(filtered_player)
        return short_list

    def load_player_by_handle(self, handle):
        """RETURNS FULL PLAYER OBJECT GIVEN HANDLE OR ERROR IF NOT FOUND"""
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_list:
            if player.handle == handle:
                return player
        return "Player not found"

    def load_single_player_info(self, handle, player: Player):
        """RETURNS SINGLE PLAYER OBJECT GIVEN HANDLE"""
        player_data: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_data:
            if player.handle == handle:
                return player
        return "Player does not exist"

    # ----------------------------------------------------------------------
    # PLAYER ID AND HANDLE HELPERS
    # ----------------------------------------------------------------------

    def get_new_player_id(self):
        """RETURNS THE NEXT AVAILABLE PLAYER ID"""
        player_data: list[Player] = self._dl_wrapper.load_all_player_info()
        if not player_data:
            return 1
        last_player: Player = player_data[-1]
        next_useable_id = int(last_player.id + 1)
        return next_useable_id

    def check_if_player_id_in_team(self, id):
        """CHECKS IF PLAYER WITH GIVEN ID IS IN A TEAM"""
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_list:
            if id == int(player.id):
                if player.team is None:
                    return False
        return True

    def take_handle_retrun_id(self, handle: str):
        """RETURNS PLAYER ID GIVEN HANDLE"""
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_list:
            if player.handle == handle:
                return player.id
        return False

    def take_id_return_handle(self, id: int):
        """RETURNS PLAYER HANDLE GIVEN ID"""
        player_list: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_list:
            if id == int(player.id):
                return str(player.handle)
        return False

    def take_list_of_players_return_list_of_ids(self, list_of_handles_players):
        """CONVERTS A LIST OF PLAYER OBJECTS INTO A LIST OF THEIR IDS"""
        player_id_list = []
        players_in_list: list[Player] = list_of_handles_players
        for player in players_in_list:
            player_id_list.append(int(player.id))
        return player_id_list

    def take_str_of_players_return_list_of_ids(self, str_of_players: str):
        """CONVERTS A COMMA-SEPARATED STRING OF PLAYER IDS INTO A LIST OF INTEGERS"""
        player_id_list = []
        for player in str_of_players.split(","):
            player_id_list.append(int(player))
        return player_id_list

    # ----------------------------------------------------------------------
    # PLACE PLAYER INTO TEAM
    # ----------------------------------------------------------------------

    def place_player_into_team(self, team_name, player_id):
        """ASSIGNS A PLAYER TO A TEAM AND UPDATES DATA LAYER"""
        player_data: list[Player] = self._dl_wrapper.load_all_player_info()
        for player in player_data:
            if player.id == player_id:
                player.team = team_name
                self._dl_wrapper.edit_player_file(player_data)
        return True
