
from datalayer.teams_data import TeamsData


def main() -> None:
    # <-- your local file
    repo = TeamsData(r"c:\GITHUB\Verklegt_1\Data\teams.csv")
    teams = repo.load_teams()

    print("Loaded teams:")
    for t in teams:
        print("-", t)

    print(f"\nTotal teams: {len(teams)}")


if __name__ == "__main__":
    main()
