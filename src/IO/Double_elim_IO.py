from csv import DictReader
from models.match import Match

class Double_elim_IO(Match):
    def __init__(self):
        self.file_path = "data/double_elim.csv"