from UI.shared_ui_helpers import view_teams
from UI.shared_ui_helpers import view_schedule
from UI.input_helper import (
    clear_screen,
)

class SpectatorUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        clear_screen()
        self.menu_ui.print_header("SPECTATOR MENU")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Browse Tournament Information: ")
        self.menu_ui.print_box_line("  [1] View schedule")
        self.menu_ui.print_box_line("  [2] View teams")
        self.menu_ui.print_box_line("  [3] View players")
        self.menu_ui.print_box_line("  [4] View clubs")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  [B] Back to main menu")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").lower()
        
    
        
        if choice not in ["1", "2", "3", "4", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, B")
            input("Press Enter to continue...")
            return self.show_menu()

        if choice == "1": 
            self.view_schedule(); 
            return "SPECTATOR_MENU"
        if choice == "2": 
            self.view_teams_and_players(); 
            return "SPECTATOR_MENU"
        if choice == "3": 
            self.view_teams_and_players(); 
            return "SPECTATOR_MENU"
        if choice == "4": 
            self.view_clubs(); 
            return "SPECTATOR_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def view_schedule(self): 
        self.menu_ui.print_header("VIEW SCHEDULE")
        view_schedule(self)
        return "SPECTATOR_MENU"
        
    def view_teams_and_players(self): 
        self.menu_ui.print_header("VIEW TEAMS AND PLAYERS")

    
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select what you want to view: ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("\t-  [1] View all teams")
        self.menu_ui.print_box_line("\t-  [2] View all players")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("\t-  [B] Back to Spectator Menu")
        self.menu_ui.print_box_bottom()

        choice = input(" ➤ Select an option: ").lower()

        if choice not in ["1", "2", "b"]:
            print("Invalid choice. Valid options: 1, 2, B")
            input("Press Enter to continue...")
            return 

        # view all teams
        if choice == "1":
            self.menu_ui.print_header("ALL TEAMS")
            view_teams(self.ll, self.menu_ui)
            return

        # view all players
        if choice == "2":
            self.menu_ui.print_header("ALL PLAYERS")
            players = self.ll.load_all_player_short_info()

            self.menu_ui.print_box_top()
            if not players:
                self.menu_ui.print_box_line("No players found.")
            else:
                for player in players:
                    self.menu_ui.print_box_line(f" - {player}")
            self.menu_ui.print_box_bottom()

            input("Press Enter to continue...")
            return

        if choice == "b":
            return

        

        
    def view_clubs(self): 
        print("TODO")


        


