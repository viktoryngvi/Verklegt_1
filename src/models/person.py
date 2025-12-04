class Person:
    def __init__(self, name: str, phone: str, address: str = None, dob: str = None, email: str):
        self.name = name
        self.phone = phone
        self.address = address
        self.dob = dob
        self.email = email