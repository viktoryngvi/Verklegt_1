

class captainUI:
    def __init__(self):
        # self.ll = LLwrapper()  later when linking to logic layer
        pass

    # Captain menu
    def menu(self):
        while True:
            print("Captain Menu")
            print("1. Create player")
            print("2. Edit player info")
            print("3. View team")
            print("4. Change team captain")
            print("5. View schedule/n")

            print("b. Back to main menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.create_player()
            elif choice == '2':
                self.edit_player()
            elif choice == '3':
                self.view_team()
            elif choice == '4':
                self.change_team_captain()
            elif choice == '5':
                self.view_schedule()
            elif choice.lower() == 'b':
                break
            else:   # if the input is invalid, not in the options above. notify the user and try again
                print("Invalid choice. Please try again.")

    
    def create_player(self):
        print(" TODO : Create player functionality ")

    def edit_player(self):
        print(" TODO : Edit player info functionality ")

    def view_team(self):
        print(" TODO : View team functionality ")

    def change_team_captain(self):
        print(" TODO : Change captain functionality ")

    def view_schedule(self):
        print(" TODO : View schedule functionality ")


    