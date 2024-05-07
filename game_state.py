from field import Field


class GameState:

    def __init__(self):
        self.board = [
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g"],
            ["g", "p", "p", "p", "p", "p", "g", "g", "g", "g"],
            ["g", "p", "g", "g", "g", "p", "p", "g", "g", "g"],
            ["g", "p", "p", "p", "g", "g", "p", "g", "g", "g"],
            ["g", "g", "g", "p", "w", "w", "p", "g", "g", "g"],
            ["s", "p", "p", "p", "w", "w", "p", "g", "g", "g"],
            ["g", "g", "g", "g", "g", "g", "p", "g", "g", "g"],
            ["g", "g", "g", "g", "g", "g", "p", "p", "p", "e"],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g"],
            ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g"]
        ]
        self.field_dimensions = len(self.board)

        self.add_fields_to_board()

    def add_fields_to_board(self):
        """
        Converts self.board into a list of lists with Field objects rather than just strings. Useful because fields have
        certain properties, such as a color associated with the type.
        """
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                self.board[y][x] = Field(self.board[y][x])

    def in_bounds(self, x, y):
        return 0 <= x < self.field_dimensions and 0 <= y < self.field_dimensions
