import pygame


class Tower:
    def __init__(self, image):
        self.image_name = image
        self.image = pygame.image.load(f"assets/images/{image}.png")

    def init_image(self):
        self.image = pygame.image.load(f"assets/images/{self.image_name}.png")
