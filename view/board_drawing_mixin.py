import pygame


class BoardDrawingMixin:

    def init_board(self):
        """
        Initializes a super basic board, without any content
        """
        self.board_view = pygame.display.set_mode((self.board_size, self.board_size), pygame.RESIZABLE)
        self.board_view.fill([0, 0, 0])
        pygame.display.set_caption('Tower Defense')
        pygame.display.update()

    def draw_board(self, board):
        """
        Draws the board into a grid on the screen.
        :param board: a square list of lists that represent the map, or level.
        """
        self.grid_size = self.board_size / len(board)

        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = j * self.grid_size + self.x_offset
                y = i * self.grid_size + self.y_offset
                pygame.draw.rect(self.board_view, field.color,
                                 (x, y, self.grid_size, self.grid_size))
                # Potentially also makes sense to draw lines here

        pygame.display.update()

    def highlight_selected_field(self, x, y, board):
        """
        Highlights the selected field on the board.
        :param x: the x coordinate for the field on the board.
        :param y: the y coordinate for the field on the board.
        :param board: the board
        """
        self.draw_board(board)
        rect = (
            x * self.grid_size + self.x_offset,
            y * self.grid_size + self.y_offset,
            self.grid_size,
            self.grid_size
        )
        pygame.draw.rect(self.board_view, [128, 128, 0], rect)
        pygame.display.update()
