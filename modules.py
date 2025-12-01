class Person:
    def __init__(self, name: str, phone: str, address: str, dob: str, email: str):
        self.name = name
        self.phone = phone
        self.address = address
        self.dob = dob
        self.email = email

class Organiser(Person):
    def __init__(self, id: int):
        super().__init__()
        self.id = id

class Spectator(Person):
    super()

class Player(Person):
    def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str):
        super().__init__(name, phone, address, dob, email)
        self.handle = handle
        self.id = id

class Captain(Player):
    def __init__(self, name: str, phone: str, address: str, dob: str, email: str, id: int, handle: str):
        super().__init__(name, phone, address, dob, email, id, handle)

class Team:
    def __init__(self, name: str, captain: Captain, players: list[Player]):
        self.name = name
        self.captain = captain
        self.players = players

        pass

class Match:
    def __init__(self, id: int, team_a: Team, team_b: Team, winner: Team, result_score: str, schedule_time: str, server_id: str ):
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.winner = winner 
        self.result_score = result_score
        self.schedule_time = schedule_time
        self.server_id = server_id

class Event:
    def __init__(self, name: str, game_type: str, teams: list[Team], matches: list[Match]):
        self.name = name
        self.game_type = game_type
        self.teams = teams
        self.matches = matches
        pass

class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, contact_person: Person, events: list[Event]):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.contact_person = contact_person
        self.events = events
        pass