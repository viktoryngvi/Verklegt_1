from UI.shared_ui_helpers import view_teams
from UI.shared_ui_helpers import view_schedule



class SpectatorUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        self.menu_ui.print_header("SPECTATOR MENU")
        print("                ║                                                                        ║")
        print("                ║  Browse Tournament Information:                                        ║")
        print("                ║  [1] View schedule                                                     ║")
        print("                ║  [2] View teams                                                        ║")
        print("                ║  [3] View players                                                      ║")
        print("                ║  [4] View clubs                                                        ║")
        print("                ║                                                                        ║")
        print("                ║  [B] Back to main menu                                                 ║")
        print("                ║                                                                        ║")
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║  ➤ Select an option: ", end="")

        choice = input().lower()
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║                    © Reykjavík University - 2025                       ║")
        print("                ╚════════════════════════════════════════════════════════════════════════╝")
        
        if choice not in ["1", "2", "3", "4", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, B")
            input("Press Enter to continue...")
            return self.show_menu()

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
        self.menu_ui.print_header("VIEW SCHEDULE")
        view_schedule(self)
        return "SPECTATOR_MENU"

    def view_teams_and_players(self): 
        # name, id, handle, team
        print("==== View Teams and Players ====")
        self.menu_ui.print_header("VIEW TEAMS AND PLAYERS")

        print(" [1] View all teams")
        print(" [2] View all players")
        print(" [B] Back to Spectator Menu")
        print("                ║  ➤ Select an option: ", end="")

        choice = input().lower()
        if choice not in ["1", "2", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, B")
            input("Press Enter to continue...")
            return 
        if choice == "1":
            self.ll.get_teams()
            view_teams(self.ll, self.menu_ui)
        if choice == "2":
            self.ll.load_all_player_short_info()
            for player in self.ll.all_players_short_info:
                print(f" - {player}")
            input("Press Enter to continue...")
        if choice == "b":
            return
        

        
    def view_clubs(self): 
        print("TODO")


        


