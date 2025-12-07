from IO.data_wrapper import DLWrapper

class ClubLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self.dl_wrapper = dl_wrapper
    
    def load_clubs(self):
        return self.dl_wrapper.load_clubs()