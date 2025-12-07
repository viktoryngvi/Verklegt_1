from UI.shared_ui_helpers import view_teams
from UI.shared_ui_helpers import view_schedule

class PlayerUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        self.menu_ui.print_header("PLAYER MENU")
        print("                ║                                                                        ║")
        print("                ║  My Profile:                                                           ║")
        print("                ║  [1] View profile                                                      ║")
        print("                ║  [2] Edit my info                                                      ║")
        print("                ║                                                                        ║")
        print("                ║  My Team:                                                              ║")
        print("                ║  [3] View team                                                         ║")
        print("                ║  [4] View schedule                                                     ║")
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
        # phone, email, address, handle
        # spurja um handle, senda new info til LL
        self.menu_ui.print_header("EDIT MY INFO")
        print("Enter your player handle: ")
        handle = input().strip().lower()
    
        if not handle:
            print("Handle cannot be empty.")
            input("Press Enter to continue...")
            return
        
        print("Select the information you want to edit: ")
        print("   [1] Phone")
        print("   [2] Email")
        print("   [3] Address")
        print("   [4] Handle")
        print("   [B] Back to Player Menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            new_phone = input("Enter new phone: ").strip()
            result = self.ll.edit_player_phone(handle, new_phone)
        
        elif choice == "2":
            new_email = input("Enter new email: ").strip()
            result = self.ll.edit_player_email(handle, new_email)

        elif choice == "3":
            new_address = input("Enter new address: ").strip()
            result = self.ll.edit_player_address(handle, new_address)

        elif choice == "4":
            new_handle = input("Enter new handle: ").strip().lower()
            result = self.ll.edit_player_handle(handle, new_handle)

        elif choice == "b":
            return "PLAYER_MENU"
        
        else:
            print("Invalid choice. Valid options are 1, 2, 3, 4, B.")
            input("Press Enter to continue...")
            return
        
        print("\n" + str(result))
        



    def view_team(self): 
        view_teams(self.ll, self.menu_ui)
        return "PLAYER_MENU"
    
    def view_schedule(self): 
        view_schedule(self.ll, self.menu_ui)
        return "PLAYER_MENU"
    
