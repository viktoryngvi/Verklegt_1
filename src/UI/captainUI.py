from models.player import Player
from UI.shared_ui_helpers import view_teams, create_team, view_schedule
from UI.input_helper import (
    get_non_empty_input,
    get_integer_input,
    get_choice_input,
    choose_from_list,
    get_optional_input,
)

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
        # 

        pass

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
