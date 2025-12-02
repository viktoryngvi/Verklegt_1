class MatchLL:
    def __init__(self):
        pass

    def enter_match_result(self, team_a_score: int, team_b_score: int):
        if team_a_score < 0 and team_b_score < 0:
            return False
        
        return f"{team_a_score}{team_b_score}"