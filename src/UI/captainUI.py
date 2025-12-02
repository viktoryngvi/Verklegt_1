class CaptainUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        print("\n==== Captain Menu ====")
        print("1. Create player")
        print("2. Edit player info")
        print("3. View team")
        print("4. Change team captain")
        print("5. View schedule")
        print("b. Back to main menu")

        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "5", "b"])

        if choice == "1": 
            self.create_player(); 
            return "CAPTAIN_MENU"
        if choice == "2": 
            self.edit_player_info(); 
            return "CAPTAIN_MENU"
        if choice == "3": 
            self.view_team(); 
            return "CAPTAIN_MENU"
        if choice == "4": 
            self.change_team_captain(); 
            return "CAPTAIN_MENU"
        if choice == "5": 
            self.view_schedule(); 
            return "CAPTAIN_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def create_player(self): 
        print("TODO")
    def edit_player_info(self): 
        print("TODO")
    def view_team(self): 
        print("TODO")
    def change_team_captain(self): 
        print("TODO")
    def view_schedule(self): 
        print("TODO")
