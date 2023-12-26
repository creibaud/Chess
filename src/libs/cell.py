import pygame

class Cell:
    def __init__(self, screen, x, y, width, height, position, color, borderTopLeft=-1, borderTopRight=-1, borderBottomLeft=-1, borderBottomRight=-1):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.position = position
        self.color = color
        self.borderTopLeft = borderTopLeft
        self.borderTopRight = borderTopRight
        self.borderBottomLeft = borderBottomLeft
        self.borderBottomRight = borderBottomRight
        self.piece = None

    def isEmpty(self):
        if self.piece is None:
            return True
        return False
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_top_left_radius=self.borderTopLeft, border_top_right_radius=self.borderTopRight, border_bottom_left_radius=self.borderBottomLeft, border_bottom_right_radius=self.borderBottomRight)