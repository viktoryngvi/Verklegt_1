from csv import DictReader
from IO.Event_IO_test import Event_IO_test

class Actual_event(Event_IO_test):
    def __init__(self):
        self.get_event_file = "data/event_blueprint.csv"
        self.file_path = "data/event.csv"
    
    def move_blueprint_to_public(self):
        """should take the illed event_blueprint and make a knockout schedule in the event file for that"""
        with open(self.get_event_file, "r", encoding="utf-8") as old_event_file:
            csv_reader = DictReader(old_event_file)
            old_event_file = list(csv_reader)
        
        with open(self.file_path, "w", encoding="utf-8") as event_file:
            event_file.write()##allllllllllllllllt sem á að vera lykill efst í fælinum
            for every_line in old_event_file:
                event_file.write(",".join(every_line.values()))
                event_file.write("\n")
        return "Event is now public"
    # TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

