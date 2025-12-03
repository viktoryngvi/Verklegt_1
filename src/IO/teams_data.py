
from typing import List


class TeamsData:
    """
    Minimal data-layer class for loading teams from a local CSV/text file.
    """

    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath
        self.teams: List[str] = []

    def load_teams(self) -> List[str]:
        """Load team names from the local file and return them as a list."""
        self.teams = []  # reset in case loaded before

        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                name: str = line.strip()
                if name:  # ignore empty lines
                    self.teams.append(name)

        return self.teams
