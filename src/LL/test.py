import unittest
from datetime import datetime, timedelta
from Create_tournament import CreateTournament


class TestDateValidation(unittest.TestCase):
    """Test suite for tournament date validation (3-day span requirement)"""

    def test_valid_3_day_span(self):
        """Test that a valid 3-day span returns success"""
        # 02.12.2025 to 05.12.2025 = exactly 3 days
        tournament = CreateTournament("Test Tournament", "Knockout", "02.12.2025", "05.12.2025")
        result = tournament.validate_input()
        self.assertEqual(result, "Correct, tournament spans 3 days")
        self.assertTrue(tournament.is_valid)

    def test_valid_3_day_span_different_dates(self):
        """Test another valid 3-day span"""
        # 10.01.2026 to 13.01.2026 = exactly 3 days
        tournament = CreateTournament("Another Tournament", "Knockout", "10.01.2026", "13.01.2026")
        result = tournament.validate_input()
        self.assertEqual(result, "Correct, tournament spans 3 days")
        self.assertTrue(tournament.is_valid)

    def test_less_than_3_days(self):
        """Test that fewer than 3 days returns error"""
        # 02.12.2025 to 04.12.2025 = 2 days
        tournament = CreateTournament("Short Tournament", "Knockout", "02.12.2025", "04.12.2025")
        result = tournament.validate_input()
        self.assertIn("Error: Tournament must span exactly 3 days", result)
        self.assertIn("spans 2 days", result)
        self.assertFalse(tournament.is_valid)

    def test_more_than_3_days(self):
        """Test that more than 3 days returns error"""
        # 02.12.2025 to 06.12.2025 = 4 days
        tournament = CreateTournament("Long Tournament", "Knockout", "02.12.2025", "06.12.2025")
        result = tournament.validate_input()
        self.assertIn("Error: Tournament must span exactly 3 days", result)
        self.assertIn("spans 4 days", result)
        self.assertFalse(tournament.is_valid)

    def test_same_start_and_end_date(self):
        """Test that same start and end date returns error"""
        # 02.12.2025 to 02.12.2025 = 0 days
        tournament = CreateTournament("Same Date Tournament", "Knockout", "02.12.2025", "02.12.2025")
        result = tournament.validate_input()
        self.assertIn("Error", result)
        self.assertFalse(tournament.is_valid)

    def test_end_date_before_start_date(self):
        """Test that end date before start date returns error"""
        # 05.12.2025 to 02.12.2025 = reversed dates
        tournament = CreateTournament("Reversed Tournament", "Knockout", "05.12.2025", "02.12.2025")
        result = tournament.validate_input()
        self.assertEqual(result, "Error: Start date must be before end date")
        self.assertFalse(tournament.is_valid)

    def test_invalid_date_format(self):
        """Test that invalid date format returns error"""
        # Wrong format: should be dd.mm.yyyy
        tournament = CreateTournament("Invalid Format", "Knockout", "2025-12-02", "2025-12-05")
        result = tournament.validate_input()
        self.assertIn("Error: Invalid date format", result)
        self.assertFalse(tournament.is_valid)

    def test_empty_tournament_name(self):
        """Test that empty tournament name returns error"""
        tournament = CreateTournament("", "Knockout", "02.12.2025", "05.12.2025")
        result = tournament.validate_input()
        self.assertIn("Tournament name cannot be empty", result)
        self.assertFalse(tournament.is_valid)

    def test_1_day_span(self):
        """Test that 1 day span returns error"""
        # 02.12.2025 to 03.12.2025 = 1 day
        tournament = CreateTournament("One Day Tournament", "Knockout", "02.12.2025", "03.12.2025")
        result = tournament.validate_input()
        self.assertIn("spans 1 day", result)
        self.assertFalse(tournament.is_valid)

    def test_7_day_span(self):
        """Test that 7 day span returns error"""
        # 02.12.2025 to 09.12.2025 = 7 days
        tournament = CreateTournament("One Week Tournament", "Knockout", "02.12.2025", "09.12.2025")
        result = tournament.validate_input()
        self.assertIn("spans 7 days", result)
        self.assertFalse(tournament.is_valid)


if __name__ == "__main__":
    unittest.main()
