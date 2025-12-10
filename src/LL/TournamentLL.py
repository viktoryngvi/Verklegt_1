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
        validate_errors = self.validate_tournament(tournament)


        if validate_errors:
            return validate_errors
        else:
            #return "Successfully created tournament."
            return self._dl_wrapper.create_tournament(tournament)


    # ----------------------------------------------------------------------
    # VALIDATE TOURNAMENT 
    # ----------------------------------------------------------------------

    def validate_tournament(self, tournament: Tournament):
        errors = []

        check_name = self.check_tournament_name(tournament)
        #check_type = self.check_tournament_type(tournament.type)
        check_dates = self.check_dates(tournament)
        check_contact_name = self.check_contact_name(tournament)
        check_contact_email = self.check_contact_email(tournament)
        check_contact_phone = self.check_contact_phone(tournament)

        if check_name is not True:
            errors.append(f"Name: {check_name}")

        # if check_type is not True:
        #     errors.append(f"Type: {check_type}")

        if check_dates is not True:
            errors.append(f"Dates: {check_dates}")

        return errors if errors else None


    # ----------------------------------------------------------------------    
     # tournament name validation
    # ----------------------------------------------------------------------
    
    def check_tournament_name(self, tournament: Tournament):
        tournament_name = tournament.name.strip()

        if len(tournament_name) == 0:
            return "Tournament name cannot be empty."

        if len(tournament_name) < 3 or len(tournament_name) > 60:
            return "Tournament name must be between 3–60 characters."

        return True


# ----------------------------------------------------------------------
 # tournament type validation
# ----------------------------------------------------------------------


    # def check_tournament_type(self, tournament_type: str):
    #     tournament_type_stripped = tournament_type.strip()

    #     allowed_names = ["Knockout", "Double Elimination"]

    #     if self.tournament_type not in allowed_names:
    #         return "Tournament type must be 'Knockout' or 'Double Elimination'."

    #     return True


    # ----------------------------------------------------------------------
     # date validation
    # ----------------------------------------------------------------------

    def check_dates(self, tournament: Tournament):
        try:
            self.start = datetime.strptime(tournament.start_date, "%Y-%m-%d")
            self.end = datetime.strptime(tournament.end_date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use yyyy-mm-dd"

        if self.start >= self.end:
            return "Start date must be before end date."

        if (self.end - self.start).days < 4:
            return "Tournament must span more then 4 days."

        return True


    
# --------------------------------------------------------------------------
# VALIDATE CONTACT NAME
# --------------------------------------------------------------------------   

    def check_contact_name(self, tournament: Tournament):
        check_contact_name = tournament.contact_name.strip()

        if len(check_contact_name) == 0:
            return "Contact name cannot be empty."

        if len(check_contact_name) < 3:
            return "Contact name must be at least 3 characters."

        return True

# --------------------------------------------------------------------------
# VALIDATE CONTACT EMAIL
# --------------------------------------------------------------------------  
    def check_contact_email(self, tournament: Tournament):
        check_contact_email = tournament.contact_email.strip()

        result = self.validator.validate_email(check_contact_email)

        if result is not None:
            return f"Invalid email: {result}"

        return True
    

# --------------------------------------------------------------------------
# VALIDATE CONTACT PHONE
# --------------------------------------------------------------------------  
    def check_contact_phone(self, tournament: Tournament):
        check_contact_phone = tournament.contact_email.strip()

        result = self.validator.validate_phone(check_contact_phone)

        if result is not None:
            return f"Invalid phone: {result}"

        return True
    
# --------------------------------------------------------------------------
# GET_TOURNAMENT_LIST 
# --------------------------------------------------------------------------
    def get_tournament_list(self):
        return self.view_tournaments()


    def get_events_in_tournament(self, tournament_name):
        return self.view_events_in_tournament(tournament_name)

    def create_tournament(self, tournament: Tournament):
        """tournaments should have a list of tournaments that have event names"""
        id = self.get_next_tournament_id()
        tournament_file = self._dl_wrapper.read_tournament_file()
        if self.validate_tournament(tournament):
            return self.validate_tournament(tournament)
        Tournament.tournament_id = id
        tournament_file.append(tournament)

        return self._dl_wrapper.write_into_file(tournament_file)
         
        #     tournament_file.write(f"{id},{tournament.name},{tournament.location},{tournament.start_date},{tournament.end_date},event_list\n")
        # return "Tournament created!"


    def put_event_into_tournament(self, tournament_name, event_name):
        tournament_file = self._dl_wrapper.read_tournament_file()
        for line in tournament_file:
            if line["tournament_name"] == tournament_name:
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






# --------------------------------------------------------------------------
# TEAM REGISTRATION CLASS 
# --------------------------------------------------------------------------

class RegisterTeam:
    """
    Helper class for managing team registration in a tournament.
    """

    def __init__(self, team_name: str, captain_name: str):
        self.team_name = team_name
        self.captain_name = captain_name
        self.players = []

    def add_player(self, player_name: str):
        if player_name in self.players:
            return "Player is already in the team."

        self.players.append(player_name)
        return True


# --------------------------------------------------------------------------
# SCHEDULING CLASS 
# --------------------------------------------------------------------------

class GenerateTournamentSchedule:
    """
    Helper class for generating tournament schedules.
    """

    def __init__(self, tournament_data: dict):
        self.tournament_data = tournament_data
        self.schedule = []

    def generate(self):
        tournament_type = self.tournament_data.get("type", "").lower()

        if tournament_type == "round robin":
            return self._round_robin()

        if tournament_type == "knockout":
            return self._knockout()

        return []

    # TODO: Implement these properly
    def _round_robin(self):
        teams = self.tournament_data.get("teams", [])
        schedule = []
        # Each team plays every other team once → TODO
        return schedule

    def _knockout(self):
        teams = self.tournament_data.get("teams", [])
        schedule = []
        # Single-elimination bracket → TODO
        return schedule

