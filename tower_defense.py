from enemy import Enemy
from game_state import GameState
from tower_menu import TowerMenu
from view.view import View
import pygame


# THE ENTRY POINT TO THE GAME
class TowerDefense:

    def __init__(self):
        """
        Initializes the necessary objects. Then runs the game.
        """
        self.game_state = GameState()
        self.tower_menu = TowerMenu()
        self.view = View(self.game_state, self.tower_menu.towers)
        self.current_tower_clicked = None
        self.last_tower = None
        self.enemy_1 = Enemy(4, (100, 100))
        self.run()

    def run(self):
        """
        Initial function called to run the game. Starts the chain of checking events.
        """
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            self.update()
            clock.tick(60)
            pygame.display.update()

    def check_events(self):
        """
        Function is called every tick. It checks the "events" of pygame, such as window resizing,
        quitting the game, keys pressed, etc.
        """
        mouse_down = False
        for event in pygame.event.get():
            # Check if game quit
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not mouse_down:
                mouse_down = True
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            elif event.type == pygame.VIDEORESIZE:
                self.view.handle_resize(event.w, event.h, self.game_state.board, self.tower_menu)

    def update(self):
        # self.view.redraw_everything(self.game_state.board, self.tower_menu)
        #
        # self.enemy_1.draw(self.view.board_view)
        # self.enemy_1.take_hit(.001)
        # self.enemy_1.move()
        if self.current_tower_clicked:
            self.view.draw_tower_at_mouse(self.current_tower_clicked, self.game_state.board, self.tower_menu)

    def handle_mouse_click(self, mouse_position):
        """
        Handles the mouse clicked at the specific location
        :param mouse_position: the position of the mouse, index 0: y, index 1: x.
        """
        if self.check_button_clicked(mouse_position):
            # A button being pressed means we don't have to continue resolving other effects.
            return

        # This calculation gives us the actual coordinates on the map
        clicked_y = int((mouse_position[1] - self.view.y_offset) // self.view.grid_size)
        clicked_x = int((mouse_position[0] - self.view.x_offset) // self.view.grid_size)

        # If we have not actually clicked on the board we can end here
        if not self.game_state.in_bounds(clicked_x, clicked_y):
            return
        if self.last_tower:
            if self.game_state.board[clicked_y][clicked_x].type_of_field == "g":
                self.check_tower_being_placed(clicked_x, clicked_y)
            else:
                self.view.redraw_everything(self.game_state.board, self.tower_menu)

        # highlight the square in the board
        self.view.highlight_selected_field(clicked_x, clicked_y, self.game_state.board, self.tower_menu)

    def check_tower_being_placed(self, clicked_x, clicked_y):
        # In motion of placing tower, we clicked on grass. This is valid, and we display the tower there.
        self.game_state.board[clicked_y][clicked_x].tower = self.last_tower
        self.view.redraw_everything(self.game_state.board, self.tower_menu)

    def check_button_clicked(self, mouse_position):
        """
        Checks all the buttons and resolves them if they were clicked.
        :param mouse_position: the position of the mouse
        :return: True if there was a button pressed, false otherwise
        """
        self.last_tower = self.current_tower_clicked
        self.current_tower_clicked = None
        if self.view.tower_menu_currently_displaying and self.view.tower_menu_box.collidepoint(mouse_position):
            self.handle_tower_menu_box_clicked(mouse_position)
            return True

        elif not self.view.tower_menu_currently_displaying:
            # tower menu not displayed, therefore check if we collide
            if self.view.reveal_tower_menu_top_button.collidepoint(mouse_position):
                # We have collided with the upper display tower menu button
                self.view.display_tower_menu(True, self.tower_menu)
                return True
            elif self.view.reveal_tower_menu_bottom_button.collidepoint(mouse_position):
                # We have collided with the lower display tower menu button
                self.view.display_tower_menu(False, self.tower_menu)
                return True
        return False

    def handle_tower_menu_box_clicked(self, mouse_position):
        """
        Handles the functions that trigger depending on where we click in the tower_menu_box.
        :param mouse_position: the mouse position. Guaranteed to be on top of the menu bar.
        """
        if self.last_tower:
            self.view.redraw_everything(self.game_state.board, self.tower_menu)
        if self.view.quit_button_hitbox.collidepoint(mouse_position):
            # We have collided with the close tower menu button
            self.view.hide_tower_menu(self.game_state.board)
            return
        for i in range(len(self.view.tower_unit_hitboxes)):
            # We have collided with the menu but not the close button. We check whether we collide with any tower
            # hitboxes. If so, we call a separate function that handles the clicking of that unit.
            if self.view.tower_unit_hitboxes[i].collidepoint(mouse_position):
                self.handle_tower_clicked(self.tower_menu.towers[i])

    def handle_tower_clicked(self, tower):
        self.current_tower_clicked = tower


TowerDefense()
