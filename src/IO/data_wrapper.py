import csv
import os
from models.player import Player


class DLWrapper:
    def __init__(self):
        # You can adjust file paths as needed
        self.players_file = "data/players.csv"

    # -----------------------
    # PLAYER HANDLING (CSV)
    # -----------------------

    def load_players(self) -> list[Player]:
        """Load all players from CSV. Returns list of Player objects."""
        if not os.path.exists(self.players_file):
            return []

        players = []
        with open(self.players_file, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Convert the 'id' from string to int (or None)
                row["id"] = int(row["id"]) if row["id"] else None

                player = Player(
                    name=row["name"],
                    phone=row["phone"],
                    address=row["address"],
                    dob=row["dob"],
                    email=row["email"],
                    id=row["id"],
                    handle=row["handle"],
                    captain=(row["captain"] == "True")
                )

                players.append(player)

        return players

    def save_players(self, players: list[Player]):
        """Save all players to CSV file."""
        os.makedirs(os.path.dirname(self.players_file), exist_ok=True)

        with open(self.players_file, mode="w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "name", "phone", "address", "dob", "email", "handle", "captain"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for p in players:
                writer.writerow({
                    "id": p.id,
                    "name": p.name,
                    "phone": p.phone,
                    "address": p.address,
                    "dob": p.dob,
                    "email": p.email,
                    "handle": p.handle,
                    "captain": p.captain
                })

    def create_player(self, player: Player):
        """Add a single new player to CSV storage."""
        players = self.load_players()

        # Automatically assign ID if needed
        if player.id is None:
            max_id = max((p.id for p in players if p.id is not None), default=0)
            player.id = max_id + 1

        players.append(player)
        self.save_players(players)
        return "Success"

