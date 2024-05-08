import pygame

from view.board_drawing_mixin import BoardDrawingMixin
from view.event_handling_mixin import EventHandlingMixin
from view.tower_menu_view_mixin import TowerMenuViewMixin


class View(BoardDrawingMixin, EventHandlingMixin, TowerMenuViewMixin):
    # This view class is called from the rest of the program, and inherits the methods and attributes of the above
    # classes. This allows us to refactor our "view" class into smaller classes with more precise functionalities.

    def __init__(self, board):
        """
        Initializes the visual components of the game
        """
        # Grid size will depend on the map, so we keep it none until we give our first map
        super().__init__()
        self.board_view = None

        # Board dimensions
        self.board_size = 800
        self.width = self.board_size
        self.height = self.board_size
        self.grid_size = self.board_size / len(board)

        self.initialize_images()

        # x and y offsets tell us where the board should be centered at when the display isn't square
        self.x_offset = 0
        self.y_offset = 0

        # Make and draw the initial board
        self.init_board()
        self.draw_board(board)
        self.display_tower_menu_button()

    def initialize_images(self):
        self.popper_image = pygame.image.load(f"assets/images/popper.png")
        self.scale_images()

    def scale_images(self):
        print(self.grid_size)
        self.popper_image = pygame.transform.smoothscale(self.popper_image, (self.grid_size, self.grid_size))

