from models.player import Player
from UI.shared_ui_helpers import view_teams, create_team, view_schedule
from UI.input_helper import (
    get_non_empty_input,
    get_integer_input,
    get_choice_input,
    choose_from_list,
    get_optional_input,
    clear_screen,
)

class CaptainUI:
    def __init__(self, ll_wrapper, menu_ui):
        self.ll = ll_wrapper
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        clear_screen()
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
        print("                  ➤ Select an option: ", end="")

        choice = input().lower()
      
        
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
        self.menu_ui.print_header("CREATE PLAYER")
        print("Please enter the following details to create a new player:")
        

        # Collect fields from user 
        name = get_non_empty_input("Full name: ").strip()
        phone = get_non_empty_input("Phone: ").strip()
        address = get_non_empty_input("Address: ").strip()
        dob = get_non_empty_input("DOB (YYYY-MM-DD): ").strip()
        email = get_non_empty_input("Email: ").strip()
        handle = get_non_empty_input("Handle (unique): ").strip()
        
        # send to LL through Player model
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

        # send to LL through wrapper
        result = self.ll.create_player(player)

        print("")  # spacing

        # list => validation errors, string => status "Success" or error text
        if isinstance(result, list):
            print("Player could not be created:")
            for err in result:
                print(f" - {err}")
        elif isinstance(result, str):
            # Should be "Success" when all validations pass
            print(result)

        input("Press Enter to continue...")
        return "CAPTAIN_MENU"

    def edit_player_info(self):
        # ask for captain id
        self.menu_ui.print_header("EDIT PLAYER INFO")
        print("                ║                                                                        ║")
        print("                ║ Enter your handle:                                                     ║")
        captain_handle = input().strip().lower()

        if not captain_handle:
            print("Handle cannot be empty.")
            input("Press Enter to continue...")
            return
        
        # show captain's team
        print("Your team is: ")
        view_team = self.ll.view_captains_team(captain_handle)
        if not view_team:
            print("No team found for this captain.")
            input("Press Enter to continue...")
            return
        
        print(view_team) # displays the captains team and the players in it

        print("")

        # get the list of players in the captains team
        print("Select the player you want to edit from your team: ")
        team_players = self.ll.get_players_in_team(view_team)
        if not team_players:
            print("No players found in your team.")
            input("Press Enter to continue...")
            return
        
        # let the captain choose a player to edit from his team
        selected_player = choose_from_list("Enter the number of the player: ", team_players)
        print(f"You selected to edit player: {selected_player}")
        print("")

        # phone, email, address, handle
        print("Player selected: ", selected_player)
        print("Select the information you want to edit: ")
        print("   [1] Phone")
        print("   [2] Email")
        print("   [3] Address")
        print("   [4] Handle")
        print("   [B] Back to Captain Menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            new_phone = input("Enter new phone number: ").strip()
            results = self.ll.edit_player_phone_captain(captain_handle, selected_player, new_phone)

        elif choice == "2":
            new_email = input("Enter new email: ").strip()
            results = self.ll.edit_player_email_captain(captain_handle, selected_player, new_email)
        
        elif choice == "3":
            new_address = input("Enter new address: ").strip()
            results = self.ll.edit_player_address_captain(captain_handle, selected_player, new_address)

        elif choice == "4":
            new_handle = input("Enter new handle: ").strip().lower()
            results = self.ll.edit_player_handle_captain(captain_handle, selected_player, new_handle)
        
        elif choice == "b":
            return "CAPTAIN_MENU"
        
        else:
            print("Invalid choice. Valid options are 1, 2, 3, 4, B.")
            input("Press Enter to continue...")
            return
        
        print("\n" + str(results))
        

    def view_team(self): 
        view_teams(self.ll, self.menu_ui)
        return "CAPTAIN_MENU"
    

    
    def change_team_captain(self):
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        print("What team do you want to change the captain for? ")
        # get the list of teams from LL
        teams = self.ll.get_teams()

        # check if there are any teams
        if not teams:
            print("No teams found.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        # let user select a team
        select_team = choose_from_list("Enter the number of the team: ", teams)

        # get players in that team
        players = self.ll.get_players_in_team(select_team)
        # check if there are any players
        if not players:
            print("No players found in this team.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        print("Select the new captain from the team players: ")
        # let user select a player to be the new captain
        select_player = choose_from_list("Enter the number of the player: ", players)

        print(f"You selected to change the captain of team: {select_team} to player: {select_player}")
        # send to LL to update
        result = self.ll.update_team_captain(
            team_name=select_team,
            new_captain_name=select_player,
            )
        
        print("")
        print(result)
        input("Press Enter to continue...")
        return "CAPTAIN_MENU"
    
    def view_schedule(self): 
        view_schedule(self.ll, self.menu_ui)
        return "CAPTAIN_MENU"
    
    def create_team(self): 
        print("TODO")
