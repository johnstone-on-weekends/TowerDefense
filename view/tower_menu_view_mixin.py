import pygame


class TowerMenuViewMixin:

    def __init__(self):
        """
        Initializes some components for the TowerMenuView
        """
        self.tower_menu_currently_displaying_topside = None
        self.reveal_tower_menu_bottom_button = None
        self.reveal_tower_menu_top_button = None
        self.tower_menu_box = None
        self.quit_button_hitbox = None
        self.tower_menu_currently_displaying = False

    def display_tower_menu(self, display_topside, tower_menu, board):
        """
        Displays the tower menu with represent to the boolean display_topside which dictates location
        :param display_topside: a boolean that tells the machine whether to display the panel in the top or bottom
        :param tower_menu: the menu at this time
        """
        self.tower_menu_currently_displaying = True
        self.draw_board(board, True)
        self.tower_menu_currently_displaying_topside = display_topside

        tower_menu_box_height = self.height // 8
        y = 0 if display_topside else self.height - tower_menu_box_height

        # Make the background box for the tower menu
        self.tower_menu_box = pygame.Rect(0, y, self.width, tower_menu_box_height)
        pygame.draw.rect(self.board_view, [181, 101, 29],
                         self.tower_menu_box)

        # Make the squares along the background box
        self.draw_unit_boxes(tower_menu_box_height, y)

        # Make the X-shaped button to quit the tower menu
        self.display_quit_button(y)

        pygame.display.update()

    def draw_unit_boxes(self, tower_menu_box_height, y):
        """
        Draws blue boxes inside the tower menu box. These boxes represent the units.
        :param tower_menu_box_height: the height of the tower menu box
        :param y: the y that the box is located at (either near bottom or top)
        """
        num_rectangles = self.width // tower_menu_box_height
        margin = 1 / 8 * tower_menu_box_height
        rectangle_size = 3 / 4 * tower_menu_box_height
        for i in range(num_rectangles):
            rect = pygame.Rect(i * tower_menu_box_height + margin, y + margin, rectangle_size, rectangle_size)
            pygame.draw.rect(self.board_view, [0, 255, 255], rect)

    def display_quit_button(self, y):
        """
        Creates and displays a leave button. Involves making an X-shaped cross with lines.
        :param y: the y level that the tower menu display is placed at
        """
        cross_length = 10
        cross_offset = 5  # cross_offset means distance from edge
        # Bottom left - Top right line
        pygame.draw.line(self.board_view, [0, 0, 0],
                         (self.width - cross_length - cross_offset, y + cross_length + cross_offset),
                         (self.width - cross_offset, y + cross_offset), 2)
        # Bottom right - Top left line
        pygame.draw.line(self.board_view, [0, 0, 0], (self.width - cross_offset, y + cross_length + cross_offset),
                         (self.width - cross_length - cross_offset, y + cross_offset), 2)
        self.quit_button_hitbox = pygame.Rect(self.width - cross_length - cross_offset, y + cross_offset, cross_length,
                                              cross_length)
        pygame.display.update()

    def hide_tower_menu(self, board):
        """
        Hides the tower menu
        :param board: the board that needs to be redrawn
        """
        self.tower_menu_currently_displaying = False
        self.board_view.fill([50, 50, 50])
        self.draw_board(board)
        self.display_tower_menu_button()
        pygame.display.update()

    def display_tower_menu_button(self):
        """
        Initializes the buttons that we use to reveal the menu.
        """
        button_height = self.height // 40

        # Define the rectangles we use to represent these buttons
        self.reveal_tower_menu_top_button = pygame.Rect(self.width // 8, 0, self.width // 8, button_height)
        self.reveal_tower_menu_bottom_button = pygame.Rect(self.width // 8, self.height - button_height,
                                                           self.width // 8, button_height)

        # Actually display the buttons
        pygame.draw.rect(self.board_view, [181, 101, 29], self.reveal_tower_menu_top_button)
        pygame.draw.rect(self.board_view, [181, 101, 29], self.reveal_tower_menu_bottom_button)
        pygame.display.update()
