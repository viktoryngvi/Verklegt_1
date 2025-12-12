class contact_person:
    """CONTACT_PERSON CLASS REPRESENTS NAME, EMAIL, AND PHONE."""
    
    def __init__(self, contact_name: str = None, contact_email :str = None, contact_phone :str = None):
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
