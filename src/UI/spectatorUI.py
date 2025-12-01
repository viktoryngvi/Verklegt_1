
class spectatorUI:
    def __init__(self):
        # self.ll = LLwrapper() later when linking to logic layer
        pass

    # Spectator menu
    def menu(self):
        while True:
            print("Spectator Menu")
            print("1. View schedule")
            print("2. View teams")
            print("3. View players")
            print("4. View clubs/n")

            print("b. Back to main menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.view_schedule()
            elif choice == '2':
                self.view_teams()
            elif choice == '3':
                self.view_players()
            elif choice == '4':
                self.view_clubs()
            elif choice.lower() == 'b':
                break
            else:   # if the input is invalid, not in the options above. notify the user and try again
                print("Invalid choice. Please try again.")

    def view_schedule(self):
        print(" TODO : View schedule functionality ")
    def view_teams(self):
        print(" TODO : View teams functionality ")
    def view_players(self):
        print(" TODO : View players functionality ")
    def view_clubs(self):
        print(" TODO : View clubs functionality ")

        


