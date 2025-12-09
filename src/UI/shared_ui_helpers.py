from UI.input_helper import choose_from_list


def view_teams(ll, menu_ui):
    menu_ui.print_header("VIEW TEAM")
    print("Select the team to view: ")

    teams = ll.view_all_teams()
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
"""

"""
def view_schedule(ll, menu_ui):
    menu_ui.print_header("VIEW TOURNAMENT SCHEDULE")
    print("Select a tournament to view its schedule:\n")

    # Get list of tournaments from LL
    tournaments = ll.get_tournament_list()  

    # choose tournament basic validation with input helper
    tournament_name = choose_from_list("Select Tournament by number: ", tournaments)   

    print(f"\nYou selected: {tournament_name}\n")

    # print the list of events in that tournament
    events_in_tournament = choose_from_list("Select Event by number: ", ll.get_events_in_tournament(tournament_name))
    print(f"\nYou selected event: {events_in_tournament}\n")

    # get schedule from ll for that tournament and event
    schedule = ll.get_tournament_schedule(tournament_name, events_in_tournament)
    if not schedule:
        print("No schedule found for this tournament/event.")
    else:
        print(f"Schedule for {tournament_name} - {events_in_tournament}:")
        for match in schedule:
            print(f" - {match}")
    input("Press Enter to continue...")
    return


