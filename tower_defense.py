from game_state import GameState
from tower_menu import TowerMenu
from view.view import View
import pygame


class TowerDefense:

    def __init__(self):
        """
        Initializes the necessary objects. Then runs the game.
        """
        self.view = View()
        self.game_state = GameState()
        self.tower_menu = TowerMenu()
        self.run()

    def run(self):
        """
        Initial function called to run the game. Starts the chain of checking events.
        """
        self.view.draw_board(self.game_state.board)
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            clock.tick(60)

    def check_events(self):
        """
        Function is called every tick. It checks the "events" of pygame, such as window resizing,
        quitting the game, keys pressed, etc.
        """
        for event in pygame.event.get():
            # Check if game quit
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.VIDEORESIZE:
                self.view.handle_resize(event.w, event.h, self.game_state.board)

    def handle_mouse_click(self, mouse_position):
        """
        Handles the mouse clicked at the specific location
        :param mouse_position: the position of the mouse, index 0: y, index 1: x.
        """
        # This calculation gives us the actual coordinates on the map
        clicked_y = int((mouse_position[1] - self.view.y_offset) // self.view.grid_size)
        clicked_x = int((mouse_position[0] - self.view.x_offset) // self.view.grid_size)

        # If we have not actually clicked on the board we can end here
        if not self.game_state.in_bounds(clicked_x, clicked_y):
            return

        # highlight the square in the board
        self.view.highlight_selected_field(clicked_x, clicked_y, self.game_state.board)

        if self.game_state.board[clicked_y][clicked_x].type_of_field == "g":
            pass



TowerDefense()