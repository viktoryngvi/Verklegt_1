
from dataclasses import dataclass


@dataclass
class Tournament:
    id: str
    name: str
    start_date: str
    end_date: str
    venue: str
    contact_name: str
    contact_email: str
    contact_phone: str
