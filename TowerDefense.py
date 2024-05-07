from GameState import GameState
from View import View
import pygame


class TowerDefense:

    def __init__(self):
        """
        Initializes the view and game_state objects. Then runs the game.
        """
        self.view = View()
        self.game_state = GameState()
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

    def handle_mouse_click(self, mouse_position):
        """
        Handles the mouse clicked at the specific location
        :param mouse_position: the position of the mouse, index 0: y, index 1: x.
        """
        clicked_row = mouse_position[0]//self.view.grid_size
        clicked_col = mouse_position[1]//self.view.grid_size
        self.view.highlight_selected_field(clicked_row, clicked_col, self.game_state.board)


TowerDefense()
