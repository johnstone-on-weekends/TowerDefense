import pygame


class View:
    def __init__(self):
        self.board_view = None
        self.board_size = 800
        self.init_board()

    def init_board(self):
        self.board_view = pygame.display.set_mode((self.board_size, self.board_size), pygame.RESIZABLE)
        self.board_view.fill([0, 0, 0])
        pygame.display.set_caption('Tower Defense')
        pygame.display.update()

    def draw_board(self, board):
        grid_size = self.board_size / len(board)
        fields_colors_dictionary = {
            -2: [255, 99, 71],
            -1: [240, 230, 140],
            0: [144, 238, 144],
            1: [139, 69, 19],
            2: [65, 105, 225]
        }
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = j * grid_size
                y = i * grid_size
                pygame.draw.rect(self.board_view, fields_colors_dictionary[field], (x, y, grid_size, grid_size))

        pygame.display.update()