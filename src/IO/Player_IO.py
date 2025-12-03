import os
from models.player import Player


class PlayerIO:
    def __init__(self, file_path: str | None = None):
        # Geymum slóðina á player_info.csv
        # Ef þú keyrir main.py úr root, er 'data/player_info.csv' nóg
        self.file_path = file_path or "data/player_info.csv"

    def _player_exists(self, name: str) -> bool:
        """Athugar hvort leikmaður með þessu nafni sé til í skránni."""
        if not os.path.exists(self.file_path):
            return False

        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                # Sleppum hauslínu ef hún er til
                if line.startswith("name,") or line.strip() == "":
                    continue
                if line.split(",")[0] == name:
                    return True
        return False

    def create_player(self, player: Player) -> str:
        """Bætir leikmanni við CSV ef hann er ekki til nú þegar."""
        # Athugum hvort hann sé til (þú getur líka tékkað á handle í stað name)
        if self._player_exists(player.name):
            return "Player already exists"

        # Ef skráin er ekki til, búum til header fyrst
        file_exists = os.path.exists(self.file_path)

        with open(self.file_path, "a", encoding="utf-8") as f:
            if not file_exists:
                f.write("id,name,phone,address,dob,email,handle,team,captain\n")

            f.write(
                f"{player.id},"
                f"{player.name},"
                f"{player.phone},"
                f"{player.address},"
                f"{player.dob},"
                f"{player.email},"
                f"{player.handle},"
                f"{getattr(player, 'team', '')},"
                f"{getattr(player, 'captain', False)}\n"
            )

        return "Player created successfully"


