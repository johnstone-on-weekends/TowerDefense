import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):

    def __init__(self, hp, waypoints):
        super().__init__()
        self.hp = hp
        self.max_hp = hp
        self.speed = 2
        self.position = Vector2(waypoints)  # Position of the enemy

    def take_hit(self, damage_taken):
        """
        The unit takes damage and may die
        :param damage_taken: the damage that the unit takes
        :return: True if the unit died, false otherwise
        """
        self.hp -= damage_taken
        if self.hp <= 0:
            return True
        return False

    def move(self):
        """
        Update the enemy's position
        """
        self.position[0] += 1

    def draw(self, surface):
        """
        Draw the enemy on the given surface
        :param surface: the surface to draw the enemy on
        """
        print(self.position)
        pygame.draw.circle(surface, (255, 0, 0), self.position, self.hp*10)
