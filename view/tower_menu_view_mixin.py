import pygame


class TowerMenuViewMixin:

    def __init__(self):
        self.tower_menu_currently_displaying = False

    def display_tower_menu(self, display_topside, tower_menu):
        self.tower_menu_currently_displaying = True

        y = 0 if display_topside else 3/4 * self.height

        pygame.draw.rect(self.board_view, [181, 101, 29],
                         (0, y, self.width, self.height//4))
        # Potentially also makes sense to draw lines here

        pygame.display.update()

    def hide_tower_menu(self, board):
        self.tower_menu_currently_displaying = False
        self.board_view.fill([50, 50, 50])
        self.draw_board(board)
