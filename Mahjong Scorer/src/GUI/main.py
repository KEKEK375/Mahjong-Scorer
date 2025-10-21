import dearpygui.dearpygui as dpg
from src.game import Game


class GUI:
    def __init__(self):
        self.game = Game()
        self.create_gui()

    def create_gui(self):
        dpg.create_context()
        dpg.create_viewport(title="Custom Title", width=600, height=200)

        with dpg.window(tag="Primary Window"):
            self.menu_bar()

            self.main_menu()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()

    def toggle_fullscreen(self):
        dpg.toggle_viewport_fullscreen()

    def raise_error(self, message):
        dpg.add_text(message, color=(255, 0, 0), parent="Primary Window")

    def menu_bar(self):
        with dpg.menu_bar():
            with dpg.menu(label="Save"):
                dpg.add_menu_item(label="Save", callback=lambda: print("Save"))
                dpg.add_menu_item(label="Load", callback=lambda: print("Load"))

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(
                    label="Fullscreen", check=True, callback=self.toggle_fullscreen
                )

    def main_menu(self):
        self.main_menu_active = True
        with dpg.group(tag="main_menu", parent="Primary Window"):
            dpg.add_button(label="Start Game", callback=self.start_game, tag="start_game_button")
            dpg.add_button(label="Quit", callback=lambda: dpg.stop_dearpygui())

    def start_game(self):
        self.get_players()
        self.show_options()

    def show_options(self):
        with dpg.group(tag="options", parent="Primary Window"):
            dpg.add_button(label=f"Score round {self.game.current_round + 1}", callback=self.score_round, tag="score_round_button")
            dpg.add_button(label="Show scores", callback=self.display_scores, tag="show_scores_button")
            dpg.add_button(label="Show graph", callback=self.display_graph, tag="show_graph_button")

    def get_players(self):
        if self.main_menu_active:
            dpg.delete_item("main_menu")
            self.main_menu_active = False

        with dpg.group(tag="get_players", parent="Primary Window"):
            dpg.add_text("Enter player names:", tag="player_names_text")
            dpg.add_input_text(hint="East", tag="east_name")
            dpg.add_input_text(hint="South", tag="south_name")
            dpg.add_input_text(hint="West", tag="west_name")
            dpg.add_input_text(hint="North", tag="north_name")
            dpg.add_button(label="Next", callback=self.set_players, tag="player_names_next_button")

    def set_players(self):
        self.east_name = dpg.get_value("east_name")
        self.south_name = dpg.get_value("south_name")
        self.west_name = dpg.get_value("west_name")
        self.north_name = dpg.get_value("north_name")

        if len({self.east_name, self.south_name, self.west_name, self.north_name}) != 4:
            self.raise_error("Please fill all fields with unique names.")
            return

        self.game.set_player(self.east_name)
        self.game.set_player(self.south_name)
        self.game.set_player(self.west_name)
        self.game.set_player(self.north_name)

        self.clear_get_player()

    def clear_get_player(self):
        dpg.delete_item("get_players")

    def score_round(self):
        dpg.delete_item("options")

        self.show_options()

    def display_scores(self):
        dpg.delete_item("options")

        with dpg.group(tag="scores", parent="Primary Window"):
            dpg.add_button(label="Back", callback=self.close_scores, tag="back_button")

    def close_scores(self):
        dpg.delete_item("scores")
        self.show_options()

    def display_graph(self):
        dpg.delete_item("options")

        with dpg.group(tag="graph", parent="Primary Window"):
            dpg.add_button(label="Back", callback=self.close_graph, tag="back_button")

    def close_graph(self):
        dpg.delete_item("graph")
        self.show_options()