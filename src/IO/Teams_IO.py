from models.team import Team


class Team_IO:
    def __init__(self,):
        self.file_path = "data/teams.csv"



        # finnur réttan captain og breytir honum í capteinin
    def _write_team_into_file(self, teams_file):
        with open(self.file_path, "w", encoding="utf-8") as teams_file:
            teams_file.write("team,captain_handle,player_list")
            for each_dict in teams_file:
                teams_file.write(",".join(each_dict.values()))
                teams_file.write("\n")
        # skrifar það aftur í skránna
        return True

    def view_all_teams(self):
        """checks all teams and their captain and returns a list of dicts of teams""" #TODO
        with open (self.file_path, "r", encoding="utf-8") as teams_file:
            header = teams_file.readline().split(",")
            for row in teams_file:
                attributes = row.split(",")
                team = Team()
                for i in range(len(header)):
                    setattr(Team, header[i], attributes[i])

        return teams_file

    