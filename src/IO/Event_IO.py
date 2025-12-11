from csv import DictReader
from models.match import Match
from models.event_blueprint import Event_blueprint

class Event_(Match, Event_blueprint):
    def __init__(self):
        self.blueprint_file = "data/event_blueprint.csv"
        self.match_file = "data/match.csv"
        self.public_event_file = "data/puclic_event.csv"
        self.results_file = "data/results.csv"



    def load_event_blueprint(self):
        event_list = []
        with open(self.blueprint_file, "r", encoding="utf-8") as blueprint_file:
            headers = blueprint_file.readline().split(",")
            for row in blueprint_file:
                attributes = row.split(",")
                blueprint = Event_blueprint()
                blueprint.id = str(attributes[0])
                blueprint.team_name = str(attributes[1])
                blueprint.event_type = str(attributes[2])
                blueprint.tournament_name = str(attributes[3])
                blueprint.start_date = int(attributes[4])
                blueprint.end_date = int(attributes[5])
                event_list.append(blueprint)
        return event_list


    def append_into_blueprint_file(self, event_blueprint: Event_blueprint):
        with open(self.blueprint_file, "a", encoding="utf-8") as blueprint_file:
            blueprint_file.write(
                f'{event_blueprint.id},'
                f'{event_blueprint.team_name},'
                f'{event_blueprint.event_type},'
                f'{event_blueprint.tournament_name},'
                f'{event_blueprint.start_date},'
                f'{event_blueprint.end_date},'
                f'\n'
                )
        return "Match has been added to file"



    def load_knockout_file(self):
        knockout_list = []
        with open(self.match_file, "r", encoding="utf-8") as match_file:
            headers = match_file.readline().split(",")
            for row in match_file:
                attributes = row.split(",")
                match = Match
                match.tournament_name = str(attributes[0])
                match.event_name = str(attributes[1])
                match.game_type = str(attributes[2])
                match.server_id = str(attributes[3])
                match.match_id = int(attributes[4])
                match.bracket_nr = int(attributes[5])
                match.date_of_match = str(attributes[6])
                match.time_of_match = str(attributes[7])
                match.teams = list(attributes[8])
                match.team_a = str(attributes[9])
                match.team_b = int(attributes[10])
                match.team_a_score = str(attributes[11])
                match.team_b_score = str(attributes[12])
                match.winner = str(attributes[13])
                knockout_list.append(match)
        return knockout_list
    

    def append_to_match_file(self, match: Match):
        with open(self.match_file, "a", encoding="utf-8") as match_file:
            match_file.write(
                    f'{match.tournament_name},'
                    f'{match.event_name},'
                    f'{match.game_type},'
                    f'{match.server_id},'
                    f'{match.match_id},'
                    f'{match.bracket_nr},'
                    f'{match.date_of_match},'
                    f'{match.time_of_match},'
                    f'{match.teams},'
                    f'{match.team_a},'
                    f'{match.team_b},'
                    f'{match.team_a_score},'
                    f'{match.team_b_score},'
                    f'{match.winner},'
                    f'\n'
                )
        return "Match has been added to file"
    
    def edit_match_file(self, matches: list[Match]):
        with open(self.match_file, "w", encoding="utf-8") as match_file:
            match_file.write("tournament,event_name,game_type,server_id,match_id,date_of_match,time_of_match,teams,team_a,team_b,team_a_score,team_b_score,winner\n")
            for match in matches:
                match_file.write(
                    f'{match.tournament_name},'
                    f'{match.event_name},'
                    f'{match.game_type},'
                    f'{match.server_id},'
                    f'{match.match_id},'
                    f'{match.bracket_nr},'
                    f'{match.date_of_match},'
                    f'{match.time_of_match},'
                    f'{match.teams},'
                    f'{match.team_a},'
                    f'{match.team_b},'
                    f'{match.team_a_score},'
                    f'{match.team_b_score},'
                    f'{match.winner},'
                    f'\n'
                )
        return "Match has been edited"

    def read_results_file(self):
        results_list = []
        with open(self.results_file, "r", encoding="utf-8") as results_file:
            headers = results_file.readline().split(",")
            for row in results_file:
                attributes = row.split(",")
                match = Match
                match.tournament_name = str(attributes[0])
                match.event_name = str(attributes[1])
                match.game_type = str(attributes[2])
                match.server_id = str(attributes[3])
                match.match_id = int(attributes[4])
                match.bracket_nr = int(attributes[5])
                match.date_of_match = str(attributes[6])
                match.time_of_match = str(attributes[7])
                match.teams = list(attributes[8])
                match.team_a = str(attributes[9])
                match.team_b = int(attributes[10])
                match.team_a_score = str(attributes[11])
                match.team_b_score = str(attributes[12])
                match.winner = str(attributes[13])
                results_list.append(match)
        return results_list
            
    def append_into_results(self, matches_to_append: list[Match]):
        with open(self.match_file, "a", encoding="utf-8") as results_file:
            for line in matches_to_append:
                teams_str = ";".join(str(t) for t in match.teams)
                results_file.write(
                        f'{match.tournament_name},'
                        f'{match.event_name},'
                        f'{match.game_type},'
                        f'{match.server_id},'
                        f'{match.match_id},'
                        f'{match.bracket_nr},'
                        f'{match.date_of_match},'
                        f'{match.time_of_match},'
                        f'{match.teams_str},'
                        f'{match.team_a},'
                        f'{match.team_b},'
                        f'{match.team_a_score},'
                        f'{match.team_b_score},'
                        f'{match.winner},'
                        f'\n'
                    )
            return "Match has been added to file"

            # það þarf ekki að vera edit results function af því við
            # erum aldrei að breyta leikjum sem eru liðnir

