from view.board_drawing_mixin import BoardDrawingMixin
from view.event_handling_mixin import EventHandlingMixin


class View(BoardDrawingMixin, EventHandlingMixin):
    # This view class is called from the rest of the program, and inherits the methods and attributes of the above
    # classes. This allows us to refactor our "view" class into smaller classes with more precise functionalities.

    def __init__(self):
        """
        Initializes the visual components of the game
        """
        # Grid size will depend on the map, so we keep it none until we give our first map
        self.grid_size = None
        self.board_view = None

        self.board_size = 800
        self.width = self.board_size
        self.height = self.board_size

        # x and y offsets tell us where the board should be centered at when the display isn't square
        self.x_offset = 0
        self.y_offset = 0

        self.init_board()
