import pygame
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):

    def __init__(self, hp, waypoints):
        super().__init__()
        self.hp = hp
        self.max_hp = hp
        self.speed = 2
        self.waypoints = waypoints
        self.position = Vector2(waypoints[0])  # Position of the enemy
        self.target_waypoint = 1
        self.dead = False

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
        if self.target_waypoint >= len(self.waypoints):
            self.dead = True
            return

        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.position
        dist = self.movement.length()
        if dist >= self.speed:
            self.position += self.movement.normalize() * self.speed
        else:
            if dist != 0:
                self.position += self.movement.normalize() * dist
            self.target_waypoint += 1

    def draw(self, surface, x_offset, y_offset):
        """
        Draw the enemy on the given surface
        :param surface: the surface to draw the enemy on
        """
        if not self.dead:
            pygame.draw.circle(surface, (255, 0, 0),
                               (self.position[0] + x_offset, self.position[1] + y_offset), self.hp * 10)
