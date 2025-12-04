class TeamLL:
    def __init__(self, dl_wrapper):
        self._dl_wrapper = dl_wrapper

    # ----------------------------------------------------------------------
    # CHANGE TEAM CAPTAIN
    # ----------------------------------------------------------------------
    def change_captain(self, team_name: str, new_captain: str) -> str:
        """
        Change the captain of a team.

        Args:
            team_name: Name of the team
            new_captain: Name of the new captain

        Returns:
            str: Success or error message
        """

        # Fetch current team data from data layer
        team_data = self._dl_wrapper.get_team(team_name)
        if not team_data:
            return "Error: Team not found"

        current_captain = team_data.get("captain")
        players = team_data.get("players", [])

        # Check if new captain is part of the team
        if new_captain not in players:
            return "Error: New captain is not a member of the team"

        # Update captain in data source
        updated = self._dl_wrapper.update_captain(team_name, new_captain)
        if updated:
            return "Success: Captain changed successfully"
        else:
            return "Error: Failed to change captain"

    # ----------------------------------------------------------------------
    # EDIT PLAYER
    # ----------------------------------------------------------------------
    def edit_player(self, team_name: str, player_name: str, new_data: dict) -> str:
        """
        Edit a player's information within a team.

        Args:
            team_name: Name of the team
            player_name: Name of the player to edit
            new_data: Dictionary containing fields to update (e.g., {"phone": "123-4567"})

        Returns:
            str: Success or error message
        """

        # Fetch current team data
        team_data = self._dl_wrapper.get_team(team_name)
        if not team_data:
            return "Error: Team not found"

        players = team_data.get("players", [])

        # Check if player exists in the team
        if player_name not in players:
            return "Error: Player not found in the team"

        # TODO: Validate new_data fields if needed

        # Update player info in data layer
        updated = self._dl_wrapper.update_player(team_name, player_name, new_data)
        if updated:
            return "Success: Player information updated"
        else:
            return "Error: Failed to update player"
