import pygame

from view.board_drawing_mixin import BoardDrawingMixin
from view.event_handling_mixin import EventHandlingMixin
from view.tower_menu_view_mixin import TowerMenuViewMixin


class View(BoardDrawingMixin, EventHandlingMixin, TowerMenuViewMixin):
    # This view class is called from the rest of the program, and inherits the methods and attributes of the above
    # classes. This allows us to refactor our "view" class into smaller classes with more precise functionalities.

    def __init__(self, game_state, towers):
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
        self.grid_size = self.board_size / len(game_state.board)

        # x and y offsets tell us where the board should be centered at when the display isn't square
        self.x_offset = 0
        self.y_offset = 0

        # Make and draw the initial board
        self.init_board()
        self.scale_tower_images(towers)
        self.draw_board(game_state.board)
        self.display_tower_menu_button()

    def scale_tower_images(self, towers):
        for tower in towers:
            tower.init_image()
            tower.icon_image = pygame.transform.smoothscale(tower.icon_image,
                                                            (self.rectangle_size, self.rectangle_size))

    def draw_tower_at_mouse(self, tower, board, tower_menu):
        self.redraw_everything(board, tower_menu)
        self.board_view.blit(tower.icon_image, (pygame.mouse.get_pos()))

    def redraw_everything(self, board, tower_menu):
        self.draw_board(board)
        if self.tower_menu_currently_displaying:
            self.display_tower_menu(self.tower_menu_currently_displaying_topside, tower_menu)
