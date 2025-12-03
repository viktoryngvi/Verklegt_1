from UI.menuUI import MenuUI
from UI.organizerUI import OrganizerUI
from UI.captainUI import CaptainUI
from UI.playerUI import PlayerUI
from UI.spectatorUI import SpectatorUI

class UImain:
    def __init__(self, ll_wrapper):
        self.llwrapper = ll_wrapper
        self.menu_ui = MenuUI()
        self.current_menu = "MAIN_MENU"

        self.organizer_ui = OrganizerUI(self.llwrapper, self.menu_ui)
        self.captain_ui = CaptainUI(self.llwrapper, self.menu_ui)
        self.player_ui = PlayerUI(self.llwrapper, self.menu_ui)
        self.spectator_ui = SpectatorUI(self.llwrapper, self.menu_ui)

    def run(self):
        while True:
            if self.current_menu == "MAIN_MENU":
                action = self.menu_ui.main_menu()

                if action in ["ORGANIZER_MENU", "CAPTAIN_MENU", "PLAYER_MENU", "SPECTATOR_MENU"]:
                    self.current_menu = action
                elif action == "EXIT":
                    print("Goodbye!")
                    break

            if self.current_menu == "ORGANIZER_MENU":
                self.current_menu = self.organizer_ui.show_menu()

            if self.current_menu == "CAPTAIN_MENU":
                self.current_menu = self.captain_ui.show_menu()

            if self.current_menu == "PLAYER_MENU":
                self.current_menu = self.player_ui.show_menu()

            if self.current_menu == "SPECTATOR_MENU":
                self.current_menu = self.spectator_ui.show_menu()


        




