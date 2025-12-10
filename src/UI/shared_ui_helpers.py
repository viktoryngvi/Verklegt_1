from UI.input_helper import choose_from_list


def __init__(self, ll, menu_ui):
    self.ll = ll
    self.menu_ui = menu_ui



def view_teams(self):
    self.menu_ui.print_header("VIEW TEAMS")
    self.menu_ui.print_box_top()
    self.menu_ui.print_box_line(" Select a team to view: ")
    teams = self.ll.get_team_list()

    team_name = choose_from_list("Select Team by number: ", teams)

    print(f"\nYou selected: {team_name}\n")

    players_in_team = self.ll.get_players_in_team(team_name)
    print(f"Players in {team_name}:")
    for player in players_in_team:
        print(f" - {player}")
    input("Press Enter to continue...")
    return
   


def create_team(ll, menu_ui):
    menu_ui.print_header("CREATE TEAM")
    pass
"""
name of team
captain id
list of players

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


