from datetime import date

class Person:
    def __init__(self, name: str = None, phone: str = None, address: str = None, dob: date = None, email: str = None):
        self.name = name
        self.phone = phone
        self.address = address
        self.dob = dob
        self.email = email