import pygame

class Text:
    def __init__(self, screen, x, y, text, color, font):
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = font

    def draw(self):
        self.screen.blit(self.font.render(self.text, True, self.color), (self.x, self.y))