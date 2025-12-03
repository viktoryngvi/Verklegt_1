from datetime import datetime
from typing import Any, Dict, List, Optional


class MatchResult:
    """Logic-layer representation of a single match's result.

    Responsibilities:
    - Store teams, scores, date/time and match metadata
    - Provide validation and convenience methods (winner, is_draw)
    - Track events that happened during the match (goals, cards, subs)
    - Serialize/deserialize to a plain dict for IO layer
    """

    def __init__(
        self,
        team_a: str,
        team_b: str,
        score_a: int = None,
        score_b: int = None,
        match_date: str = None,
        round_name: str = None,
        match_id: str = None,
    ):
        self.match_id = match_id or f"{team_a}_vs_{team_b}_{int(datetime.now().timestamp())}"
        self.team_a = team_a
        self.team_b = team_b
        self.score_a = score_a if score_a is not None else 0
        self.score_b = score_b if score_b is not None else 0
        # Expect date as dd.mm.yyyy or ISO string - keep raw but validate if needed
        self.match_date = match_date or datetime.now().strftime("%d.%m.%Y %H:%M")
        self.round_name = round_name
        # events: list of dicts, e.g. {"minute": 23, "type": "goal", "team": "A", "player": "Alice"}
        self.events: List[Dict[str, Any]] = []
        self.status = "finished" if (score_a is not None and score_b is not None) else "scheduled"

    # --- Validation ---
    def validate_teams(self) -> bool:
        if not self.team_a or not self.team_b:
            return False
        if self.team_a == self.team_b:
            return False
        return True

    def validate_scores(self) -> bool:
        try:
            if not isinstance(self.score_a, int) or not isinstance(self.score_b, int):
                return False
            if self.score_a < 0 or self.score_b < 0:
                return False
        except Exception:
            return False
        return True

    def validate_date(self) -> bool:
        # Accepts either dd.mm.yyyy or dd.mm.yyyy HH:MM
        for fmt in ("%d.%m.%Y %H:%M", "%d.%m.%Y"):
            try:
                datetime.strptime(self.match_date, fmt)
                return True
            except Exception:
                continue
        return False

    def validate_all(self) -> bool:
        return self.validate_teams() and self.validate_scores() and self.validate_date()

    # --- Helpers ---
    def winner(self) -> Optional[str]:
        if not self.validate_scores():
            return None
        if self.score_a > self.score_b:
            return self.team_a
        if self.score_b > self.score_a:
            return self.team_b
        return None

    def is_draw(self) -> bool:
        return self.score_a == self.score_b

    def set_score(self, score_a: int, score_b: int) -> None:
        self.score_a = int(score_a)
        self.score_b = int(score_b)
        self.status = "finished"

    # --- Events ---
    def add_event(self, minute: int, ev_type: str, team: str, player: Optional[str] = None, note: Optional[str] = None) -> None:
        """Add a match event.

        ev_type examples: "goal", "yellow_card", "red_card", "substitution"
        team: either the exact team name (recommended) or "A"/"B" if you prefer compact encoding
        """
        event = {"minute": minute, "type": ev_type, "team": team}
        if player:
            event["player"] = player
        if note:
            event["note"] = note
        self.events.append(event)

    # --- Serialization ---
    def to_dict(self) -> Dict[str, Any]:
        return {
            "match_id": self.match_id,
            "team_a": self.team_a,
            "team_b": self.team_b,
            "score_a": self.score_a,
            "score_b": self.score_b,
            "match_date": self.match_date,
            "round_name": self.round_name,
            "events": list(self.events),
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatchResult":
        mr = cls(
            team_a=data.get("team_a"),
            team_b=data.get("team_b"),
            score_a=int(data.get("score_a", 0)),
            score_b=int(data.get("score_b", 0)),
            match_date=data.get("match_date"),
            round_name=data.get("round_name"),
            match_id=data.get("match_id"),
        )
        mr.events = data.get("events", [])
        mr.status = data.get("status", mr.status)
        return mr

    # --- Representation ---
    def __repr__(self) -> str:
        return f"<MatchResult {self.team_a} {self.score_a} - {self.score_b} {self.team_b} ({self.match_date})>"

    