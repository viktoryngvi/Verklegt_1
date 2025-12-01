
class playerUi:
    def __init__(self):
        # self.ll = LLwrapper() later when linking to logic layer
        pass

    # Player menu
    def menu(self):
        while True:
            print("Player Menu")
            print("1. View profile")
            print("2. Edit my info")
            print("3. View team")
            print("4. View schedule/n")

            print("b. Back to main menu")


            choice = input("Select an option: ")

            if choice == '1':
                self.show_profile()
            elif choice == '2': 
                self.edit_player()
            elif choice == '3':
                self.view_team()
            elif choice == '4':
                self.view_schedule()
            elif choice.lower() == 'b':
                break
            else:   # if the input is invalid, not in the options above. notify the user and try again
                print("Invalid choice. Please try again.")  
    

    def show_profile(self):
        print(" TODO : View profile functionality ")

    def edit_player(self):
        print(" TODO : Edit my info functionality ")
    
    def view_team(self):
        print(" TODO : View team functionality ")
    
    def view_schedule(self):
        print(" TODO : View schedule functionality ")
    
