from typing import Any, Optional, Dict, Tuple
from UI.input_helper import (
    get_non_empty_input,
    get_integer_input,
    get_choice_input,
    choose_from_list
)


class OrganizerUI:
    def __init__(self, ll: Any, menu_ui: Any) -> None:
        # Store references to logic layer and menu helper class
        self.ll = ll
        self.menu_ui = menu_ui

    # ================================
    # ORGANIZER MENU
    # ================================
    def show_menu(self) -> str:
        """Show the organizer menu and return the next menu state."""

        self.menu_ui.print_header("ORGANIZER MENU")
        print("                ║                                                                        ║")
        print("                ║  Tournament Management:                                                ║")
        print("                ║  [1] Create tournament                                                 ║")
        print("                ║  [2] Generate schedule                                                 ║")
        print("                ║  [3] Enter match result                                                ║")
        print("                ║                                                                        ║")
        print("                ║  Team Management:                                                      ║")
        print("                ║  [4] Change team captain                                               ║")
        print("                ║                                                                        ║")
        print("                ║  Reports:                                                              ║")
        print("                ║  [5] View statistics                                                   ║")
        print("                ║  [6] View schedule                                                     ║")
        print("                ║                                                                        ║")
        print("                ║  [B] Back to main menu                                                 ║")
        print("                ║                                                                        ║")
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║  ➤ Select an option: ", end="")

        choice = input().lower()
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║                    © Reykjavík University - 2025                       ║")
        print("                ╚════════════════════════════════════════════════════════════════════════╝")
        
        if choice not in ["1", "2", "3", "4", "5", "6", "b"]:
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
            self.enter_match_result()
            return "ORGANIZER_MENU"
        if choice == "4":
            self.change_team_captain()
            return "ORGANIZER_MENU"
        if choice == "5":
            self.view_statistics()
            return "ORGANIZER_MENU"
        if choice == "6":
            self.view_schedule()
            return "ORGANIZER_MENU"
        if choice == "b":
            return "MAIN_MENU"


    
    def create_tournament(self) -> None:
        """Create a new tournament by collecting info and sending it to LL."""

        self.menu_ui.print_header("CREATE TOURNAMENT")
        print("Please enter the following details to create a new tournament.\n")

        # Collect input using input helper functions for basic validation
        name = get_non_empty_input("Tournament Name: ")
        location = get_non_empty_input("Location: ")
        start_date = get_non_empty_input("Start Date (YYYY-MM-DD): ")
        end_date = get_non_empty_input("End Date (YYYY-MM-DD): ")

        print("\nTournament Type:")
        print("  [1] Single Elimination")
        print("  [2] Double Elimination")
        type_choice = get_choice_input("Select type (1 or 2): ", ["1", "2"])

        print("\nContact Person Information:")
        contact_name = get_non_empty_input("Full Name: ")
        contact_email = get_non_empty_input("Email: ")
        contact_phone = get_non_empty_input("Phone: ")

        # Forward everything directly to LL 
        result = self.ll.create_tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            type_choice=type_choice,          
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )

        # Print whatever LL returns
        print("\n" + str(result))
        input("Press Enter to continue...")



    def generate_schedule(self) -> None:
    
        self.menu_ui.print_header("GENERATE TOURNAMENT SCHEDULE")
        print("Choose a tournament to generate a schedule for:\n")

        tournaments = self.ll.get_tournament_list()  # get tournaments from LL

        print("Available Tournaments:")
        tournament_name = choose_from_list("Select Tournament by number: ", tournaments)    # choose tournament basic validation with input helper

        print("\nSelect schedule type:")
        print("  [1] Single Elimination")
        print("  [2] Double Elimination")

        schedule_choice = get_choice_input("Select type (1 or 2): ", ["1", "2"]) # get schedule type

        #  Forward to LL
        result = self.ll.generate_schedule(
            tournament_name=tournament_name,
            schedule_type=schedule_choice
        )
        #  Print LL response
        print("\n" + str(result))
        input("\nPress Enter to continue...")




    def enter_match_result(self) -> None:
        """UI for entering a match result. """

        self.menu_ui.print_header("ENTER MATCH RESULT")
        print("Enter the match details below:\n")

        # get tournaments from LL 
        tournaments = self.ll.get_tournament_list()

        print("Available Tournaments:")
        tournament_name = choose_from_list("Select Tournament by number: ", tournaments)

        #  Ask LL for unfinished matches in that tournament
        matches = self.ll.get_unfinished_matches(tournament_name)

        print("\nUnfinished Matches:")
        selected_match = choose_from_list("Select Match by number: ", matches)      # choose match

        # get scores and make sure they are integers with input helper
        print("\nEnter the scores for the match:")
        team_a_score = get_integer_input("Enter Team A Score: ") 
        team_b_score = get_integer_input("Enter Team B Score: ")

        # Forward everything directly to LL
        result = self.ll.enter_match_result(
            selected_match,
            team_a_score,
            team_b_score,
        )

        #  Print LL response
        print("\n" + str(result))
        input("Press Enter to continue...")

        
        



    def change_team_captain(self) -> None:
        """ UI for changing a team's captain. """
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        print("Select a team to change its captain:\n")

        teams = self.ll.get_team_list()   # get the list of teams from LL
        team_name = choose_from_list("Select Team by number: ", teams)      # choose team
        current_captain = self.ll.get_team_captain(team_name)       # get current captain from LL


        print(f"\nTeam: {team_name}\n")
        print(f"Current Captain: {current_captain}\n")

        players = self.ll.get_players_in_team(team_name)   # get players in the selected team from LL
        new_captain = choose_from_list("Select New Captain by number: ", players)  # choose new captain
        result = self.ll.change_team_captain(
            team_name=team_name,
            new_captain=new_captain
        )
        print("\n" + str(result))   # print LL response
        input("Press Enter to continue...")



    def view_statistics(self) -> None:
        self.menu_ui.print_header("VIEW TOURNAMENT STATISTICS")
        # Ask what statistics to view
        print("What statistics would you like to view?")
        print("  [1] Player Statistics")
        print("  [2] Team Statistics")
        print("  [3] Club Statistics")

        # Get choice with input helper
        stats_choice = get_choice_input("Select option (1, 2, or 3): ", ["1", "2", "3"])
        # Based on choice, get relevant list from LL
        if stats_choice == "1":
            stats = self.ll.get_player_list()
        elif stats_choice == "2":
            stats = self.ll.get_team_list()
        elif stats_choice == "3":
            stats = self.ll.get_club_list()
        
        # Ask user to select an item from the list
        selected_item = choose_from_list("Select one: ", stats)
        statistics = self.ll.get_statistics(stats_choice, selected_item) # Get statistics from LL
        print("Statistics:\n")
        print(statistics)
        input("Press Enter to continue...")


    def view_schedule(self) -> None:
        self.menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
        print("Select a tournament to view its schedule:\n")

        # Get list of tournaments from LL
        tournaments = self.ll.get_tournament_list()  

        # choose tournament basic validation with input helper
        tournament_name = choose_from_list("Select Tournament by number: ", tournaments)   

        # get schedule from LL
        schedule = self.ll.get_tournament_schedule(tournament_name)   
        print(f"\nSchedule for {tournament_name}:\n")
        print(schedule)
        input("\nPress Enter to continue...")

    
    def create_team(self) -> None:
        print("TODO: Team creation will be implemented later.")


