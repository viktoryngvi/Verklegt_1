import re
from datetime import datetime
from typing import Callable, Dict, List, Optional


class CreatePlayer:
    """Logic-layer class to create and validate a new player.

    Usage:
        p = CreatePlayer.from_input(name, phone, email, dob, address)
        if p.is_valid():
            data = p.to_dict()
            p.save(save_func=my_storage_function)  # optional
    """

    EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    NAME_RE = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ \-']+$")

    def __init__(self, name: str, phone: str, email: str, dob: str, address: str):
        self.name = (name or "").strip()
        self.phone = (phone or "").strip()
        self.email = (email or "").strip()
        self.dob = (dob or "").strip()
        self.address = (address or "").strip()

        self._errors: List[str] = []

    @classmethod
    def from_input(cls, name: str, phone: str, email: str, dob: str, address: str) -> "CreatePlayer":
        """Create an instance from raw input values (strings)."""
        return cls(name, phone, email, dob, address)

    def validate_name(self) -> bool:
        if not self.name:
            self._errors.append("Name is required")
            return False
        if not self.NAME_RE.match(self.name):
            self._errors.append("Name contains invalid characters")
            return False
        return True

    def validate_phone(self) -> bool:
        digits = re.sub(r"\D", "", self.phone)
        if not digits:
            self._errors.append("Phone number is required")
            return False
        if len(digits) < 7 or len(digits) > 15:
            self._errors.append("Phone number must be between 7 and 15 digits")
            return False
        return True

    def validate_email(self) -> bool:
        if not self.email:
            self._errors.append("Email is required")
            return False
        if not self.EMAIL_RE.match(self.email):
            self._errors.append("Invalid email format")
            return False
        return True

    def validate_dob(self) -> bool:
        # Expected format: dd.mm.yyyy
        try:
            dob_dt = datetime.strptime(self.dob, "%d.%m.%Y")
        except ValueError:
            self._errors.append("Date of birth must be in format dd.mm.yyyy")
            return False
        # Optional: ensure dob is not in the future
        if dob_dt > datetime.now():
            self._errors.append("Date of birth cannot be in the future")
            return False
        return True

    def validate_address(self) -> bool:
        if not self.address:
            self._errors.append("Address is required")
            return False
        return True

    def validate_all(self) -> bool:
        """Run all validations and populate `self._errors`.

        Returns True if all validations pass.
        """
        self._errors.clear()
        checks = [
            self.validate_name(),
            self.validate_phone(),
            self.validate_email(),
            self.validate_dob(),
            self.validate_address(),
        ]
        return all(checks)

    def is_valid(self) -> bool:
        return len(self._errors) == 0

    def errors(self) -> List[str]:
        return list(self._errors)

    def to_dict(self) -> Dict[str, Optional[str]]:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "dob": self.dob,
            "address": self.address,
        }

    def save(self, save_func: Optional[Callable[[Dict[str, str]], None]] = None) -> bool:
        """Persist the player using `save_func`.

        If `save_func` is None the method will do nothing and return True when data is valid.
        `save_func` should accept a dict and raise on error.
        """
        if not self.validate_all():
            return False

        data = self.to_dict()
        if save_func:
            save_func(data)
        return True




