from UI.organizerUI import organizerUI
from UI.captainUI import captainUI
from UI.playerUI import playerUi
from UI.spectatorUI import spectatorUI


class MainUI:
    def __init__(self):
        self.organizer_ui = organizerUI()
        self.captain_ui = captainUI()
        self.player_ui = playerUi()
        self.spectator_ui = spectatorUI()
    
    
    # Main menu 
    def menu(self):
        while True:
            print("================================")
            print("RU’s e-Sport Extravaganza")
            print("================================")
            print("Main Menu:")
            print("1. Organizer")
            print("2. Captain")
            print("3. Player")
            print("4. Spectator")

            print("q. Quit")
            # select option and redirect to respective UI
            choice = input("Select an option: ")

            if choice == '1':
                self.organizer_ui.menu()
            elif choice == '2':
                self.captain_ui.menu()
            elif choice == '3':
                self.player_ui.menu()
            elif choice == '4':
                self.spectator_ui.menu()
            elif choice.lower() == 'q':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")




        




