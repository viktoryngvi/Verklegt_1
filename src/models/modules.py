class Modules:
    class Person:
        def __init__(self, name: str, phone: str, address: str, dob: str, email: str):
            self.name = name
            self.phone = phone
            self.address = address
            self.dob = dob
            self.email = email

    class Organiser(Person):
        def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int):
            super().__init__(name, phone, address, dob, email)
            self.id = id

    class Spectator(Person):
        pass

    class Player(Person):
        def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str):
            super().__init__(name, phone, address, dob, email)
            self.handle = handle
            self.id = id

    class Captain(Player):
        def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str):
            super().__init__(name, phone, address, dob, email, id, handle)

    class Team():
        def __init__(self, name: str, captain: "Modules.Captain" , players: list["Modules.Player"]):
            self.name = name
            self.captain = captain
            self.players = players
            pass

    class Match:
        def __init__(self, id: int, team_a: "Modules.Team", team_b: "Modules.Team", winner: "Modules.Team", result_score: str, schedule_time: str, server_id: str ):
            self.id = id
            self.team_a = team_a
            self.team_b = team_b
            self.winner = winner 
            self.result_score = result_score
            self.schedule_time = schedule_time
            self.server_id = server_id

    class Event:
        def __init__(self, name: str, game_type: str, teams: list["Modules.Team"], matches: list["Modules.Match"]):
            self.name = name
            self.game_type = game_type
            self.teams = teams
            self.matches = matches
            pass

    class Tournament:
        def __init__(self, name: str, location: str, start_date: str, end_date: str, contact_person: "Modules.Person", events: list["Modules.Event"]):
            self.name = name
            self.location = location
            self.start_date = start_date
            self.end_date = end_date
            self.contact_person = contact_person
            self.events = events
            pass

    class Club:
        def __init__(self, name: str, home_town: str, country: str, colors: list):
            self.name = name
            self.home_town = home_town
            self.country = country
            self.colors = colors
            pass

