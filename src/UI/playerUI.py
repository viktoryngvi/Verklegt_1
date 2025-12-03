class PlayerUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        print("\n==== Player Menu ====")
        print("1. View profile")
        print("2. Edit my info")
        print("3. View team")
        print("4. View schedule")
        print("b. Back to main menu")

        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "b"])

        if choice == "1": 
            self.show_profile(); 
            return "PLAYER_MENU"
        if choice == "2": 
            self.edit_player(); 
            return "PLAYER_MENU"
        if choice == "3": 
            self.view_team(); 
            return "PLAYER_MENU"
        if choice == "4": 
            self.view_schedule(); 
            return "PLAYER_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def show_profile(self):
        print("TODO")
    def edit_player(self): 
        print("TODO")
    def view_team(self): 
        print("TODO")
    def view_schedule(self): 
        print("TODO")
