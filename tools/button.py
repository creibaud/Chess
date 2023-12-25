import pygame
from tools.text import Text

class Button:
    def __init__(self, screen, x, y, width, height, color, hoverColor, text, textColor, font, action):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hoverColor = hoverColor
        self.action = action
        self.text = Text(self.screen, self.x + (self.width / 2) - (font.size(text)[0] / 2), self.y + (self.height / 2) - (font.size(text)[1] / 2) + 2, text, textColor, font)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handleHover(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            return True
        return False

    def handleClick(self, event):
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.handleHover():
                self.action()

    def draw(self):
        color = self.color
        if self.handleHover():
            color = self.hoverColor

        pygame.draw.rect(self.screen, color, self.rect, border_radius=5)
        self.text.draw()