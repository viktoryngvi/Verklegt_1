from UI.input_helper import (
    clear_screen,
)


class MenuUI:

    box_width = 120

    def print_box_top(self):
        print("╔" + "═" * (self.box_width - 2) + "╗")
        
    def print_box_bottom(self):
        print("╚" + "═" * (self.box_width - 2) + "╝")

    def print_box_line(self, text=""):
        print("║ " + text.ljust(self.box_width - 4) + " ║")


    
    def print_header(self, title: str):
        clear_screen()
        try:
            print("\n")
            print(" ███████████   █████  █████  ██            ██████████             █████████  ███████████     ███████    ███████████   ███████████                              ")
            print("░░███░░░░░███ ░░███  ░░███  ███           ░░███░░░░░█            ███░░░░░███░░███░░░░░███  ███░░░░░███ ░░███░░░░░███ ░█░░░███░░░█                              ")
            print(" ░███    ░███  ░███   ░███ ░░░   █████     ░███  █ ░            ░███    ░░░  ░███    ░███ ███     ░░███ ░███    ░███ ░   ░███  ░                               ")
            print(" ░██████████   ░███   ░███      ███░░      ░██████    ██████████░░█████████  ░██████████ ░███      ░███ ░██████████      ░███                                  ")
            print(" ░███░░░░░███  ░███   ░███     ░░█████     ░███░░█   ░░░░░░░░░░  ░░░░░░░░███ ░███░░░░░░  ░███      ░███ ░███░░░░░███     ░███                                  ")
            print(" ░███    ░███  ░███   ░███      ░░░░███    ░███ ░   █            ███    ░███ ░███        ░░███     ███  ░███    ░███     ░███                                  ")
            print(" █████   █████ ░░████████       ██████     ██████████           ░░█████████  █████        ░░░███████░   █████   █████    █████                                  ")
            print("░░░░░   ░░░░░   ░░░░░░░░       ░░░░░░     ░░░░░░░░░░             ░░░░░░░░░  ░░░░░           ░░░░░░░    ░░░░░   ░░░░░    ░░░░░                                  ")
            print()
            print(" ██████████ █████ █████ ███████████ ███████████     █████████   █████   █████   █████████     █████████    █████████   ██████   █████ ███████████   █████████  ")
            print("░░███░░░░░█░░███ ░░███ ░█░░░███░░░█░░███░░░░░███   ███░░░░░███ ░░███   ░░███   ███░░░░░███   ███░░░░░███  ███░░░░░███ ░░██████ ░░███ ░█░░░░░░███   ███░░░░░███ ")
            print(" ░███  █ ░  ░░███ ███  ░   ░███  ░  ░███    ░███  ░███    ░███  ░███    ░███  ░███    ░███  ███     ░░░  ░███    ░███  ░███░███ ░███ ░     ███░   ░███    ░███ ")
            print(" ░██████     ░░█████       ░███     ░██████████   ░███████████  ░███    ░███  ░███████████ ░███          ░███████████  ░███░░███░███      ███     ░███████████ ")
            print(" ░███░░█      ███░███      ░███     ░███░░░░░███  ░███░░░░░███  ░░███   ███   ░███░░░░░███ ░███    █████ ░███░░░░░███  ░███ ░░██████     ███      ░███░░░░░███ ")
            print(" ░███ ░   █  ███ ░░███     ░███     ░███    ░███  ░███    ░███   ░░░█████░    ░███    ░███ ░░███  ░░███  ░███    ░███  ░███  ░░█████   ████     █ ░███    ░███ ")
            print(" ██████████ █████ █████    █████    █████   █████ █████   █████    ░░███      █████   █████ ░░█████████  █████   █████ █████  ░░█████ ███████████ █████   █████")
            print("░░░░░░░░░░ ░░░░░ ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░   ░░░░░      ░░░      ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░   ░░░░░ ")
            print()
            print()
            print()
            self.print_box_top()
            centered = f"{title.center(self.box_width - 4)}"
            print(centered)
            self.print_box_bottom()
        except Exception:
            # Fallback without unicode/ANSI if terminal doesn't support it
            print("="*80)
            print("RU's e-Sport Extravaganza")
            print("="*80)
            print(title.center(80))
        print()

    def _prompt_choice(self, valid_choices):
        """Helper method for other menus that still use it."""
        valid = [c.lower() for c in valid_choices]
        while True:
            choice = input("Select an option: ").lower()
            if choice in valid:
                return choice
            print(f"Invalid choice. Valid options: {', '.join(valid_choices)}")

    # MAIN MENU
    def main_menu(self) -> str:
        self.print_header("MAIN MENU")
        self.print_box_top()
        self.print_box_line()
        self.print_box_line("  [1] Organizer   - Manage tournaments ")
        self.print_box_line("  [2] Captain     - Manage teams and players")
        self.print_box_line("  [3] Player      - View your profile and team")
        self.print_box_line("  [4] Spectator   - View tournament information")
        self.print_box_line()
        self.print_box_line("  [Q] Quit")
        self.print_box_line()
        self.print_box_bottom() 
        choice = input(" ➤ Select an option: ").lower()
    
        
        
        if choice not in ['1', '2', '3', '4', 'q']:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, Q")
            input("Press Enter to continue...")
            return self.main_menu()

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