import pygame
import src.includes.colors as colors

class Cell:
    def __init__(self, screen, x, y, width, height, position, color, active=False):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.position = position
        self.color = color
        self.activeColor = colors.WHITE_SELECTED if self.color == colors.WHITE else colors.BLACK_SELECTED
        self.active = active
        self.borderTopLeft = -1
        self.borderTopRight = -1
        self.borderBottomLeft = -1
        self.borderBottomRight = -1

    def drawPossibleMove(self):
        if self.color == colors.WHITE:
            pygame.draw.circle(self.screen, colors.WHITE_POSSIBLE, self.rect.center, self.rect.width * 0.15)
        else:
            pygame.draw.circle(self.screen, colors.BLACK_POSSIBLE, self.rect.center, self.rect.width * 0.15)
    
    def drawAttackMove(self):
        if self.color == colors.WHITE:
            pygame.draw.circle(self.screen, colors.WHITE_POSSIBLE, self.rect.center, self.rect.width // 2, int(self.rect.width * 0.1))
        else:
            pygame.draw.circle(self.screen, colors.BLACK_POSSIBLE, self.rect.center, self.rect.width // 2, int(self.rect.width * 0.1))
    
    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.activeColor, self.rect, border_top_left_radius=self.borderTopLeft, border_top_right_radius=self.borderTopRight, border_bottom_left_radius=self.borderBottomLeft, border_bottom_right_radius=self.borderBottomRight)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect, border_top_left_radius=self.borderTopLeft, border_top_right_radius=self.borderTopRight, border_bottom_left_radius=self.borderBottomLeft, border_bottom_right_radius=self.borderBottomRight)