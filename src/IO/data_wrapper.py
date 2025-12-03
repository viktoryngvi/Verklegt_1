from IO.Player_IO import PlayerIO
from models.player import Player


class DLWrapper:
    """Aðal gateway inn í gagnalagið.

    Er bara með tilvísun í PlayerIO og kall-fram föll hans.
    Seinna má bæta við TeamIO, MatchIO o.s.frv.
    """

    def __init__(self) -> None:
        self.player_io = PlayerIO()

    # --- PLAYER ---

    def create_player(self, player: Player) -> str:
        """Creates a player in players.csv."""
        return self.player_io.create_player(player)

    def load_players(self) -> list[Player]:
        """Returns a list of players from players.csv."""
        return self.player_io.load_players()


   