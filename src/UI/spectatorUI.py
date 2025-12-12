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
        list_of_tournament_names = [tournament for tournament in tournaments]

        for i, tournament in enumerate(list_of_tournament_names, start=1):
            self.menu_ui.print_box_line(f"  [{i}] {tournament}")
        self.menu_ui.print_box_line()
        select_tournament = get_non_empty_input(" ➤ Select Tournament by number: ").strip()
        try:
            t_idx = int(select_tournament) - 1
            tournament_name = list_of_tournament_names[t_idx]
        except (ValueError, IndexError):
            print("Invalid tournament selection.")
            input("Press Enter to continue...")
            return
        # choose tournament basic validation with input helper
        
        event_name = self.ll.get_events_in_tournament(tournament_name)
        list_of_event_names = [event for event in event_name]

        for i, tournament in enumerate(list_of_event_names, start=1):
            self.menu_ui.print_box_line(f"  [{i}] {tournament}")
        self.menu_ui.print_box_line()
        select_event = get_non_empty_input(" ➤ Select Event by number: ").strip()
        try:
            e_idx = int(select_event) - 1
            event_name = list_of_event_names[e_idx]
        except (ValueError, IndexError):
            print("Invalid event selection.")
            input("Press Enter to continue...")
            return

        self.menu_ui.print_box_line() 
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")    
        self.menu_ui.print_box_bottom()

        # print the list of events in that tournament
        self.menu_ui.print_box_top()
        # Load events
        events = self.ll.get_events_in_tournament(tournament_name)
        if not events:
            print("This tournament has no events.")
            input("Press Enter to continue...")
            return

        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Event: {select_event}")
        self.menu_ui.print_box_bottom()

        # get schedule from ll for that tournament and event
        # bracket id, date, server id, teams, scores
        self.menu_ui.print_header("TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()

        schedule: list[Match] = self.ll.view_games(tournament_name, select_event)
        if not schedule:
            self.menu_ui.print_box_line(" No schedule found for this tournament/event. ")
        else:
            self.menu_ui.print_box_line(f" Schedule for {tournament_name} - {select_event}: ")    
            for match in schedule:
                self.menu_ui.print_box_line(f" Match ID: {match.match_id} ")
                self.menu_ui.print_box_line(f" - Bracket Number: {match.bracket_nr} ")
                self.menu_ui.print_box_line(f" - Date: {match.date_of_match}")
                self.menu_ui.print_box_line(f" - Time: {match.time_of_match} ")
                self.menu_ui.print_box_line(f" - Server ID: {match.server_id} ")
                self.menu_ui.print_box_line(f" - Team A: {match.team_a} vs Team B: {match.team_b} ")
                self.menu_ui.print_box_line(f" - Score: {match.team_a_score} - {match.team_b_score} ")
                self.menu_ui.print_box_line(f" - Winner: {match.winner} ")
                self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()

        input("Press Enter to continue...")
        return


    # Id, Name, Handle, Team PUBLIC INFO    
    def view_teams_and_players(self): 
        self.menu_ui.print_header("VIEW TEAMS AND PLAYERS")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a team to view: ")
        teams = self.ll.view_teams_with_no_club()
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
        team_names = selected_club.teams  
        self.menu_ui.print_box_line(f"   Teams: {', '.join(team_names)}")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        input("Press Enter to continue...")
        return


        


