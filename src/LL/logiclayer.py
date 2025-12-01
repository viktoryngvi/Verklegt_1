from LL.logical_wraper import LLWrapper

class MatchLL:
    def enter_match_result(team_a_score: int, team_b_score: int):
        if team_a_score < 0 and team_b_score < 0:
            return False
        
        return f"{team_a_score} - {team_b_score}"

class TeamLL:
    def change_team_captain():
        pass

    def edit_player():
        pass

class PlayerLL:
    def edit_player(id):
        pass 

    def create_player(player):
        pass

