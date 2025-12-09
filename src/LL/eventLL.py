from IO.data_wrapper import DLWrapper
from models.event import Event

class EventLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self.dl_wrapper = dl_wrapper
    
    def create_event(self, event: Event):
        self.validate.check_name_of_event(event.name)
        