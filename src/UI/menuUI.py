class MenuUI:
    def _prompt_choice(self, valid_choices):
        valid = [c.lower() for c in valid_choices]

        while True:
            choice = input("Select an option: ").lower()
            if choice in valid:
                return choice
            print(f"Invalid choice. Valid options: {', '.join(valid_choices)}")

    # MAIN MENU
    def main_menu(self) -> str:
        print("\n==== Main Menu ====")
        print("1. Organizer")
        print("2. Captain")
        print("3. Player")
        print("4. Spectator")
        print("q. Quit")

        choice = self._prompt_choice(['1', '2', '3', '4', 'q'])

        if choice == '1': 
            return "ORGANIZER_MENU"
        if choice == '2': 
            return "CAPTAIN_MENU"
        if choice == '3': 
            return "PLAYER_MENU"
        if choice == '4': 
            return "SPECTATOR_MENU"
        if choice == 'q': 
            return "EXIT"