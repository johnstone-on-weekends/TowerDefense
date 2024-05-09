from field import Field
from copy import deepcopy


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

        self.waypoints = self.calculate_waypoints()
        print(self.waypoints)

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

    def calculate_waypoints(self):
        """
        Calculated the path the enemies must take to cross the screen. It uses the board to determine the "waypoints" that
        the enemies with use in their pathfinding.
        :return:
        """
        board_copy = deepcopy(self.board)

        def find_start():
            for i in range(len(board_copy)):
                for j in range(len(board_copy[0])):
                    if board_copy[i][j] == "s":
                        return i, j

        start_row, start_col = find_start()
        current_row, current_col = start_row, start_col
        waypoints = []

        while board_copy[current_row][current_col] != "e":
            board_copy[current_row][current_col] = "v"  # Mark visited
            waypoints.append((current_col, current_row))
            if current_row > 0 and board_copy[current_row - 1][current_col] in ["p", "e"]:
                current_row -= 1
            elif current_row < len(board_copy) - 1 and board_copy[current_row + 1][current_col] in ["p", "e"]:
                current_row += 1
            elif current_col > 0 and board_copy[current_row][current_col - 1] in ["p", "e"]:
                current_col -= 1
            elif current_col < len(board_copy[0]) - 1 and board_copy[current_row][current_col + 1] in ["p", "e"]:
                current_col += 1

        waypoints.append((current_col, current_row))  # Add end point
        return waypoints
