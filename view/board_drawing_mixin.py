import pygame


class BoardDrawingMixin:

    def init_board(self):
        """
        Initializes a super basic board, without any content
        """
        self.board_view = pygame.display.set_mode((self.board_size, self.board_size), pygame.RESIZABLE)
        pygame.display.set_caption('Tower Defense')

    def draw_board(self, board, tower_menu=None, skip_display_tower_menu=False):
        """
        Draws the board into a grid on the screen.
        :param skip_display_tower_menu: optional parameter to skip displaying the tower menu
        :param tower_menu:
        :param board: a square list of lists that represent the map, or level.
        """
        if tower_menu is None:
            tower_menu = []
        self.board_view.fill([50, 50, 50])
        self.grid_size = self.board_size / len(board)

        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = j * self.grid_size + self.x_offset
                y = i * self.grid_size + self.y_offset
                rect = (x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(self.board_view, field.color, rect)
                if field.tower:
                    self.board_view.blit(field.tower.image, rect)
                # Potentially also makes sense to draw lines here

        if self.tower_menu_currently_displaying and not skip_display_tower_menu:
            self.display_tower_menu(self.tower_menu_currently_displaying_topside, tower_menu, board)

    def highlight_selected_field(self, x, y, board, tower_menu):
        """
        Highlights the selected field on the board.
        :param x: the x coordinate for the field on the board.
        :param y: the y coordinate for the field on the board.
        :param board: the board
        """
        self.draw_board(board, tower_menu)
        if not self.tower_menu_currently_displaying:
            self.display_tower_menu_button()
        rect = (
            x * self.grid_size + self.x_offset,
            y * self.grid_size + self.y_offset,
            self.grid_size,
            self.grid_size
        )
        pygame.draw.rect(self.board_view, [128, 128, 0], rect)
        if board[y][x].tower:
            self.board_view.blit(board[y][x].tower.image, rect)

