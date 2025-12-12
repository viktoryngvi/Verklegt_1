from UI.input_helper import (
    clear_screen,
    choose_from_list,
    get_non_empty_input
)

class SpectatorUI:
    def __init__(self, ll, menu_ui):
        self.ll = ll
        self.menu_ui = menu_ui

    def show_menu(self) -> str:
        clear_screen()
        self.menu_ui.print_header("SPECTATOR MENU")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Browse Tournament Information: ")
        self.menu_ui.print_box_line("  [1] View schedule")
        self.menu_ui.print_box_line("  [2] View teams and players")
        self.menu_ui.print_box_line("  [3] View clubs")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  [B] Back to main menu")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").lower()
        
    
        
        if choice not in ["1", "2", "3", "4", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, B")
            input("Press Enter to continue...")
            return self.show_menu()

        if choice == "1": 
            self.view_schedule(); 
            return "SPECTATOR_MENU"
        if choice == "2": 
            self.view_teams_and_players(); 
            return "SPECTATOR_MENU"
        if choice == "3": 
            self.view_clubs(); 
            return "SPECTATOR_MENU"
        if choice == "b": 
            return "MAIN_MENU"

    def view_schedule(self): 
        self.menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a tournament to view its schedule: ")
        self.menu_ui.print_box_line()

        # Get list of tournaments from LL
        tournaments = self.ll.get_tournament_list()  

        # choose tournament basic validation with input helper
        tournament_name = choose_from_list("Select Tournament by number: ", tournaments)  

        self.menu_ui.print_box_line() 
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")    
        self.menu_ui.print_box_bottom()

        # print the list of events in that tournament
        self.menu_ui.print_box_top()
        events_in_tournament = choose_from_list("Select Event by number: ", self.ll.get_events_in_tournament(tournament_name))
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Event: {events_in_tournament}")
    
        self.menu_ui.print_box_bottom()
        # get schedule from ll for that tournament and event
        self.menu_ui.print_header("TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        
        schedule = self.ll.get_tournament_schedule(tournament_name, events_in_tournament)
        if not schedule:
            print("No schedule found for this tournament/event.")
        else:
            print(f"Schedule for {tournament_name} - {events_in_tournament}:")
            for match in schedule:
                print(f" - {match}")
        input("Press Enter to continue...")
        return


    # Id, Name, Handle, Team PUBLIC INFO    
    def view_teams_and_players(self): 
        self.menu_ui.print_header("VIEW TEAMS AND PLAYERS")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a team to view: ")
        teams = self.ll.view_all_teams()
        if not teams:
            self.menu_ui.print_box_line(" No teams found. ")
            self.menu_ui.print_box_bottom()
            input("Press Enter to continue...")
            return
        
        for team in teams:
            self.menu_ui.print_box_line(f" - {team.name} (Captain: {team.captain}) ")
        self.menu_ui.print_box_bottom()

        self.menu_ui.print_box_top()
        team_name = get_non_empty_input(" Enter team name: ").strip()
        self.menu_ui.print_box_bottom()
        team_players = self.ll.get_players_in_team(team_name)
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Players in team {team_name}: ")
        if team_players:
            for player in team_players:
                self.menu_ui.print_box_line(f" - Id: {player.id}")
                self.menu_ui.print_box_line(f"   Name: {player.name}")
                self.menu_ui.print_box_line(f"   Handle: {player.handle}")
                self.menu_ui.print_box_line(f"   Team: {player.team}")

        else:
            self.menu_ui.print_box_line(" No players found or team does not exist. ")
        self.menu_ui.print_box_bottom()
        input("Press Enter to continue...")
        return
        

    # name, home_town, country, color, teams
    def view_clubs(self): 
        self.menu_ui.print_header("VIEW CLUBS")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" List of Clubs: ")
        clubs = self.ll.load_clubs()
        for club in clubs:
            self.menu_ui.print_box_line(f" - {club.name} ")
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()    

        user_input = get_non_empty_input(" Enter club name to view details: ").strip().lower()
        
        selected_club = None
        for club in clubs:
            if club.name.lower() == user_input:
                selected_club = club
                break
        
        if not selected_club:
            print("Club not found.")
            input("Press Enter to continue...")
            return
        

        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" Club Details for: {selected_club.name} ")

        
        self.menu_ui.print_box_line(f" - Club Name: {selected_club.name}")
        self.menu_ui.print_box_line(f"   Home Town: {selected_club.home_town}")
        self.menu_ui.print_box_line(f"   Country: {selected_club.country}")
        self.menu_ui.print_box_line(f"   Colors: {', '.join(selected_club.colors)}")            
        team_names = [team.name for team in selected_club.teams]
        self.menu_ui.print_box_line(f"   Teams: {', '.join(team_names)}")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        input("Press Enter to continue...")
        return


        


