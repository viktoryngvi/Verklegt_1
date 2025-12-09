from IO.data_wrapper import DLWrapper
from LL.validate import Validate
from models.event import Event

class EventLL:
    def __init__(self, dl_wrapper: DLWrapper, validate: Validate):
        self.dl_wrapper = dl_wrapper
        self.validate = validate
    
    def create_event(self, tournament_name, event: Event):
        validate_errors = self.validate.validate_event(event)
        if validate_errors:
            return validate_errors
        
        
        
        return self.dl_wrapper.create_event(tournament_name, event)


        