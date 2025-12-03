from models.player import Player



class CaptainUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        print("\n==== Captain Menu ====")
        print("1. Create player")
        print("2. Edit player info")
        print("3. View team")
        print("4. Change team captain")
        print("5. View schedule")
        print("b. Back to main menu")

        choice = self.menu_ui._prompt_choice(["1", "2", "3", "4", "5", "b"])

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
            self.view_schedule(); 
            return "CAPTAIN_MENU"
        if choice == "b": 
            return "MAIN_MENU"
    

    def create_player(self):
        print("\n==== Create Player ====")

        # Collect fields from user (UI does only raw input)
        name = input("Full name: ").strip()
        phone = input("Phone: ").strip()
        address = input("Address: ").strip()
        dob = input("DOB (YYYY-MM-DD): ").strip()
        email = input("Email: ").strip()
        handle = input("Handle (unique): ").strip()

        # ID must not be asked by UI — let LL/DL handle it.
        # So we send id=None
        player = Player(
            name=name,
            phone=phone,
            address=address,
            dob=dob,
            email=email,
            id=None,
            handle=handle
        )

        # Call LL through wrapper
        try:
            result = self.ll.create_player(player)
        except Exception as e:
            print(f"Unexpected error creating player: {e}")
            return "CAPTAIN_MENU"

        # LL returns list of errors OR a success string
        if isinstance(result, list):  # validation failed
            print("Player could not be created. Errors:")
            for err in result:
                print(f" - {err}")
        else:
            print("Player created successfully!")

        return "CAPTAIN_MENU"

    def edit_player_info(self): 
        print("TODO")
    def view_team(self): 
        print("TODO")
    def change_team_captain(self): 
        print("TODO")
    def view_schedule(self): 
        print("TODO")
