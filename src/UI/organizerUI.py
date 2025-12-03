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

        print("\n==== Organizer Menu ====")
        print("1. Create tournament")
        print("2. Generate schedule")
        print("3. Enter match result")
        print("4. Change team captain")
        print("5. View statistics")
        print("6. View schedule")
        print("b. Back to main menu")

        # Use the shared menu input validation function
        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "5", "6", "b"])

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
        """Collect all tournament information and create a tournament in LL."""

        print("\n==== Create Tournament ====")

        # User selects the tournament type (knockout or double elimination)
        t_type = self._select_tournament_type()
        if not t_type:
            print("Cancelled.")
            return

        # Collect all the data the user must type in
        info = self._collect_tournament_info()
        if info is None:
            print("Cancelled.")
            return

        # Validate date formats + check the tournament is exactly 3 days long
        ok, msg = self._validate_tournament_info(info)
        if not ok:
            print(f"Error: {msg}")
            return

        # Check if LL has a function to check if the tournament name is already used
        if hasattr(self.ll, "tournament_exists") and self.ll.tournament_exists(info["name"]):
            print("Error: Tournament name already exists.")
            return

        # Try to create the tournament using the LL function
        try:
            self.ll.create_tournament(
                name=info["name"],
                location=info["location"],
                start_date=info["start_date"],
                end_date=info["end_date"],
                contact={
                    "name": info["contact_name"],
                    "phone": info["contact_phone"],
                    "address": info["contact_address"],
                    "dob": info["contact_dob"],
                    "email": info["contact_email"]
                },
                tournament_type=t_type
            )

            # If LL supports automatically registering teams for tournaments
            if hasattr(self.ll, "register_teams_for_tournament"):
                registered = self.ll.register_teams_for_tournament(info["name"])
            else:
                registered = 0

            print(f"Tournament '{info['name']}'has been created. {registered} teams registered.")

        except Exception as e:
            # A general error handler in case LL throws something unexpected
            print(f"Failed to create tournament: {e}")


    # ================================
    # SELECT TOURNAMENT TYPE
    # ================================
    def _select_tournament_type(self) -> Optional[str]:
        """Let user choose tournament type and return the type string."""
        
        print("\nSelect Tournament Type:")
        print("1. Knockout")
        print("2. Double elimination")
        print("b. Back")

        choice = self.menu_ui._prompt_choice(["1", "2", "b"])

        if choice == "1":
            return "Knockout"
        if choice == "2":
            return "Double elimination"
        return None


    # ================================
    # COLLECT TOURNAMENT INFO
    # ================================
    def _collect_tournament_info(self) -> Dict[str, str]:
        """Collect the basic tournament info from user input."""

        name = get_required_input("Tournament Name: ")
        location = get_required_input("Location: ")
        start_date_str = get_date_input("Start Date (YYYY-MM-DD): ")
        end_date_str = get_date_input("End Date (YYYY-MM-DD): ")

        print("\n-- Contact Person --")
        contact_name = get_required_input("Name: ")
        contact_phone = get_phone_input("Phone: ")
        contact_address = get_required_input("Address: ")
        contact_dob = get_date_input("DOB (YYYY-MM-DD): ")
        contact_email = get_email_input("Email: ")

        return {
            "name": name,
            "location": location,
            "start_date": start_date_str,
            "end_date": end_date_str,
            "contact_name": contact_name,
            "contact_phone": contact_phone,
            "contact_address": contact_address,
            "contact_dob": contact_dob,
            "contact_email": contact_email
        }


    # ================================
    # VALIDATE TOURNAMENT INFO 
    # ================================
    def _validate_tournament_info(self, info: Dict[str, str]) -> Tuple[bool, str]:
        """Validate date formats + enforce tournament must be 3 days long."""
        return validate_3_day_duration(info["start_date"], info["end_date"])


    # ================================
    # PLACEHOLDER FUNCTIONS
    # ================================
    def generate_schedule(self) -> None:
        print("TODO: Schedule generation will be handled later by LL.")

    def enter_match_result(self) -> None:
        print("TODO: Match result entry will be implemented later.")

    def change_team_captain(self) -> None:
        print("TODO: Captain change function will be added later.")

    def view_statistics(self) -> None:
        print("TODO: Statistics view not implemented yet.")

    def view_schedule(self) -> None:
        print("TODO: Schedule viewing will be added later.")
