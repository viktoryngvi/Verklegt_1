
class organizerUI:
    def __init__(self):
        # self.ll = LLwrapper() later when linking to logic layer
        pass

    # Organizer menu
    def menu(self):
        while True:
            print("Organizer Menu")
            print("1. Create tournament")
            print("2. Generate schedule")
            print("3. Enter match results")
            print("4. Change team captain")
            print("5. View statistics")
            print("6. View schedule/n")

            print("b. Back to main menu")

            choice = input("Select an option: ")

            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.generate_schedule()
            elif choice == '3':
                self.enter_match_result()
            elif choice == '4':
                self.change_team_captain()
            elif choice == '5':
                self.view_statistics()
            elif choice == '6':
                self.view_schedule()
            elif choice.lower() == 'b':
                break
            else:   # if the input is invalid, not in the options above. notify the user and try again
                print("Invalid choice. Please try again.")
            

    # Functionality not yet implemented, placeholders for now
    def create_tournament(self):
        print(" TODO : Create tournament functionality ")

    def generate_schedule(self):
        print(" TODO : Generate tournament schedule functionality ")

    def enter_match_result(self):
        print(" TODO : Enter results functionality ")

    def change_team_captain(self):
        print(" TODO : Change captain functionality ")

    def view_statistics(self):
        print(" TODO : View statistics functionality ")

    def view_schedule(self):
        print(" TODO : View schedule functionality ")

    
    

        