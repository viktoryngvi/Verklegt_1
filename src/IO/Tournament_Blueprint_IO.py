from csv import DictReader
# from models.tournament import Tournament

class Tournament_Blueprint_IO:
    def __init__(self, team_amount= None, ):
        self.file_path = "data/tournament_blueprint.csv"
        self.team_amount = team_amount
    
    def create_empty_blueprint(self, team_amount):
        with open(self.file_path, "w", encoding="utf-8"):
            pass
