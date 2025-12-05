class MenuUI:
    def print_header(self, title: str):
        try:
            print("\n")
            print("                ██████╗ ██╗   ██╗██╗███████╗    ███████╗      ███████╗██████╗  ██████╗ ██████╗ ████████╗")
            print("                ██╔══██╗██║   ██║╚═╝██╔════╝    ██╔════╝      ██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝")
            print("                ██████╔╝██║   ██║   ███████╗    █████╗  █████╗███████╗██████╔╝██║   ██║██████╔╝   ██║")
            print("                ██╔══██╗██║   ██║   ╚════██║    ██╔══╝  ╚════╝╚════██║██╔═══╝ ██║   ██║██╔══██╗   ██║")
            print("                ██║  ██║╚██████╔╝   ███████║    ███████╗      ███████║██║     ╚██████╔╝██║  ██║   ██║")
            print("                ╚═╝  ╚═╝ ╚═════╝    ╚══════╝    ╚══════╝      ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝")
            print()
            print("                                       ★ EXTRAVAGANZA ★")
            print()
            print("                ╔════════════════════════════════════════════════════════════════════════╗")
            print("                ║" + title.center(72) + "║")
            print("                ╠════════════════════════════════════════════════════════════════════════╣")
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
        print("                ║                                                                        ║")
        print("                ║  [1] Organizer   - Manage tournaments                                  ║")
        print("                ║  [2] Captain     - Manage teams and players                            ║")
        print("                ║  [3] Player      - View your profile and team                          ║")
        print("                ║  [4] Spectator   - View tournament information                         ║")
        print("                ║                                                                        ║")
        print("                ║  [Q] Quit                                                              ║")
        print("                ║                                                                        ║")
        print("                ╠════════════════════════════════════════════════════════════════════════╣")
        print("                ║  ➤ Select an option: ", end="", flush=True)
        
        choice = input().lower()
        
        print("                ╚════════════════════════════════════════════════════════════════════════╝")
        
        
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