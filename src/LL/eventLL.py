from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.event import Event

class EventLL:
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self.dl_wrapper = dl_wrapper
        self.validate = validate
    
    def create_empty_event(self, event: Event):
        validate_errors = self.validate.validate_event(event)
        if validate_errors:
            return validate_errors
    
    def write_team_into_event(self, event: Event):
        self.dl_wrapper.create_empty_event(event.tournament_name)
        self.dl_wrapper.write_team_into_empty_event(event.team)
        

        


        