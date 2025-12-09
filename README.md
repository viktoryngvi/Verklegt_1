# Verklegt_1

RU e‑Sport Cup (Python)

Overview:

Tournament management system for the RU e‑Sport Cup. Follows a 3-layer architecture: UI (user interface), LL (business logic), IO (data/IO). Model classes aswell.

Project layout (key items):

- README.md, readme.txt          Docs
- data/                          CSV data (teams, players, clubs, schedule, results, tournament)
- src/
  - main.py                      Program main flow (use UI entry points instead)
  - IO/                          Data layer (CSV readers/writers, wrapper)
  - LL/                          Logic layer (tournament, teams, players, schedule)
  - models/                      Entities (player, team, tournament, match, etc.)
  - UI/                          UIs (main/menu/organizer/captain/player/spectator)
- Dagbok/                        Project diary
- Verkefnipdf/                   Assignment docs / handbook

Prerequisites:

- Python 3.11+
- No external dependencies required (standard library only)

How to run:

Run from repo root so package imports resolve:

- Main UI menu: python -m src.UI.mainUI

Debugging in VS Code:

1) Open src/UI/mainUI.py (or another UI file).
2) Set breakpoints.
3) Run with F5.

Architecture notes:

- UI layer: menus, input helpers, and role-specific screens (mainUI.py, menuUI.py, organizerUI.py, captainUI.py, playerUI.py, spectatorUI.py, shared_ui_helpers.py).
- Logic layer: business rules and orchestration (e.g., TournamentLL.py, schedule_generator.py, clubLL.py, teamLL.py, playerLL.py).
- Data layer: CSV persistence and wrappers (data_wrapper.py, Player_IO.py, Teams_IO.py, Tournament_IO.py, etc.).
- Models: domain entities (player.py, team.py, tournament.py, match.py, club.py, etc.).

Data files:

- Located in data (e.g., teams.csv, player_info.csv, schedule.csv, results.csv, Tournament.csv).
- IO layer handles read/write; run UIs from repo root so relative paths resolve.

Common run issues:

- ModuleNotFoundError: No module named UI: run as a module from repo root (python -m src.UI.mainUI) and keep src/__init__.py present.
- Empty src/main.py: intentionally blank; use UI entry points above.

Suggested workflow:

- Work on a feature branch; keep UI > LL > IO separation.
- Add tests under src/LL/test.py or create a tests/ folder if expanding.
- Use git regularly: git status, git add, git commit -m "msg".

License / authors:

Educational project for Reykjavík University, 2025.
