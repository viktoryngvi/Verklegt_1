from typing import Any, Optional, Dict, Tuple
from UI.input_helper import (
    get_non_empty_input,
    #get_integer_input,
    get_choice_input,
    choose_from_list,
    clear_screen,
)
from models.tournament import Tournament
from models.event import Event
from LL.logical_wraper import LLWrapper
from models.team import Team
from models.club import Club
from models.player import Player

class OrganizerUI:
    def __init__(self, ll: LLWrapper, menu_ui: Any):
        # Store references to logic layer and menu helper class
        self.ll = ll
        self.menu_ui = menu_ui

   
    def show_menu(self) -> str:
        """Show the organizer menu and return the next menu state."""
        # Clear previous screen / main menu
        clear_screen()  

        self.menu_ui.print_header("ORGANIZER MENU")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Tournmaent Management: ")
        self.menu_ui.print_box_line("  [1] Create tournament ")
        self.menu_ui.print_box_line("  [2] Generate schedule ")
        self.menu_ui.print_box_line("  [3] Create Event ")
        self.menu_ui.print_box_line("  [4] Register team into event ")
        self.menu_ui.print_box_line("  [5] Enter match result ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Team Management: ")
        self.menu_ui.print_box_line("  [6] Change team captain ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Reports: ")
        self.menu_ui.print_box_line("  [7] View statistics ")
        self.menu_ui.print_box_line("  [8] View schedule ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  Club Management: ")
        self.menu_ui.print_box_line("  [9] Create team ")
        self.menu_ui.print_box_line("  [10] Create club ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line("  [B] Back to main menu ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        choice = input(" ➤ Select an option: ").lower()
        

        
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "b"]:
            print(f"Invalid choice. Valid options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, B")
            input("Press Enter to continue...")
            return self.show_menu()

        # Based on the choice, call a function and return the next menu state
        if choice == "1":
            self.create_tournament()
            return "ORGANIZER_MENU"
        if choice == "2":
            self.generate_schedule()
            return "ORGANIZER_MENU"
        if choice == "3":
            self.create_event()
            return "ORGANIZER_MENU"
        if choice == "4":
            self.Register_team_into_event()
            return "ORGANIZER_MENU"
        if choice == "5":
            self.enter_match_result()
            return "ORGANIZER_MENU"
        if choice == "6":
            self.change_team_captain()
            return "ORGANIZER_MENU"
        if choice == "7":
            self.view_statistics()
            return "ORGANIZER_MENU"
        if choice == "8":
            self.view_schedule()
            return "ORGANIZER_MENU"
        if choice == "9":
            self.create_team()
            return "ORGANIZER_MENU"
        if choice == "10":
            self.register_club()
            return "ORGANIZER_MENU"
        if choice == "b":
            return "MAIN_MENU"


    
    def create_tournament(self):
        """Create a new tournament by collecting info and sending it to LL."""

        self.menu_ui.print_header("CREATE TOURNAMENT")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Please enter the following details to create a new tournament: ")
        self.menu_ui.print_box_line()

        # Collect input using input helper functions for basic validation
        name = get_non_empty_input("\t-  Tournament Name: ")
        location = get_non_empty_input("\t-  Location: ")
        start_date = get_non_empty_input("\t-  Start Date (YYYY-MM-DD): ")
        end_date = get_non_empty_input("\t-  End Date (YYYY-MM-DD): ")
        self.menu_ui.print_box_line()


        self.menu_ui.print_box_line("Contact Person Information: ")
        self.menu_ui.print_box_line()
        
        contact_name = get_non_empty_input("\t-  Full Name: ")
        contact_email = get_non_empty_input("\t-  Email: ")
        contact_phone = get_non_empty_input("\t-  Phone: ")
        self.menu_ui.print_box_bottom()

        # Forward everything directly to LL 
        result = Tournament(
            name,
            location,
            start_date,
            end_date,
            contact_name,
            contact_email,
            contact_phone
        )
        result = self.ll.create_tournament(result)

        if result:
            print(("\n" + "Tournament Created!"))
        else:
            print(("\n" + "Tournament Could Not Be Created!"))
        # Print whatever LL returns
        # print("\n" + str(result))
        input("Press Enter to continue...")

# event name, game type, start date, end date, teams registered

    def create_event(self):
        """Create a new event within a tournament."""
        self.menu_ui.print_header("CREATE EVENT")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Please enter the following details to create a new event")
        self.menu_ui.print_box_line()
    
        self.menu_ui.print_box_line(" Select the tournament for the event: ")


        # get a list of the tournaments created
        tournaments = self.ll.get_tournament_list()  
        tournament_name = choose_from_list(" Select Tournament by number: ", tournaments)
        self.menu_ui.print_box_bottom()
        
        self.menu_ui.print_box_top()
        event_name = get_non_empty_input("\tEvent name: ").strip()
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select the event type: ")
        event_types = self.ll.event_types()
        event_type = choose_from_list(" ➤ Select one type: ", event_types) 
        self.menu_ui.print_box_line(f" You selected event type: {event_type}")
        self.menu_ui.print_box_bottom()

        # get start and end date for the event
        self.menu_ui.print_header("EVENT DATES")
        self.menu_ui.print_box_top()
        start_date = get_non_empty_input("\tStart Date (YYYY-MM-DD): ").strip()
        end_date = get_non_empty_input("\tEnd Date (YYYY-MM-DD): ").strip()
        self.menu_ui.print_box_bottom()

        results = Event(
            event_name,
            event_type,
            tournament_name,
            start_date,
            end_date,
            team_name = None,
            event_id = None
        )
        results = self.ll.create_empty_event(results)
        
        print("\n" + str(results))
        input("Press Enter to continue...")

    def Register_team_into_event(self):
        self.menu_ui.print_header("Register Teams for Event")

        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a tournament: ")
        # get a list of the tournaments created
        tournament = self.ll.get_tournament_list()  
        tournament_name = choose_from_list(" Select Tournament by number: ", tournament)
        self.menu_ui.print_box_bottom()

        # select event
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select an event to register teams for: ")
        events = self.ll.get_events_in_tournament(tournament_name)
        event_name = choose_from_list("Select event:", events)
        self.menu_ui.print_box_bottom()

        # register teams
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select teams to register for this event: ")
        # Register teams  for the event, get the list of teams and pick what teams to register by number
        max_teams = 16
        registered_teams = []

        teams = self.ll.view_all_teams()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(" Available Teams: ")
        for i, team in enumerate(teams, start=1):
            print(f"  [{i}] {team.name}")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()
        
        while True:
            team_index = get_integer_input(" Enter the number of the team to register: ") - 1

            if team_index < 0 or team_index >= len(teams):
                print("Invalid team number. Try again.")
                continue
            team_name = teams[team_index]
            if team_name in registered_teams:
                print(f"Team {team_name} is already registered.")
                continue
            else:
                registered_teams.append(team_name)
            
            print(f"\n{len(registered_teams)}/{max_teams} teams registered.")
            print("Registered Teams: " + ", ".join(registered_teams))

            if len(registered_teams) >= max_teams:
                print("Maximum number of teams registered.")
                break
            more = get_choice_input(" Register another team? (y/n): ", ["y", "n"])
            if more == "n":
                break

        results = self.ll.register_teams_into_event(
            tournament_name=tournament_name,
            event_name=event_name,
            team_names=registered_teams
        )
        print("\n" + str(results))
        input("Press Enter to continue...")
        
    """
    list of events
    write team into event
    """


 
    def generate_schedule(self):
    
        self.menu_ui.print_header("GENERATE TOURNAMENT SCHEDULE")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Choose a tournament to generate a schedule for: ")
        self.menu_ui.print_box_line()

        tournaments = self.ll.get_tournament_list()  # get tournaments from LL
        self.menu_ui.print_box_line(" Available Tournaments: ")

        tournament_name = choose_from_list(" Select Tournament by number: ", tournaments) 
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()  
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")
        self.menu_ui.print_box_bottom() 

        # get events in that tournament
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select an event to generate the schedule for: ")
        events_in_tournament = choose_from_list(" Select Event by number: ", self.ll.get_events_in_tournament(tournament_name))
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Event: {events_in_tournament} ")
        self.menu_ui.print_box_bottom()

        # send to LL to generate schedule
        result = self.ll.generate_schedule(
            tournament_name=tournament_name,
            event_name=events_in_tournament,
        )

        print("\n" + str(result))
        input("Press Enter to continue...")



    def enter_match_result(self):
        """UI for entering a match result. """

        self.menu_ui.print_header("ENTER MATCH RESULT")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select a tournament: ")

        # get tournaments from LL 
        tournaments = self.ll.get_tournament_list()
        tournament_name = choose_from_list(" Select Tournament by number: ", tournaments)
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(f" You selected Tournament: {tournament_name} ")
        self.menu_ui.print_box_bottom()

        # get events in that tournament
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select an event: ")
        events = self.ll.get_events_in_tournament(tournament_name)

        event_name = choose_from_list(" Select Event by number: ", events)
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom() 

        # enter match result for that tournament / event
        self.menu_ui.print_header(f"ENTER MATCH RESULT - {tournament_name} / {event_name}")
        self.menu_ui.print_box_top()

        #  Ask LL for unfinished matches in that tournament
        matches = self.ll.get_unfinished_matches(event_name, tournament_name)
        if not matches:
            print("No unfinished matches found for this tournament/event.")
            input("Press Enter to continue...")
            return
        

        self.menu_ui.print_box_line(" Select a match to enter results for: ")

        # list of matches that have not been entered yet
        selected_match = choose_from_list(" Select Match by number: ", matches)      

        # get scores and make sure they are integers with input helper
        self.menu_ui.print_box_line("Enter the scores for the match: ")
        team_a_score = get_integer_input("\t-  Enter Team A Score: ") 
        team_b_score = get_integer_input("\t-  Enter Team B Score: ")
        self.menu_ui.print_box_bottom()

        # Forward everything directly to LL
        result = self.ll.enter_match_result(
            selected_match,
            team_a_score,
            team_b_score,
            tournament_name,
            event_name,
        )

        #  Print LL response
        print("\n" + str(result))
        input("Press Enter to continue...")


    def change_team_captain(self):
        self.menu_ui.print_header("CHANGE TEAM CAPTAIN")
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" To change the team captain, please follow the steps below: ")
        self.menu_ui.print_box_bottom()
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(" Select the team you want to change the captain for: ")
        self.menu_ui.print_box_line()
        # get the list of teams from LL 
        teams = self.ll.view_all_teams()

        # check if there are any teams
        if not teams:
            print("No teams found.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        # let user select a team
        for team in teams:
            self.menu_ui.print_box_line(f" - {team.name}")
        
        self.menu_ui.print_box_line()
        select_team = input(" Enter the team name: ").strip()
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_bottom()



        # get players in that team
        players:list[Player] = self.ll.view_all_players_in_team(select_team)
        # check if there are any players
        if not players:
            print("No players found in this team.")
            input("Press Enter to continue...")
            return "CAPTAIN_MENU"
        
        
        self.menu_ui.print_box_top()
        self.menu_ui.print_box_line(f" You selected team: {select_team} ")
        self.menu_ui.print_box_line()
        self.menu_ui.print_box_line(" Select the new captain from the team players: ")


        # let user select a player to be the new captain
        for player in players:
            self.menu_ui.print_box_line(f" - {player.handle}")
        new_captain_handle = input(" Enter the player handle: ").strip().lower()

        self.menu_ui.print_box_line(f" You selected player: {new_captain_handle} as the new captain. ")
        self.menu_ui.print_box_bottom()
        
        # send to LL to update
        result = self.ll.update_team_captain(
            select_team,
            new_captain_handle
            )
        
        print("")
        print(result)
        input("Press Enter to continue...")


    def view_statistics(self):
        pass
        


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
        # Load events
        events = self.ll.get_events_in_tournament(tournament_name)

       
        if not events or events == "None" or events == ["None"]:
            self.menu_ui.print_box_line()
            self.menu_ui.print_box_line(" This tournament has no events.")
            self.menu_ui.print_box_bottom()
            input("Press Enter to continue...")
            return

       
        events_in_tournament = choose_from_list("Select Event by number: ", events)

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

    
    def create_team(self):
        self.menu_ui.print_header("CREATE TEAM")

        # team name
        self.menu_ui.print_box_top()
        team_name = input("\tTeam Name: ").strip()
        self.menu_ui.print_box_bottom()

        # captain handle
        self.menu_ui.print_box_top()
        captain_handle = input("\tCaptain Handle: ").strip().lower()
        self.menu_ui.print_box_bottom()

        # select players
        self.menu_ui.print_box_top()
        # need list of all players without a team
        all_players = self.ll.players_team_none()  

        # select players for the team  
        print(" Select players: ")
        
        for player in all_players:
            player_id, name, handle = player
            print(f" - [{player_id}] {name} ({handle})")
        selected_players = input("\tEnter player id's separated by commas: ").strip().lower()

    
        self.menu_ui.print_box_bottom()
        
        cap_id = self.ll.take_handle_return_id(captain_handle)
        # send to ll to create team
        player_ids = self.ll.take_list_of_players_return_list_of_ids(selected_players)
        result = self.ll.create_team(team_name, cap_id, player_ids)

        print(result)
        input("Press Enter to continue...")

    def register_club(self):
        self.menu_ui.print_header("REGISTER NEW CLUB")

        # Club name
        self.menu_ui.print_box_top()
        club_name = input("\tClub Name: ").strip()
        self.menu_ui.print_box_bottom()

        # Club home town
        self.menu_ui.print_box_top()
        club_home_town = input("\tHome Town: ").strip()
        self.menu_ui.print_box_bottom()

        # Club country
        self.menu_ui.print_box_top()
        club_country = input("\tCountry: ").strip()
        self.menu_ui.print_box_bottom()

        # Club colors
        self.menu_ui.print_box_top()
        club_colors = input("\tClub Colors (comma separated): ").strip()
        self.menu_ui.print_box_bottom()

        # Select teams to add to this club
        self.menu_ui.print_box_top()
        all_teams = self.ll.view_all_teams()   
        listi = []
        all: Team
        for all in all_teams:
            listi.append(all.name)
        selected_teams = choose_from_list(
            "Select teams to add (comma separated for multiple): ",
            listi,
            allow_multiple=True
        )
        self.menu_ui.print_box_bottom()

        # Send to ll
        result = Club(
            club_name,
            club_home_town,
            club_country,
            club_colors,
            selected_teams
        )

        result = self.ll.create_club(result)

        print(result)
        input("Press Enter to continue...")


    

