import pygame

class Cell:
    def __init__(self, screen, x, y, width, height, position, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.position = position
        self.color = color
        self.piece = None

    def isEmpty(self):
        if self.piece is None:
            return True
        return False
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)