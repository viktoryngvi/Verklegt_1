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
        
        return self.dl_wrapper.create_empty_event(event)
        

    def write_team_into_event(self, event: Event, team):
        
        if self.dl_wrapper.check_if_name_event_exists(event.name):
            return "Event name does not exists"

        if not self.dl_wrapper.check_if_team_name_exists(team):
            return "Team Does not exists"
        
        if self.dl_wrapper.check_if_team_in_event(team):
            return "Team already in event"
        
        return self.dl_wrapper.write_team_into_empty_event(event.name, team)
        

        


        