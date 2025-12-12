from datetime import date
from models.player import Player
from LL.logical_wraper import LLWrapper
from UI.input_helper import (
    get_non_empty_input,
    get_integer_input,
    get_choice_input,
    choose_from_list,
    get_optional_input,
    clear_screen,
)

class CaptainUI:
    def __init__(self, ll_wrapper: LLWrapper, menu_ui):
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
        self.menu_ui.print_box_line("  [5] Create new team")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Schedule: ")
        self.menu_ui.print_box_line("  [6] View schedule")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  [B] Back to main menu")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").strip().lower()
        

      
        if choice not in ["1", "2", "3", "4", "5", "6", "b"]:
            print("Invalid choice. Valid options: 1, 2, 3, 4, 5, 6, B")
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
            self.create_team(); 
            return "CAPTAIN_MENU"
        if choice == "6": 
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
        dob = get_integer_input("\t- DOB (YYYY-MM-DD): ")
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
            print(result)

        input("Press Enter to continue...")
        return "CAPTAIN_MENU"

    def edit_player_info(self):
        # ask for captain handle
        self.menu_ui.print_header("EDIT PLAYER INFO")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To edit a player's information, please provide your captain handle: ")
        self.menu_ui.print_box_line()

        
        print("\t-  Enter your captain handle: ", end="")                                   
        captain_handle = input().strip().lower() 
        self.menu_ui.print_box_bottom()

        check_captain = self.ll.captain_handle(captain_handle)
        if not check_captain:
            print("\tNo captain found with that handle.")
            input("Press Enter to continue...")
            return
        
    
        

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
        #################################################3
        
        # let the captain choose a player to edit from his team
        for player in team_players:
            self.menu_ui.print_box_line(f" - {player.handle}")
        self.menu_ui.print_box_line()
        selected_player = input("\t-  Enter the player handle: ").strip().lower()
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
        self.menu_ui.print_header("VIEW YOUR TEAM")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To view your team, please provide your team name: ")
        self.menu_ui.print_box_line()

        
        captains_team = input("\t-  Enter your team name: ").strip()
        # check if captain's team exists
        if not self.ll.check_if_team_exists(captains_team):
            print("\tNo team found with that name.")
            input("Press Enter to continue...")
            return
        
        self.menu_ui.print_box_line()
        
        self.menu_ui.print_box_bottom()

        if not captains_team:
            print("\tTeam name cannot be empty.")
            input("Press Enter to continue...")
            return

        team_players = self.ll.view_all_players_in_team(captains_team)
        if not team_players:
            print("No players found in your team.")
            input("Press Enter to continue...")
            return
        print("")

        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Players in team: {captains_team} ")
        self.menu_ui.print_box_line()
        for player in team_players:
            self.menu_ui.print_box_line(f" Player ID: {player.id} ")
            self.menu_ui.print_box_line(f"-----------------------")
            self.menu_ui.print_box_line(f"\t Name: {player.name}")
            self.menu_ui.print_box_line(f"\t Handle: {player.handle}")
            self.menu_ui.print_box_line(f"\t Email: {player.email}")
            self.menu_ui.print_box_line(f"\t Phone: {player.phone}")
            self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        input("Press Enter to continue...")
        return
    
        

        

    
    def change_team_captain(self):
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To change the team captain, please follow the steps below: ")
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select the team you want to change the captain for: ")
        self.menu_ui.print_box_line()
        # get the list of teams from LL 
        teams = self.ll.view_all_teams()

        # check if there are any teams
        if not teams:
            print("No teams found.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        # let user select a team
        for team in teams:
            self.menu_ui.print_box_line(f" - {team.name}")
        
        self.menu_ui.print_box_line()

        while True:
            user_team_input = input(" Enter the team name: ").strip()

            # find the actual team object
            select_team = None
            for team in teams:
                if team.name == user_team_input:
                    select_team = team
                    break


            if not select_team:
                print("Team not found. Please try again.")
                continue
            break

        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()



        # get players in that team
        players = self.ll.view_all_players_in_team(select_team.name)
        # check if there are any players
        if not players:
            print("No players found in this team.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        
        teams = self.ll.view_all_teams()
        current_captain = None
        for t in teams:
            if t.name == select_team:
                current_captain = t.captain
                break

        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" You selected team: {select_team} ")
        if current_captain:
            self.menu_ui.print_box_line(f" Current captain: {current_captain}")
        else:
            self.menu_ui.print_box_line(" Current captain: None ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(" Select the new captain from the team players: ")


        # let user select a player to be the new captain
        for player in players:
            self.menu_ui.print_box_line(f" - {player.handle}")
        while True:
            new_captain_handle = input(" Enter the player handle: ").strip().lower()
            if any(p.handle == new_captain_handle for p in players):
                break
            print(" Handle not found in this team. Try again.")

        self.menu_ui.print_box_line(f" You selected player: {new_captain_handle} as the new captain. ")
        self.menu_ui.print_box_bottom()
        
        # send to LL to update
        result = self.ll.update_team_captain(
            select_team.name,
            new_captain_handle
            )
        
        print("")
        print(result)
        input("Press Enter to continue...")
    
    def view_schedule(self): 
        self.menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a tournament to view its schedule: ")
        self.menu_ui.print_box_line()

        # Get list of tournaments from LL
        tournaments = self.ll.get_tournament_list()  

        # choose tournament basic validation with input helper
        tournament_name = choose_from_list("Select Tournament by number: ", tournaments)  

        self.menu_ui.print_box_line() 
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")    
        self.menu_ui.print_box_bottom()

        # print the list of events in that tournament
        self.menu_ui.print_box_top()
        events_in_tournament = choose_from_list("Select Event by number: ", self.ll.get_events_in_tournament(tournament_name))
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Event: {events_in_tournament}")
    
        self.menu_ui.print_box_bottom()
        # get schedule from ll for that tournament and event
        self.menu_ui.print_header("TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        
        schedule = self.ll.get_tournament_schedule(tournament_name, events_in_tournament)
        if not schedule:
            print("No schedule found for this tournament/event.")
        else:
            print(f"Schedule for {tournament_name} - {events_in_tournament}:")
            for match in schedule:
                print(f" - {match}")
        input("Press Enter to continue...")
        return
    
    def create_team(self):
       self.menu_ui.print_header("CREATE TEAM")


       # team name
       self.menu_ui.print_box_top()
       team_name = input("\tTeam Name: ").strip()
       self.menu_ui.print_box_bottom()


       # captain handle
       self.menu_ui.print_box_top()
     
       # validate that captain handle exists and get id
      
       while True:
           captain_handle = get_non_empty_input("\tCaptain Handle: ").strip().lower()
           cap_id = self.ll.take_handle_return_id(captain_handle)


           if cap_id:
               break


           print("Captain handle does not exist. Try again.")
       self.menu_ui.print_box_bottom()
      




       # select players
       self.menu_ui.print_box_top()
       # need list of all players without a team
       all_players = self.ll.players_team_none() 


       # select players for the team 
       print(" Select players: ")
      
       for player in all_players:
           player_id, name, handle = player
           print(f" - [{player_id}] {name} ({handle})")

       # only valid IDs the _ is to skip the name, and handle and only get the id 
       valid_ids = {int(player_id) for player_id, _, _ in all_players}


       while True:
           raw = input("Enter player IDs (comma separated): ").strip()
           if not raw:
               print("Input cannot be empty.")
               continue


           parts = [p.strip() for p in raw.split(",") if p.strip() != ""]
           try:
               ids = [int(p) for p in parts]
           except ValueError:
               print("Invalid input! Use only numbers separated by commas.")
               continue


           # check all selected IDs exist in valid_ids
           invalid = [i for i in ids if i not in valid_ids]
           if invalid:
               print(f"Invalid player IDs: {', '.join(map(str, invalid))}")
               print("Please choose only from the listed IDs.")
               continue


           break 


       players_as_str = ",".join(str(i) for i in ids)
       self.menu_ui.print_box_bottom()


       player_ids = self.ll.take_list_of_players_return_list_of_ids(players_as_str)
       result = self.ll.create_team(team_name, cap_id, player_ids)


       print(result)
       input("Press Enter to continue...")
