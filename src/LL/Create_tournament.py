from datetime import datetime


class CreateTournament:
    """
    Logic layer class that handles tournament creation.
    Takes input data and routes it to the appropriate data storage and scheduling functions.
    """
    
    def __init__(self, tournament_name: str, tournament_type: str, start_date: str, end_date: str):
        """
        Initialize tournament creation with basic information.
        
        Args:
            tournament_name: Name of the tournament
            tournament_type: Type of tournament (e.g., "Round Robin", "Knockout", etc.)
            start_date: Tournament start date (format: "dd.mm.yyyy")
            end_date: Tournament end date (format: "dd.mm.yyyy")
        """
        self.tournament_name = tournament_name
        self.tournament_type = tournament_type
        self.start_date = start_date
        self.end_date = end_date
        self.teams = []
        self.is_valid = False
    
    def validate_input(self) -> bool:
        """
        Validate tournament input data.
        
        Returns:
            bool: True if all data is valid, False otherwise
        """
        try:
            # Validate tournament name
            if not self.tournament_name or len(self.tournament_name.strip()) == 0:
                print("Error: Tournament name cannot be empty")
                return False
            
            # Validate tournament type
            if not self.tournament_type or len(self.tournament_type.strip()) == 0:
                print("Error: Tournament type cannot be empty")
                return False
            
            # Validate dates
            start = datetime.strptime(self.start_date, "%d.%m.%Y")
            end = datetime.strptime(self.end_date, "%d.%m.%Y")
            
            if start >= end:
                print("Error: Start date must be before end date")
                return False
            
            self.is_valid = True
            return True
        
        except ValueError as e:
            print(f"Error: Invalid date format. Use dd.mm.yyyy - {e}")
            return False
    
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
    
    def get_tournament_summary(self) -> str:
        """
        Get a summary of the tournament data.
        
        Returns:
            str: Formatted tournament summary
        """
        if not self.is_valid:
            return "Tournament not validated yet"
        
        summary = f"""
Tournament: {self.tournament_name}
Type: {self.tournament_type}
Start Date: {self.start_date}
End Date: {self.end_date}
Teams: {len(self.teams)}
"""
        return summary


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

