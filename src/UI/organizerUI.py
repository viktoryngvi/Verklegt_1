from typing import Any, Optional, Dict, Tuple



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


    # ================================
    # CREATE TOURNAMENT
    # ================================
    def create_tournament(self) -> None:
        """Create a new tournament by collecting info and sending it to LL."""

        self.menu_ui.print_header("CREATE TOURNAMENT")
        print("Please enter the following details to create a new tournament.\n")

        # 1. Collect raw input (UI only)
        name = input("Tournament Name: ").strip()
        location = input("Location: ").strip()
        start_date = input("Start Date (YYYY-MM-DD): ").strip()
        end_date = input("End Date (YYYY-MM-DD): ").strip()

        print("\nTournament Type:")
        print("  [1] Single Elimination")
        print("  [2] Double Elimination")
        type_choice = input("Select type (1 or 2): ").strip()

        print("\nContact Person Information:")
        contact_name = input("Full Name: ").strip()
        contact_email = input("Email: ").strip()
        contact_phone = input("Phone: ").strip()

        # 2. Forward everything directly to LL 
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

        # 3. Print whatever LL returns
        print("\n" + str(result))
        input("Press Enter to continue...")



    def generate_schedule(self) -> None:
    
        self.menu_ui.print_header("GENERATE TOURNAMENT SCHEDULE")
        print("Choose a tournament to generate a schedule for:\n")

        tournaments = self.ll.get_tournament_list()

        print("Available Tournaments:")
        for i, t in enumerate(tournaments, start=1):
            print(f"  [{i}] {t}")
        print("")

        choice_idx = int(input("Select Tournament by number: ").strip()) - 1
        tournament_name = tournaments[choice_idx]

        print("\nSelect schedule type:")
        print("  [1] Single Elimination")
        print("  [2] Double Elimination")

        schedule_choice = input("Select type (1 or 2): ").strip()

        # UI does NOT decide validity — just sends raw input to LL
        result = self.ll.generate_schedule(
            tournament_name=tournament_name,
            schedule_type=schedule_choice
        )

        print("\n" + str(result))
        input("\nPress Enter to continue...")




    def enter_match_result(self) -> None:
        """UI for entering a match result. """

        self.menu_ui.print_header("ENTER MATCH RESULT")
        print("Enter the match details below:\n")

        # 1. Get tournaments from LL (LL owns data/validation)
        tournaments = self.ll.get_tournament_list()

        print("Available Tournaments:")
        for i, t in enumerate(tournaments, start=1):
            print(f"  [{i}] {t}")
        print("")

        # 2. User selects tournament (UI index conversion only)
        tournament_idx = int(input("Select Tournament by number: ").strip()) - 1
        tournament_name = tournaments[tournament_idx]

        # 3. Ask LL for unfinished matches (LL decides format)
        matches = self.ll.get_unfinished_matches(tournament_name)

        print("\nUnfinished Matches:")
        for i, match in enumerate(matches, start=1):
            print(f"  [{i}] {match}")
        print("")

        # 4. User selects match, UI does not interpret match structure
        match_idx = int(input("Select Match by number: ").strip()) - 1
        selected_match = matches[match_idx] # get selected match

        # 5. Read raw scores (simple int conversion allowed)
        team_a_score = int(input("Enter Team A Score: ").strip())
        team_b_score = int(input("Enter Team B Score: ").strip())

        # 6. Forward everything directly to LL
        result = self.ll.enter_match_result(
            selected_match,
            team_a_score,
            team_b_score,
        )

        # 7. Print LL response
        print("\n" + str(result))
        input("Press Enter to continue...")

        
        



    def change_team_captain(self) -> None:
        print("TODO: Captain change function will be added later.")

    def view_statistics(self) -> None:
        print("TODO: Statistics view not implemented yet.")

    def view_schedule(self) -> None:
        print("TODO: Schedule viewing will be added later.")
    
    def create_team(self) -> None:
        print("TODO: Team creation will be implemented later.")


