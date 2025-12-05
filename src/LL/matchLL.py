from models.match import Match
from IO.data_wrapper import DLWrapper

class MatchLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper

    def check_score_format(self, match: Match):
        """
        Validates that the result_score is in the format 'Int-Int'.
        """
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

    def check_winner_consistency(self, match: Match):
        """
        Validates that the declared winner matches the logic of the scores
        and that the winner is actually one of the participating teams.
        """
        # If no winner is set yet, we cannot validate consistency
        if not match.winner:
            return "No winner declared."

        # Check if winner is one of the participants
        # Assuming Team objects are compared by name or ID
        team_a_name = match.team_a.name if hasattr(match.team_a, 'name') else str(match.team_a)
        team_b_name = match.team_b.name if hasattr(match.team_b, 'name') else str(match.team_b)
        winner_name = match.winner.name if hasattr(match.winner, 'name') else str(match.winner)

        if winner_name != team_a_name and winner_name != team_b_name:
            return f"Winner ({winner_name}) is not part of this match ({team_a_name} vs {team_b_name})."

        # Parse scores to ensure the winner actually has the higher score
        try:
            score_a, score_b = map(int, match.result_score.split("-"))
        except:
            return "Invalid score format prevents winner validation."

        if score_a == score_b:
            return "Draws are not allowed (or winner cannot be determined by a tie)."

        if winner_name == team_a_name and score_a < score_b:
            return f"Winner is set to {team_a_name}, but score favors {team_b_name}."
        
        if winner_name == team_b_name and score_b < score_a:
            return f"Winner is set to {team_b_name}, but score favors {team_a_name}."

        return True

    def validate_match(self, match: Match):
        """
        Aggregates validation checks.
        Returns a LIST of errors if invalid, or None if valid.
        """
        errors = []

        check_score = self.check_score_format(match)
        check_winner = self.check_winner_consistency(match)
        
        if check_score is not True:
            errors.append(f"Score: {check_score}")
        
        # Only check winner logic if the score format was valid
        if check_score is True and check_winner is not True:
            errors.append(f"Winner: {check_winner}")

        if errors:
            return errors
        
        return None

    def enter_match_result(self, match: Match):
        """
        Validates the match result and sends it to the DLWrapper to be saved.
        """
        # 1. Validate data
        validation_errors = self.validate_match(match)
        
        if validation_errors:
            return validation_errors

        # 2. Check if match ID exists (Optional, depending on your logic)
        # if not self._dl_wrapper.check_if_match_exists(match.id):
        #     return ["Match ID not found."]

        # 3. Save to Data Layer
        # Note: You need to implement save_match_result in your DLWrapper
        try:
            return  self._dl_wrapper.save_match_result(match)
        except Exception as e:
            return [f"Database Error: {str(e)}"]