import csv
import os

class TournamentScheduleIO:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save_schedule(self, tournament_name: str, event):
        """
        Saves the full schedule for a tournament into a CSV file.
        The 'event' argument is an Event model object containing a list of Match objects.
        """

        filename = f"{tournament_name}_schedule.csv"
        filepath = os.path.join(self.base_path, filename)

        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            # Header row
            writer.writerow([
                "match_id",
                "round_name",
                "team_a",
                "team_b",
                "winner",
                "score",
                "server_id",
                "schedule_time"
            ])

            # Write each match as a row
            for match in event.matches:  # event.matches is a list of Match objects
                writer.writerow([
                    match.id,
                    match.round_name,  # you should include round_name in your Match model or LL
                    match.team_a.name if match.team_a else "",
                    match.team_b.name if match.team_b else "",
                    match.winner.name if match.winner else "",
                    match.result_score if match.result_score else "",
                    match.server_id if match.server_id else "",
                    match.schedule_time if match.schedule_time else ""
                ])

        return True  # DL returns simple success confirmation
