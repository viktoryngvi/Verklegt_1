from models.match import Match
from IO.data_wrapper import DLWrapper

class MatchLL:
    """LOGIC LAYER CLASS FOR MATCH VALIDATION AND RESULT MANAGEMENT"""

    def __init__(self, dl_wrapper: DLWrapper):

        self._dl_wrapper = dl_wrapper

    # ----------------------------------------------------------------------
    # CHECK SCORE FORMAT
    # ----------------------------------------------------------------------

    def check_score_format(self, match: Match):
        """VALIDATES THAT THE MATCH RESULT SCORE IS IN THE FORMAT 'X-Y'"""
       
        score_str = match.result_score.strip()
        
        if "-" not in score_str:
            return "Score must be in format 'X-Y' (e.g., 2-1)."
        
        parts = score_str.split("-")
        
        if len(parts) != 2:
            return "Score must contain exactly two numbers separated by a dash."
        
        try:
            score_a = int(parts[0])
            score_b = int(parts[1])
            
        except ValueError:
            return "Score values must be integers."
            
        if score_a < 0 or score_b < 0:
            return "Scores cannot be negative."
            
        return True

    # ----------------------------------------------------------------------
    # CHECK WINNER CONSISTENCY
    # ----------------------------------------------------------------------

    def check_winner_consistency(self, match: Match):
        """VALIDATES THAT THE DECLARED WINNER MATCHES THE SCORE LOGIC"""
       
        if not match.winner:
            return "No winner declared."

        team_a_name = match.team_a.name if hasattr(match.team_a, 'name') else str(match.team_a)
        team_b_name = match.team_b.name if hasattr(match.team_b, 'name') else str(match.team_b)
        winner_name = match.winner.name if hasattr(match.winner, 'name') else str(match.winner)

        if winner_name != team_a_name and winner_name != team_b_name:
            return f"Winner ({winner_name}) is not part of this match ({team_a_name} vs {team_b_name})."

        try:
            score_a, score_b = map(int, match.result_score.split("-"))
        except ValueError:
            return "Invalid score format prevents winner validation."

        if score_a == score_b:
            return "Draws are not allowed (or winner cannot be determined by a tie)."

        if winner_name == team_a_name and score_a < score_b:
            return f"Winner is set to {team_a_name}, but score favors {team_b_name}."
        
        if winner_name == team_b_name and score_b < score_a:
            return f"Winner is set to {team_b_name}, but score favors {team_a_name}."

        return True

    # ----------------------------------------------------------------------
    # VALIDATE MATCH
    # ----------------------------------------------------------------------

    def validate_match(self, match: Match):
        """AGGREGATES MATCH VALIDATION CHECKS AND RETURNS ERRORS OR NONE"""
        errors = []

        check_score = self.check_score_format(match)
        check_winner = self.check_winner_consistency(match)
        
        if check_score is not True:
            errors.append(f"Score: {check_score}")
        
        if check_score is True and check_winner is not True:
            errors.append(f"Winner: {check_winner}")

        if errors:
            return errors
        
        return None

    # ----------------------------------------------------------------------
    # ENTER MATCH RESULT
    # ----------------------------------------------------------------------

    def enter_match_result(self, match: Match):
        """VALIDATES AND SAVES MATCH RESULT USING DLWrapper"""
        validation_errors = self.validate_match(match)
        
        if validation_errors:
            return validation_errors

        try:
            return self._dl_wrapper.save_match_result(match)
        except Exception as e:
            return [f"Database Error: {str(e)}"]

    # ----------------------------------------------------------------------
    # GET UNFINISHED MATCHES
    # ----------------------------------------------------------------------

    def get_unfinished_matches(self, event_name, tournament_name ):
        list_of_unfinished_matches = self._dl_wrapper.get_unfinished_matches()