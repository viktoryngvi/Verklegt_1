# LL/schedule_generator.py

from models.match import Match
from models.event import Event
from models.team import Team


class ScheduleGeneratorLL:

    # ---------------------------------------------------------------
    # KNOCKOUT (Single Elimination)
    # ---------------------------------------------------------------
    def generate_knockout_schedule(self, teams: list[Team]) -> Event:
        """
        Generates a knockout bracket:
            Round of 16 → Quarterfinals → Semifinals → Final
        Returns an Event object containing all matches.
        """

        if len(teams) != 16:
            raise ValueError("Knockout tournament requires exactly 16 teams")

        matches = []
        match_id = 1

        # Round of 16 (16 teams → 8 matches)
        round_16 = []
        for i in range(0, 16, 2):
            match = Match(
                id=match_id,
                team_a=teams[i],
                team_b=teams[i+1],
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            round_16.append(match)
            match_id += 1

        matches.extend(round_16)

        # Quarterfinals (8 teams → 4 matches), placeholder until winners known
        quarterfinals = [
            Match(
                id=match_id + i,
                team_a=None,
                team_b=None,
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            for i in range(4)
        ]
        match_id += 4
        matches.extend(quarterfinals)

        # Semifinals (4 teams → 2 matches)
        semifinals = [
            Match(
                id=match_id + i,
                team_a=None,
                team_b=None,
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            for i in range(2)
        ]
        match_id += 2
        matches.extend(semifinals)

        # Final (2 teams → 1 match)
        final = Match(
            id=match_id,
            team_a=None,
            team_b=None,
            winner=None,
            result_score=None,
            schedule_time=None,
            server_id=None,
        )
        matches.append(final)

        # Build tournament event (LL responsibility)
        return Event(
            name="Knockout Bracket",
            game_type="knockout",
            teams=teams,
            matches=matches
        )

    # ---------------------------------------------------------------
    # DOUBLE ELIMINATION
    # ---------------------------------------------------------------
    def generate_double_elimination_schedule(self, teams: list[Team]) -> Event:
        """
        Generates a double elimination bracket:
        Winners bracket and losers bracket.
        Returns an Event object containing all matches.
        """

        if len(teams) != 16:
            raise ValueError("Double elimination requires exactly 16 teams")

        matches = []
        match_id = 1

        # -------------------------------
        # WINNERS BRACKET ROUND 1 (8 matches)
        # -------------------------------
        winners_round_1 = []
        for i in range(0, 16, 2):
            m = Match(
                id=match_id,
                team_a=teams[i],
                team_b=teams[i+1],
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            winners_round_1.append(m)
            match_id += 1

        matches.extend(winners_round_1)

        # -------------------------------
        # WINNERS BRACKET ROUND 2 (4 matches, TBD teams)
        # -------------------------------
        winners_round_2 = []
        for _ in range(4):
            m = Match(
                id=match_id,
                team_a=None,  # filled later based on winners
                team_b=None,
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            winners_round_2.append(m)
            match_id += 1

        matches.extend(winners_round_2)

        # -------------------------------
        # WINNERS SEMIFINALS (2 matches)
        # -------------------------------
        winners_semis = []
        for _ in range(2):
            m = Match(
                id=match_id,
                team_a=None,
                team_b=None,
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            winners_semis.append(m)
            match_id += 1

        matches.extend(winners_semis)

        # -------------------------------
        # WINNERS FINAL (1 match)
        # -------------------------------
        winners_final = Match(
            id=match_id,
            team_a=None,
            team_b=None,
            winner=None,
            result_score=None,
            schedule_time=None,
            server_id=None,
        )
        match_id += 1
        matches.append(winners_final)

        # -------------------------------
        # LOSERS BRACKET (structure only)
        # You will fill loser slots after matches play out.
        # -------------------------------
        losers = []
        for _ in range(10):   # typical 16-team DE losers bracket
            m = Match(
                id=match_id,
                team_a=None,
                team_b=None,
                winner=None,
                result_score=None,
                schedule_time=None,
                server_id=None,
            )
            losers.append(m)
            match_id += 1

        matches.extend(losers)

        # -------------------------------
        # GRAND FINAL
        # -------------------------------
        grand_final = Match(
            id=match_id,
            team_a=None,
            team_b=None,
            winner=None,
            result_score=None,
            schedule_time=None,
            server_id=None,
        )
        matches.append(grand_final)

        return Event(
            name="Double Elimination Bracket",
            game_type="double_elimination",
            teams=teams,
            matches=matches
        )
