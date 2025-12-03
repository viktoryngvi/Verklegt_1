class SpectatorUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        print("\n==== Spectator Menu ====")
        print("1. View schedule")
        print("2. View teams")
        print("3. View players")
        print("4. View clubs")
        print("b. Back to main menu")

        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "b"])

        if choice == "1": 
            self.view_schedule(); 
            return "SPECTATOR_MENU"
        if choice == "2": 
            self.view_teams(); 
            return "SPECTATOR_MENU"
        if choice == "3": 
            self.view_players(); 
            return "SPECTATOR_MENU"
        if choice == "4": 
            self.view_clubs(); 
            return "SPECTATOR_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def view_schedule(self): 
        print("TODO")
    def view_teams(self): 
        print("TODO")
    def view_players(self): 
        print("TODO")
    def view_clubs(self): 
        print("TODO")


        


