import pygame

class Piece:
    def __init__(self, screen, path, position):
        self.screen = screen
        self.path = path
        self.img = pygame.image.load(self.path)
        self.position = position
        self.rect = self.img.get_rect()

    def positionPiece(self, cells):
        for row in range(len(cells)):
            for col in range(len(cells[row])):
                if cells[row][col].position == self.position:
                    self.rect.center = cells[row][col].rect.center

    def draw(self):
        self.screen.blit(self.img, self.rect)