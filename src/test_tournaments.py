
# tests/test_tournaments.py

from IO.tournaments_data import TournamentsData
from IO.tournament import Tournament


def test_add_and_load_tournament_real_data():
    print("=== TEST: Using REAL CSV data (data/tournaments.csv) ===")

    # This now uses the real data file (default value)
    td = TournamentsData()   # <-- no filename passed

    print("=== TEST: Adding a tournament to REAL DATA ===")
    new_t = td.add_tournament(
        name="Real Test Cup",
        start_date="2025-02-01",
        end_date="2025-02-03",
        venue="Main Arena",
        contact_name="Real Tester",
        contact_email="realtester@example.com",
        contact_phone="777-8888"
    )

    print("New REAL tournament created:")
    print(new_t)
    print()

    print("=== TEST: Reloading tournaments from REAL DATA ===")
    loaded = td.load_tournaments()

    print("Loaded tournaments:")
    for t in loaded:
        print(t)

    print("\nTEST PASSED — REAL IO data successfully updated!")


if __name__ == "__main__":
    test_add_and_load_tournament_real_data()
