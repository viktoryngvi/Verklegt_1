# Import Data inputs from ui  



class create_tournament: 
    def __init__(self, create_tournament:str , tournament_list:list, tournament_type:str, start_date:str, end_date:str):
        self.create_tournament = create_tournament
        self.tournament_list = tournament_list
        self.tournament_type = tournament_type
        self.start_date = start_date
        self.end_date = end_date


        

class register_team: 
    def __init__(self, register_team_names:list, register_captain:str, register_player:str):
        self.register_team_names = register_team_names
        self.register_captain = register_captain
        self.register_player = register_player

class generate_tournament_schedule: # Sækja, teams, start/end Date, Tournament type
    def __init__(self, tournament_schedule:str, register_teams:list, start_date:str, end_date:str):
        self.tournament_schedule = tournament_schedule 
        self.registered_teams = register_teams # Sækja gögnin frá registered teams, 
        self.start_date = start_date
        self.end_date = end_date 

