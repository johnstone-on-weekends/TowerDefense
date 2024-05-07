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
        self.view.draw_board(self.game_state.board)

        clock = pygame.time.Clock()
        while True:
            self.check_events()
            clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            # Check if game quit
            if event.type == pygame.QUIT:
                pygame.quit()


TowerDefense()
