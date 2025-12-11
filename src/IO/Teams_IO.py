from models.team import Team


class Team_IO:
    def __init__(self):
        self.file_path = "data/teams.csv"

    # def view_all_teams(self):
    #     """checks all teams and their captain and returns a list of dicts of teams""" #TODO
    #     with open (self.file_path, "r", encoding="utf-8") as teams_file:
    #         header = teams_file.readline().split(",")
    #         for row in teams_file:
    #             attributes = row.split(",")
    #             team = Team()
    #             for i in range(len(header)):
    #                 setattr(Team, header[i], attributes[i])

    #     return teams_file

    def view_all_teams(self):
        team_list = []
        with open(self.file_path, "r", encoding="utf-8") as teams_data:
            header = teams_data.readline().split(",")
            for row in teams_data:
                attributes = row.split(",")
                team = Team()
                team.id = int(attributes[0])
                team.name = str(attributes[1])
                team.captain = str(attributes[2])
                team.players = list(attributes[3].split(";"))


                team_list.append(team)
        return team_list
    
    def append_team_into_file(self, team: Team):
        players_str = ";".join(str(p) for p in team.players)
        # þetta skrifar players niður sem streng
        with open(self.file_path, "a", encoding="utf-8") as teams_file:
                teams_file.write(
                    f'{team.id},'
                    f'{team.name},'
                    f'{team.captain},'
                    f'{players_str},'
                )
        return True


    def write_team_into_file(self, teams_file):
        with open(self.file_path, "w", encoding="utf-8") as teams_file:
            teams_file.write("team,captain_handle,player_list")
            for each_dict in teams_file:
                teams_file.write(",".join(each_dict.values()))
                teams_file.write("\n")
        # skrifar það aftur í skránna
        return True
    

