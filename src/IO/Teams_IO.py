from models.team import Team


class Team_IO:
    """HANDLES READING, CREATING AND EDITING TEAM INFORMATION IN CSV FILE"""


    def __init__(self):
        self.file_path = "data/teams.csv"

    # ----------------------------------------------------------------------
    # VIEW ALL TEAMS
    # ----------------------------------------------------------------------

    def view_all_teams(self):
        """LOADS ALL TEAMS FROM TEAM CSV FILE AND RETURNS THEM AS A LIST"""

    
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
    
    # ----------------------------------------------------------------------
    # APPEND TEAM INTO FILE 
    # ----------------------------------------------------------------------

    def append_team_into_file(self, team: Team):
        """APPENDS A NEW TEAM AND SAVES IT INTO THE TEAM FILE"""

    
        players_str = ";".join(str(p) for p in team.players)
        # þetta skrifar players niður sem streng
    
        with open(self.file_path, "a", encoding="utf-8") as teams_file:
                teams_file.write(
                    f'{team.id},'
                    f'{team.name},'
                    f'{team.captain},'
                    f'{players_str},'
                    f'\n'
                )
    
        return True   

    # ----------------------------------------------------------------------
    # EDIT TEAM FILE 
    # ----------------------------------------------------------------------

    def edit_teams_file(self, teams: list[Team]):
        """OVERWRITES TEAM FILE WITH UPDATED TEAM INFORMATION"""

   
        with open(self.file_path, "w", encoding="utf-8") as teams_file:
   
            teams_file.write("id,team,captain_handle,player_list\n")
   
            for team in teams:
                players_str = ";".join(str(t) for t in team.players)
                teams_file.write(
                    f'{team.id},'
                    f'{team.name},'
                    f'{team.captain},'
                    f'{players_str},'
                    f'\n'
                )
   
        return "team has been edited"



