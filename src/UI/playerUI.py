from UI.input_helper import (
    get_non_empty_input,
    clear_screen,
    choose_from_list
)
from LL.logical_wraper import LLWrapper
from models.player import Player


class PlayerUI:
    def __init__(self, ll: LLWrapper, menu_ui):
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
        # self.ll.validate_handle(handle)
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Loading profile for handle: {handle} ")
        self.menu_ui.print_box_bottom()

        player = self.ll.load_player_by_handle(handle)
        if isinstance(player, Player):  
            self.menu_ui.print_box_top()
            self.menu_ui.print_box_line(f" Profile Information for {handle} ")
            self.menu_ui.print_box_line(f" Name   : {player.name} ")
            self.menu_ui.print_box_line(f" Phone  : {player.phone} ")
            self.menu_ui.print_box_line(f" Address: {player.address} ")
            self.menu_ui.print_box_line(f" DOB    : {player.dob} ")
            self.menu_ui.print_box_line(f" Email  : {player.email} ")
            self.menu_ui.print_box_line(f" Handle : {player.handle} ")
            self.menu_ui.print_box_line(f" Team   : {player.team if player.team else 'No team assigned'} ")
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
        self.menu_ui.print_box_bottom() 
        T_F = True
        while T_F:
            self.menu_ui.print_header("EDIT MY INFO")
            self.menu_ui.print_box_top()
            handle = input("\tEnter your player handle: ").strip().lower()
            self.menu_ui.print_box_bottom() 

            if not handle:
                print("Handle cannot be empty.")
                input("Press Enter to continue...")
                return
            else:
                result = self.ll.check_if_handle_in_use(handle)
                if result == False:
                    print("Player handle does not exist")
                    T_F = True
                else:
                    T_F = False
                
                
                
            
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
                if "-" not in new_phone:
                    new_phone = new_phone[:3] + "-" + new_phone[3:]
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

        for team in teams:
            self.menu_ui.print_box_line(f" - {team.name} (Captain: {team.captain}) ")
        self.menu_ui.print_box_bottom()

        team_name = get_non_empty_input(" Enter team name: ").strip()
        team_players = self.ll.get_players_in_team(team_name)
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Players in team {team_name}: ")
        if team_players:
            for player in team_players:
                self.menu_ui.print_box_line(f" - {player.name} ")
        else:
            self.menu_ui.print_box_line(" No players found or team does not exist. ")
        self.menu_ui.print_box_bottom()
        input("Press Enter to continue...")

        

        
        
    def view_schedule(self): 
        self.menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a tournament to view its schedule: ")
        self.menu_ui.print_box_line()

        # Get list of tournaments from LL
        tournaments = self.ll.get_tournament_list()  
        list_of_tournament_names = [tournament for tournament in tournaments]

        for i, tournament in enumerate(list_of_tournament_names, start=1):
            self.menu_ui.print_box_line(f"  [{i}] {tournament}")
        self.menu_ui.print_box_line()
        select_tournament = get_non_empty_input(" ➤ Select Tournament by number: ").strip()
        try:
            t_idx = int(select_tournament) - 1
            tournament_name = list_of_tournament_names[t_idx]
        except (ValueError, IndexError):
            print("Invalid tournament selection.")
            input("Press Enter to continue...")
            return
        # choose tournament basic validation with input helper
        
        event_name = self.ll.get_events_in_tournament(tournament_name)
        list_of_event_names = [event for event in event_name]

        for i, event in enumerate(list_of_event_names, start=0):
            if i == 0:
                continue
            self.menu_ui.print_box_line(f"  [{i}] {event}")
        self.menu_ui.print_box_line()
        select_event = get_non_empty_input(" ➤ Select Event by number: ").strip()
        try:
            e_idx = int(select_event)
            event_name = list_of_event_names[e_idx]
        except (ValueError, IndexError):
            print("Invalid event selection.")
            input("Press Enter to continue...")
            return 

        self.menu_ui.print_box_line() 
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")    
        self.menu_ui.print_box_bottom()

        # print the list of events in that tournament
        self.menu_ui.print_box_top()
        # Load events
        events = self.ll.get_events_in_tournament(tournament_name)
        if not events:
            print("This tournament has no events.")
            input("Press Enter to continue...")
            return

        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Event: {event_name}")
        self.menu_ui.print_box_bottom()

        # get schedule from ll for that tournament and event
        # bracket id, date, server id, teams, scores
        self.menu_ui.print_header("TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()

        schedule: list[Match] = self.ll.view_games(tournament_name, event_name)
        if not schedule:
            self.menu_ui.print_box_line(" No schedule found for this tournament/event. ")
        else:
            self.menu_ui.print_box_line(f" Schedule for {tournament_name} - {event_name}: ")    
            for match in schedule:
                self.menu_ui.print_box_line(f" Match ID: {match.match_id} ")
                self.menu_ui.print_box_line(f" - Bracket Number: {match.bracket_nr} ")
                self.menu_ui.print_box_line(f" - Date: {match.date_of_match}")
                self.menu_ui.print_box_line(f" - Time: {match.time_of_match} ")
                self.menu_ui.print_box_line(f" - Server ID: {match.server_id} ")
                self.menu_ui.print_box_line(f" - Team A: {match.team_a} vs Team B: {match.team_b} ")
                self.menu_ui.print_box_line(f" - Score: {match.team_a_score} - {match.team_b_score} ")
                self.menu_ui.print_box_line(f" - Winner: {match.winner} ")
                self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()

        input("Press Enter to continue...")
        return
    
