import pygame.display


class EventHandlingMixin:
    def handle_resize(self, width, height, board, tower_menu):
        """
        Handles the visual resizing of the screen
        :param towers: the towers images in the menu. They need to be rescaled
        :param width: new width of the screen
        :param height: new height of the screen
        :param board: current board
        """
        self.width = width
        self.height = height
        self.board_size = min(self.width, self.height)
        self.x_offset = max((self.width - self.height) // 2, 0)
        self.y_offset = max((self.height - self.width) // 2, 0)
        self.draw_board(board)
        self.grid_size = self.board_size / len(board)
        self.scale_tower_images(tower_menu.towers)
        if not self.tower_menu_currently_displaying:
            self.display_tower_menu_button()