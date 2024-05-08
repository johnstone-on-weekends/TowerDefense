import pygame


class TowerMenuViewMixin:

    def __init__(self):
        self.tower_menu_box = None
        self.quit_button_hitbox = None
        self.tower_menu_currently_displaying = False

    def display_tower_menu(self, display_topside, tower_menu):
        self.tower_menu_currently_displaying = True

        y = 0 if display_topside else 3 / 4 * self.height

        self.tower_menu_box = pygame.Rect(0, y, self.width, self.height // 4)
        pygame.draw.rect(self.board_view, [181, 101, 29],
                         self.tower_menu_box)
        # Potentially also makes sense to draw lines here

        # Make the X-shaped button to quit the tower display
        self.display_quit_button(y)

        pygame.display.update()

    def display_quit_button(self, y):
        """
        Creates and displays a leave button. Involves making an X-shaped cross with lines.
        :param y: the y level that the tower menu display is placed at
        """
        cross_length = 10
        cross_offset = 5  # cross_offset means distance from edge
        # Bottom left - Top right line
        pygame.draw.line(self.board_view, [0, 0, 0],
                         (self.width - cross_length - cross_offset, y + cross_length + cross_offset),
                         (self.width - cross_offset, y + cross_offset), 2)
        # Bottom right - Top left line
        pygame.draw.line(self.board_view, [0, 0, 0], (self.width - cross_offset, y + cross_length + cross_offset),
                         (self.width - cross_length - cross_offset, y + cross_offset), 2)
        self.quit_button_hitbox = pygame.Rect(self.width - cross_length - cross_offset, y+cross_offset, cross_length, cross_length)

    def hide_tower_menu(self, board):
        self.tower_menu_currently_displaying = False
        self.board_view.fill([50, 50, 50])
        self.draw_board(board)
