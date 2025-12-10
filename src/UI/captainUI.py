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
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Player Management: ")
        self.menu_ui.print_box_line("  [1] Create player")
        self.menu_ui.print_box_line("  [2] Edit player info")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Team Management: ")
        self.menu_ui.print_box_line("  [3] View team")
        self.menu_ui.print_box_line("  [4] Change team captain")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Schedule: ")
        self.menu_ui.print_box_line("  [5] View schedule")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  [B] Back to main menu")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").strip().lower()
        

      
        if choice not in ["1", "2", "3", "4", "5", "b"]:
            print("Invalid choice. Valid options: 1, 2, 3, 4, 5, B")
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
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Please provide the following details to create a new player: ")
        self.menu_ui.print_box_bottom()        

        # get player details
        name = get_non_empty_input("\t- Full name: ").strip()
        phone = get_non_empty_input("\t- Phone: ").strip()
        address = get_non_empty_input("\t- Address: ").strip()
        dob = get_non_empty_input("\t- DOB (YYYY-MM-DD): ").strip()
        email = get_non_empty_input("\t- Email: ").strip()
        handle = get_non_empty_input("\t- Handle (unique): ").strip().lower()
        self.menu_ui.print_box_bottom()
        
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

        print("")  

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
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To edit a player's information, please provide your captain handle: ")
        self.menu_ui.print_box_line()
        print("\t-  Enter your captain handle: ", end="")
                                            
        captain_handle = input().strip().lower() 
        self.menu_ui.print_box_bottom()
        

        if not captain_handle:
            print("\tHandle cannot be empty.")
            input("Press Enter to continue...")
            return
        
        # show captain's team
        print("")
        self.menu_ui.print_box_top()
        team_name = self.ll.view_captain_team(captain_handle)
        self.menu_ui.print_box_line(f"\t-  Your team is: {team_name}")
        self.menu_ui.print_box_line()
        
        if not team_name:
            print("No team found for this captain.")
            input("Press Enter to continue...")
            return
        
        

        # get the list of players in the captains team
        self.menu_ui.print_box_line(" Select the player to edit:")

        team_players = self.ll.view_all_players_in_team(team_name)
        if not team_players:
            print("No players found in your team.")
            input("Press Enter to continue...")
            return
        
        
        # let the captain choose a player to edit from his team
        selected_player = choose_from_list(" Enter the number of the player: ", team_players)
        self.menu_ui.print_box_bottom()
        print("")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" You selected to edit player: {selected_player}")
        self.menu_ui.print_box_line()

        # phone, email, address, handle
        self.menu_ui.print_box_line(" Select the information you want to edit:")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("\t-  [1] Phone")
        self.menu_ui.print_box_line("\t-  [2] Email")
        self.menu_ui.print_box_line("\t-  [3] Address")
        self.menu_ui.print_box_line("\t-  [4] Handle")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("\t-  [B] Back to Captain Menu")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").strip().lower()
        print("")

        # Ask for actual new value using input(), not print_box_line
        if choice == "1":
            new_phone = input("\t-  Enter new phone number: ").strip()
            results = self.ll.edit_player_phone_captain(captain_handle, selected_player, new_phone)

        elif choice == "2":
            new_email = input("\t-  Enter new email: ").strip()
            results = self.ll.edit_player_email_captain(captain_handle, selected_player, new_email)
        
        elif choice == "3":
            new_address = input("\t-  Enter new address: ").strip()
            results = self.ll.edit_player_address_captain(captain_handle, selected_player, new_address)

        elif choice == "4":
            new_handle = input("\t-  Enter new handle: ").strip().lower()
            results = self.ll.edit_player_handle_captain(captain_handle, selected_player, new_handle)
        
        elif choice == "b":
            return "CAPTAIN_MENU"
        
        else:
            print("Invalid choice. Valid options are 1, 2, 3, 4, B.")
            input("Press Enter to continue...")
            return
        
        print("\n" + str(results))
        input("Press Enter to continue...")
        return "CAPTAIN_MENU"

    def view_team(self): 
        view_teams(self.ll, self.menu_ui)
        return "CAPTAIN_MENU"
    

    
    def change_team_captain(self):
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To change the team captain, please follow the steps below: ")
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select the team you want to change the captain for: ")
        # get the list of teams from LL
        teams = self.ll.view_all_teams()

        # check if there are any teams
        if not teams:
            print("No teams found.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        # let user select a team
        select_team = choose_from_list(" Enter the number of the team: ", teams)

        # get players in that team
        players = self.ll.view_all_players_in_team(select_team)
        # check if there are any players
        if not players:
            print("No players found in this team.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" You selected team: {select_team} ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(" Select the new captain from the team players: ")


        # let user select a player to be the new captain
        select_player = choose_from_list(" Enter the number of the player: ", players)

        self.menu_ui.print_box_line(" You selected player: {select_player} as the new captain. ")
        self.menu_ui.print_box_bottom()
        
        # send to LL to update
        result = self.ll.update_team_captain(
            team_name=select_team,
            new_captain_handle=select_player,
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
