import pygame
from tools.text import Text

class InputText:
    def __init__(self, screen, x, y, width, height, textColor, color, activeColor, font):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.activeColor = activeColor
        self.actualText = Text(self.screen, x, y, "ZZ", textColor, font)
        self.active = False

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.x < event.pos[0] < self.x + self.width and self.y < event.pos[1] < self.y + self.height:
                    self.active = True
                else:
                    self.active = False

    def handleKey(self, event):
        if self.active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.actualText.text = self.actualText.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.active = False

    def handleHover(self):
        if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.activeColor, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        
        self.actualText.draw()