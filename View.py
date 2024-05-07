import pygame


class View:
    def __init__(self):
        """
        Initializes the visual components of the game
        """
        # Grid size will depend on the map, so we keep it none until we give our first map
        self.grid_size = None

        self.board_view = None

        self.board_size = 800
        self.init_board()

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
                x = j * self.grid_size
                y = i * self.grid_size
                pygame.draw.rect(self.board_view, field.color,
                                 (x, y, self.grid_size, self.grid_size))
        pygame.display.update()

    def highlight_selected_field(self, x, y, board):
        self.draw_board(board)
        pygame.draw.rect(self.board_view, [128, 128, 0], (x*self.grid_size, y*self.grid_size, self.grid_size, self.grid_size))
        pygame.display.update()
