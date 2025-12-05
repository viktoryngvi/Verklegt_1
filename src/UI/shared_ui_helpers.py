from UI.input_helper import choose_from_list


def view_teams(ll, menu_ui):
    menu_ui.print_header("VIEW TEAM")
    print("Select the team to view: ")

    teams = ll.get_teams()
    if not teams:
        print("No teams found.")
        input("Press Enter to continue...")
        return
    select_team = choose_from_list("Enter the number of the team: ", teams)

    print(f"You selected to view team: {select_team}")
    players = ll.get_players_in_team(select_team)
    if not players:
        print("No players found in this team.")
    else:
        print(f"Players in team {select_team}:")
        for player in players:
            print(f" - {player}")
    input("Press Enter to continue...")

def create_team(ll, menu_ui):
    menu_ui.print_header("CREATE TEAM")
    pass

def view_schedule(ll, menu_ui):
    menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
    print("Select a tournament to view its schedule:\n")

    # Get list of tournaments from LL
    tournaments = ll.get_tournament_list()  

    # choose tournament basic validation with input helper
    tournament_name = choose_from_list("Select Tournament by number: ", tournaments)   

    # get schedule from LL
    schedule = ll.get_tournament_schedule(tournament_name)   
    print(f"\nSchedule for {tournament_name}:\n")
    print(schedule)
    input("\nPress Enter to continue...")
    
