from models.player import Player
from UI.input_helper import get_non_empty_input



class CaptainUI:
    def __init__(self, ll_wrapper, menu_ui):
        self.ll = ll_wrapper
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        self.menu_ui.print_header("CAPTAIN MENU")
        print("                ║                                                                        ║")
        print("                ║  Player Management:                                                    ║")
        print("                ║  [1] Create player                                                     ║")
        print("                ║  [2] Edit player info                                                  ║")
        print("                ║                                                                        ║")
        print("                ║  Team Management:                                                      ║")
        print("                ║  [3] View team                                                         ║")
        print("                ║  [4] Change team captain                                               ║")
        print("                ║                                                                        ║")
        print("                ║  Schedule:                                                             ║")
        print("                ║  [5] View schedule                                                     ║")
        print("                ║                                                                        ║")
        print("                ║  [B] Back to main menu                                                 ║")
        print("                ║                                                                        ║")
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║  ➤ Select an option: ", end="")

        choice = input().lower()
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║                    © Reykjavík University - 2025                       ║")
        print("                ╚════════════════════════════════════════════════════════════════════════╝")
        
        if choice not in ["1", "2", "3", "4", "5", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, 5, B")
            input("Press Enter to continue...")
            return self.show_menu()

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
        print("\n==== Create Player ====\n")

        # Collect input (UI safety only - prevent empty/crashes)
        name = get_non_empty_input("Full name: ")
        phone = get_non_empty_input("Phone: ")
        address = get_non_empty_input("Address: ")
        dob = get_non_empty_input("DOB (YYYY-MM-DD): ")
        email = get_non_empty_input("Email: ")
        handle = get_non_empty_input("Handle (unique): ")
        team = None  # Captains do not assign teams when creating players

        # ID must not be asked by UI — let LL/DL handle it.
        # So we send id=None
        player = Player(
            name=name,
            phone=phone,
            address=address,
            dob=dob,
            email=email,
            id=None,
            handle=handle,
            team=None,
        )

        # Call LL through wrapper
        try:
            result = self.ll.create_player(player)
        except Exception as e:
            print(f"Unexpected error creating player: {e}")
            return "CAPTAIN_MENU"

        # LL returns list of errors OR a success string
        if isinstance(result, list):  # validation failed
            print("Player could not be created. Errors:")
            for err in result:
                print(f" - {err}")
        else:
            print("Player created successfully!")

        return "CAPTAIN_MENU"

    def edit_player_info(self): 
        print("TODO")
    def view_team(self): 
        print("TODO")
    def change_team_captain(self): 
        print("TODO")
    def view_schedule(self): 
        print("TODO")
    def create_team(self): 
        print("TODO")
