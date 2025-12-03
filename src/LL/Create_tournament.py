from datetime import datetime



# There are 3 classes in this file: create tournament, register team, generate tournament schedule

# in create tournament we have the main class that takes input and routes it to data storage and schedule generation
# in create tournament, todo data storage and schedule generation functions need to be implemented


# in register team we have a helper class for managing team registration.
# in register team, todo player management functions need to be implemented.

# in generate tournament schedule we have a helper class for generating schedules based on tournament type
# in generate tournament schedule, todo scheduling algorithms need to be implemented.


class CreateTournament:

    
    def __init__(self, tournament_name: str, tournament_type: str, start_date: str, end_date: str):
        

        self.tournament_name = tournament_name # Tournament name
        self.tournament_type = tournament_type # Tournament type
        self.start_date = start_date # Start date
        self.end_date = end_date # End date
        self.teams = [] # List of teams
        self.is_valid = False # Validation flag
    
    def validate_input(self): #-> bool:
 
        try:
            # Validate tournament name
            if not self.tournament_name or not self.tournament_name.strip():
                return "Error: Tournament name cannot be empty"
            
            # Validate tournament type
            if not self.tournament_type or not self.tournament_type.strip():
                print("Error: Tournament type cannot be empty")
                return False
            if not self.tournament_tpe != "Knockout" or self.tournament_type != "Double Elimination":
                return "Error: Tournament type must be 'Knockout' or 'Double Elimination'"
            
            # Validate dates
            start = datetime.strptime(self.start_date, "%Y.%m.%d")
            end = datetime.strptime(self.end_date, "%Y.%m.%d")
            
            if start >= end:
                return "Error: Start date must be before end date"
            
            # Calculate day difference (number of days between start and end)
            date_diff = (end - start).days
            
            if date_diff == 3:
                self.is_valid = True # if validation passes
                return "Correct, tournament spans 3 days"

            else:
                return "Error: Tournament must span exactly 3 days, but spans over 3 days"
            
              
        except ValueError as x:
            return f"Error: Invalid date format. Use dd.mm.yyyy - {x}"
            
    


    def add_team(self, team_name: str, captain_name: str, players: list) -> bool:
        """
        Add a team to the tournament.
        
        Args:
            team_name: Name of the team
            captain_name: Name of the team captain
            players: List of player names
            
        Returns:
            bool: True if team was added successfully
        """
        if not self.is_valid:
            print("Error: Tournament must be validated before adding teams")
            return False
        
        if not team_name or not captain_name or not players:
            print("Error: Team name, captain name, and players list cannot be empty")
            return False
        
        team = {
            "name": team_name,
            "captain": captain_name,
            "players": players
        }
        self.teams.append(team)
        return True
    
    def create(self) -> dict:
        """
        Create the tournament and return the tournament data.
        This method routes the data to appropriate storage/scheduling functions.
        
        Returns:
            dict: Tournament data structure ready to be stored
        """
        if not self.is_valid:
            print("Error: Tournament data is not valid. Call validate_input() first")
            return None
        
        if len(self.teams) == 0:
            print("Error: Tournament must have at least one team")
            return None
        
        tournament_data = {
            "name": self.tournament_name,
            "type": self.tournament_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "teams": self.teams,
            "created_at": datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }
        
        # TODO: Route to data storage (e.g., save_tournament_to_file(tournament_data))
        # TODO: Route to schedule generation (e.g., generate_tournament_schedule(tournament_data))
        
        return tournament_data
    
    def create_dummy_teams(self) -> bool:

        # Might not need this
        if not self.is_valid:
            print("Error: Tournament must be validated before adding teams")
            return False
        
        # get data from dl, for Dummy data
        
        for team in dummy_teams:
            self.teams.append(team)
        # If created successfully
        print(f"Successfully created {len(dummy_teams)} dummy teams")
        return True

    
#     def get_tournament_summary(self) -> str:
#         """
#         Get a summary of the tournament data.
        
#         Returns:
#             str: Formatted tournament summary
#         """
#         if not self.is_valid:
#             return "Tournament not validated yet"
        
#         summary = f"""
# Tournament: {self.tournament_name}
# Type: {self.tournament_type}
# Start Date: {self.start_date}
# End Date: {self.end_date}
# Teams: {len(self.teams)}
# """
#         return summary





class RegisterTeam:
    """
    Helper class for managing team registration in a tournament.
    """
    
    def __init__(self, team_name: str, captain_name: str):
        """
        Initialize team registration.
        
        Args:
            team_name: Name of the team
            captain_name: Name of the team captain
        """
        self.team_name = team_name
        self.captain_name = captain_name
        self.players = []
    
    def add_player(self, player_name: str) -> bool:
        """
        Add a player to the team.
        
        Args:
            player_name: Name of the player
            
        Returns:
            bool: True if player was added
        """
        if not player_name or len(player_name.strip()) == 0:
            return False
        
        if player_name not in self.players:
            self.players.append(player_name)
            return True
        
        return False




class GenerateTournamentSchedule:
    """
    Helper class for generating tournament schedules based on tournament type.
    """
    
    def __init__(self, tournament_data: dict):
        """
        Initialize schedule generation with tournament data.
        
        Args:
            tournament_data: Dictionary containing tournament information
        """
        self.tournament_data = tournament_data
        self.schedule = []
    
    def generate(self) -> list:
        """
        Generate schedule based on tournament type.
        
        Returns:
            list: List of matches/rounds
        """
        tournament_type = self.tournament_data.get("type", "").lower()
        
        if tournament_type == "round robin":
            return self._generate_round_robin()
        elif tournament_type == "knockout":
            return self._generate_knockout()
        else:
            print(f"Unknown tournament type: {tournament_type}")
            return []
    




    def _generate_round_robin(self) -> list:
        """Generate round robin schedule."""
        teams = self.tournament_data.get("teams", [])
        schedule = []
        
        # TODO: Implement round robin logic
        # Each team plays every other team once
        
        return schedule
    



    def _generate_knockout(self) -> list:
        """Generate knockout/elimination schedule."""
        teams = self.tournament_data.get("teams", [])
        schedule = []
        
        # TODO: Implement knockout logic
        # Single elimination bracket
        
        return schedule 

