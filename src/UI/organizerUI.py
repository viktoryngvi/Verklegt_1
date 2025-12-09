from typing import Any, Optional, Dict, Tuple
from UI.shared_ui_helpers import create_team
from UI.shared_ui_helpers import view_schedule
from UI.input_helper import (
    get_non_empty_input,
    get_integer_input,
    get_choice_input,
    choose_from_list,
    clear_screen,
)
from models.tournament import Tournament

class OrganizerUI:
    def __init__(self, ll: Any, menu_ui: Any):
        # Store references to logic layer and menu helper class
        self.ll = ll
        self.menu_ui = menu_ui

    # ================================
    # ORGANIZER MENU
    # ================================
    def show_menu(self) -> str:
        """Show the organizer menu and return the next menu state."""
        # Clear previous screen / main menu
        clear_screen()  

        self.menu_ui.print_header("ORGANIZER MENU")
        print("                ║                                                                        ║")
        print("                ║  Tournament Management:                                                ║")
        print("                ║  [1] Create tournament                                                 ║")
        print("                ║  [2] Generate schedule                                                 ║")
        print("                ║  [3] Create Event                                                      ║")
        print("                ║  [4] Enter match result                                                ║")
        print("                ║                                                                        ║")
        print("                ║  Team Management:                                                      ║")
        print("                ║  [5] Change team captain                                               ║")
        print("                ║                                                                        ║")
        print("                ║  Reports:                                                              ║")
        print("                ║  [6] View statistics                                                   ║")
        print("                ║  [7] View schedule                                                     ║")
        print("                ║                                                                        ║")
        print("                ║  [B] Back to main menu                                                 ║")
        print("                ║                                                                        ║")
        print("                ╚════════════════════════════════════════════════════════════════════════╝")
        print("                   ➤ Select an option: ", end="")

        choice = input().lower()

        
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, 5, 6, B")
            input("Press Enter to continue...")
            return self.show_menu()

        # Based on the choice, call a function and return the next menu state
        if choice == "1":
            self.create_tournament()
            return "ORGANIZER_MENU"
        if choice == "2":
            self.generate_schedule()
            return "ORGANIZER_MENU"
        if choice == "3":
            self.create_event()
            return "ORGANIZER_MENU"
        if choice == "4":
            self.enter_match_result()
            return "ORGANIZER_MENU"
        if choice == "5":
            self.change_team_captain()
            return "ORGANIZER_MENU"
        if choice == "6":
            self.view_statistics()
            return "ORGANIZER_MENU"
        if choice == "7":
            self.view_schedule()
            return "ORGANIZER_MENU"
        if choice == "b":
            return "MAIN_MENU"


    
    def create_tournament(self):
        """Create a new tournament by collecting info and sending it to LL."""

        self.menu_ui.print_header("CREATE TOURNAMENT")
        print("                ║ Please enter the following details:\n")

        # Collect input using input helper functions for basic validation
        name = get_non_empty_input("                ║ Tournament Name: ")
        location = get_non_empty_input("                ║ Location: ")
        start_date = get_non_empty_input("                ║ Start Date (YYYY-MM-DD): ")
        end_date = get_non_empty_input("                ║ End Date (YYYY-MM-DD): ")


        print("\n                ║ Contact Person Information:")
        contact_name = get_non_empty_input("                ║ Full Name: ")
        contact_email = get_non_empty_input("                ║ Email: ")
        contact_phone = get_non_empty_input("                ║ Phone: ")

        # Forward everything directly to LL 
        result = Tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,          
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )

        result = self.ll.create_tournament(result)
        # Print whatever LL returns
        print("\n" + str(result))
        input("Press Enter to continue...")


    def create_event(self):
        """Create a new event within a tournament."""
        self.menu_ui.print_header("CREATE EVENT")
        print("                ║ Please enter the following details to create a new event.\n")

        # get the info from the user for the event
        print("                ║ Select the tournament for the event:\n")

        # get a list of the tournaments created
        tournaments = self.ll.get_tournament_list()  
        tournament_name = choose_from_list("                ║ Select Tournament by number: ", tournaments)
        print(f"\n                ║ You selected: {tournament_name}\n")

        event_name = get_non_empty_input("                ║ Event Name: ")
        event_type = choose_from_list("                ║ Select Event Type:")

        print("\n                 ║ [1] Single Elimination")
        print("                   ║ [2] Double Elimination")
        print("                   ║ [3] Last man standing")
        event_type_choice = get_choice_input("Select type (1, 2, or 3): ", ["1", "2", "3"])

        # send the info to LL
        result = self.ll.create_event(
            tournament_name,
            event_name,
            event_type,
        )
        print("\n" + str(result))
        input("Press Enter to continue...")



    def generate_schedule(self):
    
        self.menu_ui.print_header("GENERATE TOURNAMENT SCHEDULE")
        print("                ║ Choose a tournament to generate a schedule for:\n")

        tournaments = self.ll.get_tournament_list()  # get tournaments from LL

        print("                ║ Available Tournaments:")
        tournament_name = choose_from_list("                ║ Select Tournament by number: ", tournaments)    
        print(f"\nTournament: {tournament_name}\n")

        # get events in that tournament
        events_in_tournament = choose_from_list("                ║ Select Event by number: ", self.ll.get_events_in_tournament(tournament_name))
        print(f"\n                ║ You selected event: {events_in_tournament}\n")

        # send to LL to generate schedule
        result = self.ll.generate_schedule(
            tournament_name=tournament_name,
            event_name=events_in_tournament,
        )

        print("\n" + str(result))
        input("Press Enter to continue...")



    def enter_match_result(self):
        """UI for entering a match result. """

        self.menu_ui.print_header("ENTER MATCH RESULT")
        print("                ║ Select a tournament: \n")

        # get tournaments from LL 
        tournaments = self.ll.get_tournament_list()

        print("                ║ Available Tournaments:")
        tournament_name = choose_from_list("                ║ Select Tournament by number: ", tournaments)

        events = self.ll.get_events_in_tournament(tournament_name)
        print("\n                ║ Available Events:")

        event_name = choose_from_list("                ║ Select Event by number: ", events)
        print(f"\n                ║ You selected Tournament: {tournament_name}, Event: {event_name}\n")


        #  Ask LL for unfinished matches in that tournament
        matches = self.ll.get_unfinished_matches(event_name, tournament_name)
        if not matches:
            print("No unfinished matches found for this tournament/event.")
            input("Press Enter to continue...")
            return
        

        print("\nUnfinished Matches:")
        selected_match = choose_from_list("                ║ Select Match by number: ", matches)      

        # get scores and make sure they are integers with input helper
        print("\n                ║ Enter the scores for the match:")
        team_a_score = get_integer_input("                ║ Enter Team A Score: ") 
        team_b_score = get_integer_input("                ║ Enter Team B Score: ")

        # Forward everything directly to LL
        result = self.ll.enter_match_result(
            selected_match,
            team_a_score,
            team_b_score,
            tournament_name,
            event_name,
        )

        #  Print LL response
        print("\n" + str(result))
        input("Press Enter to continue...")


    def change_team_captain(self):
        """ UI for changing a team's captain. """
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        print("                ║ Select a team to change its captain:\n")

        teams = self.ll.view_all_teams()   # get the list of teams from LL
        team_name = choose_from_list("                ║ Select Team by number: ", teams)      # choose team
        current_captain = self.ll.update_team_captain(team_name)       # get current captain from LL


        print(f"\n                ║ Team: {team_name}\n")
        print(f"                ║ Current Captain: {current_captain}\n")

        players = self.ll.view_all_players_in_team(team_name)   # get players in the selected team from LL
        new_captain_handle = choose_from_list("                ║ Select New Captain by number: ", players)  # choose new captain
        result = self.ll.change_team_captain(
            team_name=team_name,
            new_captain_handle=new_captain_handle,
        )
        print("\n" + str(result))   # print LL response
        input("Press Enter to continue...")



    def view_statistics(self):
        pass
        


    def view_schedule(self):
        view_schedule(self.ll, self.menu_ui)
        return "ORGANIZER_MENU"
        

    
    def create_team(self):
        print("TODO: Team creation will be implemented later.")

    def register_club(self):
        pass

    # add team to club
    # view clubs
    # view club information

