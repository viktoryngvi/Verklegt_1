from UI.shared_ui_helpers import view_teams
from UI.shared_ui_helpers import view_schedule
from UI.input_helper import (
    get_non_empty_input,
    clear_screen,
    choose_from_list
)


class PlayerUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        clear_screen()
        self.menu_ui.print_header("PLAYER MENU")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  My Profile: ")
        self.menu_ui.print_box_line("  [1] View profile")
        self.menu_ui.print_box_line("  [2] Edit my info")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  My Team: ")
        self.menu_ui.print_box_line("  [3] View team")
        self.menu_ui.print_box_line("  [4] View schedule")
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
        self.menu_ui.print_header("MY PROFILE")
        self.menu_ui.print_box_top()
        handle = get_non_empty_input("\tEnter your player handle: ").strip().lower()
        self.menu_ui.print_box_bottom()

        # display profile info
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Loading profile for handle: {handle} ")
        self.menu_ui.print_box_bottom()

        profile = self.ll.load_player_info(handle)
        if profile:  
            self.menu_ui.print_box_top()
            self.menu_ui.print_box_line(f" Profile Information for {handle} ")
            self.menu_ui.print_box_line(f" Name   : {profile['name']}")
            self.menu_ui.print_box_line(f" Phone  : {profile['phone']}")
            self.menu_ui.print_box_line(f" Address: {profile['address']}")
            self.menu_ui.print_box_line(f" DOB    : {profile['dob']}")
            self.menu_ui.print_box_line(f" Email  : {profile['email']}")
            self.menu_ui.print_box_line(f" Handle : {profile['handle']}")
            self.menu_ui.print_box_line(f" Team   : {profile['team']}")
            self.menu_ui.print_box_bottom()
        else:
            self.menu_ui.print_box_top()
            self.menu_ui.print_box_line(" Player not found.")
            self.menu_ui.print_box_bottom()

        input("Press Enter to continue...")


    def edit_player(self): 
        # phone, email, address, handle
        # spurja um handle, senda new info til LL
        self.menu_ui.print_header("EDIT MY INFO")
        self.menu_ui.print_box_top()
        handle = input("\tEnter your player handle: ").strip().lower()
        self.menu_ui.print_box_bottom() 

        if not handle:
            print("Handle cannot be empty.")
            input("Press Enter to continue...")
            return
        while True:

            self.menu_ui.print_box_top()
            self.menu_ui.print_box_line(f" Editing info for handle: {handle} ")
            self.menu_ui.print_box_bottom()
            self.menu_ui.print_box_top()
            self.menu_ui.print_box_line(" Choose info to edit: ")
            self.menu_ui.print_box_line()
            self.menu_ui.print_box_line("\t-  [1] Phone")
            self.menu_ui.print_box_line("\t-  [2] Email")
            self.menu_ui.print_box_line("\t-  [3] Address")
            self.menu_ui.print_box_line("\t-  [4] Handle")
            self.menu_ui.print_box_line()
            self.menu_ui.print_box_line("\t-  [B] Back to Player Menu")
            self.menu_ui.print_box_bottom()
            choice = input(" ➤ Select an option: ").lower()
            

            if choice == "1":
                self.menu_ui.print_box_top()
                new_phone = input(" Enter new phone (format 123-4567): ").strip()
                result = self.ll.edit_player_phone(handle, new_phone)
                self.menu_ui.print_box_bottom()
        
            elif choice == "2":
                self.menu_ui.print_box_top()
                new_email = input(" Enter new email: ").strip()
                result = self.ll.edit_player_email(handle, new_email)
                self.menu_ui.print_box_bottom()

            elif choice == "3":
                self.menu_ui.print_box_top()
                new_address = input(" Enter new address: ").strip()
                result = self.ll.edit_player_address(handle, new_address)
                self.menu_ui.print_box_bottom()

            elif choice == "4":
                self.menu_ui.print_box_top()
                new_handle = input(" Enter new handle: ").strip().lower()
                result = self.ll.edit_player_handle(handle, new_handle)
                self.menu_ui.print_box_bottom()

            elif choice == "b":
                return "PLAYER_MENU"
        
            else:
                print("Invalid choice. Valid options are 1, 2, 3, 4, B.")
                input("Press Enter to continue...")
                continue
        
            print("\n" + str(result))
            input("Press Enter to continue...")


        



    def view_team(self): 
        self.menu_ui.print_header("VIEW TEAMS")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a team to view: ")
        teams = self.ll.view_all_teams()

        team_name = choose_from_list("Select Team by number: ", teams)

        print(f"\nYou selected: {team_name}\n")

        players_in_team = self.ll.get_players_in_team(team_name)
        print(f"Players in {team_name}:")
        for player in players_in_team:
            print(f" - {player}")
        input("Press Enter to continue...")
        return
        
    def view_schedule(self): 
        view_schedule(self.ll, self.menu_ui)
        return "PLAYER_MENU"
    
