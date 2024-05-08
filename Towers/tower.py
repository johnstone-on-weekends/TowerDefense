import pygame


class Tower:
    def __init__(self, name):
        self.name = name
        self.icon_image = pygame.image.load(f"assets/images/{name}.png")

    def init_image(self):
        self.icon_image = pygame.image.load(f"assets/images/{self.name}.png")
