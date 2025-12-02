class OrganizerUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        print("\n==== Organizer Menu ====")
        print("1. Create tournament")
        print("2. Generate schedule")
        print("3. Enter match result")
        print("4. Change team captain")
        print("5. View statistics")
        print("6. View schedule")
        print("b. Back to main menu")

        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "5", "6", "b"])

        if choice == "1": 
            self.create_tournament(); 
            return "ORGANIZER_MENU"
        if choice == "2": 
            self.generate_schedule(); 
            return "ORGANIZER_MENU"
        if choice == "3": 
            self.enter_match_result(); 
            return "ORGANIZER_MENU"
        if choice == "4": 
            self.change_team_captain(); 
            return "ORGANIZER_MENU"
        if choice == "5": 
            self.view_statistics(); 
            return "ORGANIZER_MENU"
        if choice == "6": 
            self.view_schedule(); 
            return "ORGANIZER_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def create_tournament(self): 
        print("TODO")
    def generate_schedule(self): 
        print("TODO")
    def enter_match_result(self): 
        print("TODO")
    def change_team_captain(self): 
        print("TODO")
    def view_statistics(self): 
        print("TODO")
    def view_schedule(self): 
        print("TODO")
