from datetime import datetime
from models.tournament import Tournament
from models.team import Team
from IO.data_wrapper import DLWrapper
from LL.validate import Validate


class TournamentLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper
        self.validator = Validate(dl_wrapper)

    def create_tournament(self, tournament: Tournament):
        validate_errors = self.validator.validate_tournament(tournament)


        if validate_errors:
            return validate_errors
        else:
            #return "Successfully created tournament."
            return self.create_tournament_to_data(tournament)
        
    
    def create_tournament_to_data(self, tournament: Tournament):
        """tournaments should have a list of tournaments that have event names"""
        id = self.get_next_tournament_id()
        tournament_file = self._dl_wrapper.read_tournament_file()
        if self.validator.validate_tournament(tournament):
            return self.validator.validate_tournament(tournament)
        Tournament.tournament_id = id
        tournament_file.append(tournament)

        return self._dl_wrapper.write_into_file(tournament_file)
         
# --------------------------------------------------------------------------
# GET_TOURNAMENT_LIST 
# --------------------------------------------------------------------------
    def get_tournament_list(self):
        return self.view_tournaments()


    def get_events_in_tournament(self, tournament_name):
        return self.view_events_in_tournament(tournament_name)

        #     tournament_file.write(f"{id},{tournament.name},{tournament.location},{tournament.start_date},{tournament.end_date},event_list\n")
        # return "Tournament created!"


    def put_event_into_tournament(self, tournament_name, event_name, tournament: Tournament):
        tournament_file = self._dl_wrapper.read_tournament_file()
        for line in tournament_file:
            if tournament.name == tournament_name:
                if line["event_list"] == "event_list":
                    line["event_list"] = []
                    line["event_list"].append(event_name)
                    if self._dl_wrapper.write_into_file(tournament_file):
                        return "Done!"
                else:
                    line["event_list"].append(event_name)
                    if self._dl_wrapper.write_into_file(tournament_name):
                        return "Done!"
                 
        return "Tournament does not exist."


    def view_tournaments(self):
        tournament_file = self._()
        list_of_tournaments = []
        for line in tournament_file:
            list_of_tournaments.append(line["tournament_name"])
        return list_of_tournaments

    def view_events_in_tournament(self, tournament_name):
        tournament_file = self._dl_wrapper.read_tournament_file()
        for line in tournament_file:
            if line["tournament_name"] == tournament_name:
                return line["event_list"]
        return "No tournament with this name"
    
    def get_next_tournament_id(self):
        """checks the last player and returns the id of said player"""
        tournament_data = self._dl_wrapper.read_tournament_file()
        if not tournament_data:
            next_useable_id = 1
        else:
            next_useable_id = int(tournament_data[-1]["id"])
            next_useable_id += 1
        return next_useable_id
