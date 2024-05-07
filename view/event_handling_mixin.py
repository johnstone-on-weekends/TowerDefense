class EventHandlingMixin:
    def handle_resize(self, width, height, board):
        """
        Handles the visual resizing of the screen
        :param width: new width of the screen
        :param height: new height of the screen
        :param board: current board
        """
        self.width = width
        self.height = height
        self.board_size = min(self.width, self.height)
        self.board_view.fill([50, 50, 50])
        self.x_offset = max((self.width - self.height) // 2, 0)
        self.y_offset = max((self.height - self.width) // 2, 0)
        self.draw_board(board)