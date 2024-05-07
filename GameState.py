from Field import Field


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
        self.add_fields_to_board()

    def add_fields_to_board(self):
        """
        Converts self.board into a list of lists with Field objects rather than just strings. Useful because fields have
        certain properties, such as a color associated with the type.
        """
        for r in range(len(self.board)):
            for c in range(len(self.board)):
                self.board[r][c] = Field(self.board[r][c])
