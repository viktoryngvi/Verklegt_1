class change_team_captain:
    
    def __init__(self, team_name: str, new_captain: str):
        self.team_name = team_name
        self.new_captain = new_captain
        self.current_captain = # Fetch current captain from data source 
    def change_captain(self) -> str:

        # Check if team name is valid
        if not self.team_name in #list_of_teams#:
            return "Error: Team not found"
        else:
            return True
        
        # Check if new captain is part of the team
        if not self.new_captain in #Get names of player in team:
            return "Error: New captain is not a member of the team"
        else:
            return True
        
        # Update captain in data source
        if self.team_name and self.new_captain:
            # Perform the update operation here
            self.current_captain = self.new_captain
            return "Success: Captain changed successfully"
        else:
            return "Error: Failed to change captain"

           


    