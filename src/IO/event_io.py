
# models/event.py

from models.match import Match

class Event:
    def __init__(self, name: str, game_type: str):
        self.name = name
        self.game_type = game_type
        self.matches = []

    def add_match(self, match: Match):
        """Add a match to the event."""
        self.matches.append(match)

    def get_match_by_id(self, match_id: int):
        """Return one match by ID."""
        for m in self.matches:
            if m.id == match_id:
                return m
        return None

    def get_played_matches(self):
        """Matches that have a winner or a score."""
        played = []
        for m in self.matches:
            if m.winner is not None or m.result_score not in ("", None):
                played.append(m)
        return played

    def get_unplayed_matches(self):
        """Matches that do not have results yet."""
        unplayed = []
        for m in self.matches:
            if m.winner is None and m.result_score in ("", None):
                unplayed.append(m)
        return unplayed
