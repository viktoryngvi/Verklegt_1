from IO.data_wrapper import DLWrapper
from models.event import Event
from LL.validate import Validate

class EventLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper
        self.validate = Validate(dl_wrapper)
    

    # ----------------------------------------------------------------------
    # CREATE EVENT
    # ----------------------------------------------------------------------



    def create_event(self, event : Event):
        validate_errors = self.validate.validate_event(event)

        if validate_errors:
            return validate_errors
        else:
            #return "Successfully created tournament."
            return self._dl_wrapper.create_event(event)



    # ----------------------------------------------------------------------
    # EVENT TYPES 
    # ----------------------------------------------------------------------

    def event_types(self):
        return [
            "Single Elimination",
            "Double Elimination",
            "Last Team Standing"] 
        