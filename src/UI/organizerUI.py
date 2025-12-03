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
        print("\n==== Create Tournament ====")

        name = input("Tournament name: ").strip()
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()
        teams_raw = input("Teams (comma-separated): ").strip()

        teams = [t.strip() for t in teams_raw.split(",") if t.strip()]

        if not name:
            print("Name is required. Returning to menu.")
            return

        # UI-only handoff. If LL is ready, try to call it; otherwise print a placeholder.
        try:
            if hasattr(self.ll, "create_tournament"):
                result = self.ll.create_tournament(name=name, start_date=start_date, end_date=end_date, teams=teams)
                if isinstance(result, list):
                    print("Tournament could not be created. Errors:")
                    for err in result:
                        print(f" - {err}")
                else:
                    print("Tournament creation submitted to LL.")
            else:
                print("LL not implemented yet. Collected data:")
                print(f" - name: {name}")
                print(f" - start_date: {start_date}")
                print(f" - end_date: {end_date}")
                print(f" - teams: {', '.join(teams) if teams else '(none)'}")
        except Exception as e:
            print(f"Unexpected error handing off to LL: {e}")

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
