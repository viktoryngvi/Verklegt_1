from models.player import Player
from IO.data_wrapper import DLWrapper
from LL.validate import Validate



class PlayerLL:
    """
    The Player Logical Layer (LL) class.
    
    This layer is responsible for handling business logic related to Player objects,
    including validation of data fields (e.g., name, email, DOB) and coordinating 
    data persistence by interacting with the Data Layer (DLWrapper).
    """
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        """
        Initializes the PlayerLL instance with a Data Layer wrapper.
        
        This dependency injection allows the PlayerLL to access storage functions 
        without knowing the underlying storage implementation (e.g., CSV, database).

        :param dl_wrapper: An instance of DLWrapper used for all data access operations.
        :type dl_wrapper: DLWrapper
        """
        self._dl_wrapper = dl_wrapper
        self._validate = validate

        
    def create_player(self, player: Player):
        """
        Validates the player data and, if valid, passes it to the Data Layer for storage.
        """
        validate_errors = self._validate.validate_player(player)

        if validate_errors:
            # If a list of errors is returned, stop and return the errors.
            return validate_errors
        
        id = self.get_new_player_id()
        player.id = id
        create_player = self.create_player_to_data(player)
        return create_player
    
    def create_player_to_data(self, player: Player):
        """takes all inputted info and created a player, and checks the last players id and taked the next number"""

        if self._dl_wrapper.create_player(player):
            return "PLayer successfully created"
        
        return "Player was not created" 


    def edit_player_phone(self, handle: str, phone: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        # Validate the updated data
        validate_error = self._validate.validate_phone(phone)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "phone", phone)
        if updated:
            return "Success: Player information updated"
        
        return "Error: Failed to update player"


    def edit_player_email(self, handle: str, email: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        # Validate the updated data
        validate_error = self._validate.validate_email(email)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "email", email)
        if updated:
            return "Success: Player information updated"

        return "Error: Failed to update player"


    def edit_player_address(self, handle: str, address: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        # Validate the updated data
        validate_error = self._validate.validate_address(address)
        if validate_error:
            return validate_error
        
        updated = self._dl_wrapper.edit_player_info(handle, "address", address)
        if updated:
            return "Success: Player information updated"
        
        return "Error: Failed to update player"


    def edit_player_handle(self, handle: str, handle_str: str) -> str:
        """
        Handles the business logic for updating an existing player's information.
        """
        # Check if player exists
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        existing_new_handle = self._validate.check_if_handle_in_use(handle_str)
        if existing_new_handle:
            return "Error: New handle already exists"
        
        updated = self.edit_player_try(handle, "handle", handle_str)
        if updated:
            return "Success: Player information updated"
        
        return "Error: Failed to update player"
        
    def load_player_info(self, handle: str):
        existing_player = self._validate.check_if_handle_in_use(handle)
        if not existing_player:
            return "Error: Player handle does not exists"
        
        return self.load_all_player_short_info()

    def edit_player_try(self, find_player_handle, what_to_edit, new_information):
        player_file = self._dl_wrapper.load_all_player_info()
        for player in player_file:
            handle = player(["handle"])
            if find_player_handle == handle:
                player[what_to_edit] = new_information
                return self._dl_wrapper.edit_player_info(player_file)

    def load_all_player_short_info(self):
        """loads a list of dictionarys containing only the id, name, handle and team of the player(public information)"""
        player_file = self._dl_wrapper.load_all_player_info()
        short_list = []
        for line in player_file:
            filtered_player = {"id": line["id"], "name": line["name"], "handle": line["handle"], "team": line["team"]}
            short_list.append(filtered_player)
        return short_list
    #býr til lista af dicts af id, name og

    def get_new_player_id(self):
        """checks the last player and returns the id of said player"""
        player_data: list[Player] = self._dl_wrapper.load_all_player_info()
        if not player_data:
            return 1
        
        last_player: Player = player_data[-1]
        next_useable_id = last_player.id+1
        return next_useable_id
    
    # notað til að checka hvort id passar við player sem er ekki í liði
    
    def check_if_player_id_in_team(self, player: Player, id):
        """takes id and check if that player is in a team"""
        player_list = self._dl_wrapper.load_all_player_info()
        for row  in player_list:
            if id == int(player.id):
                if player.team is None:
                    return False
        return True


    def turn_handle_into_id(self, handle: str, player: Player):
        """takes handle and returns the players id"""
        player_list = self._dl_wrapper.load_all_player_info() 
        for players in player_list:
            if handle == str(player.handle):
                return int(player.id)
        return False

    def take_id_return_handle(self, id: int, player: Player):
        """takes an id and returns the players handle"""
        player_list = self._dl_wrapper.load_all_player_info() 
        for players in player_list:
            if id == int(player.id):
                return str(player.handle)
        return False

    def load_single_player_info(self, handle, player: Player):
        player_data = self._dl_wrapper.load_all_player_info
        for player in player_data:
            if player.handle == handle:
                return player
        return "Player does not exist"
    














        

        

    
    
    
    
    