from models.match import Match
from IO.data_wrapper import DLWrapper

class MatchLL:
    def __init__(self, dl_wrapper: DLWrapper):
        self._dl_wrapper = dl_wrapper

    def enter_match_result(self, match: Match):
        