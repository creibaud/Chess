import pygame

class Text:
    def __init__(self, screen, text, x, y, font, size, color):
        pygame.font.init()
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.size = size
        self.color = color
        self.font = pygame.font.Font(self.font, self.size)
        self.text = self.font.render(self.text, True, self.color)
        self.rect = self.text.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.text, self.rect)