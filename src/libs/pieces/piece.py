import pygame

class Piece:
    def __init__(self, screen, name, path, position, color):
        self.screen = screen
        self.name = name
        self.path = path
        self.img = pygame.image.load(self.path)
        self.position = position
        self.color = color
        self.rect = self.img.get_rect()
        self.possibleMoves = []
        self.attackMoves = []

    def getCell(self, cells):
        for row in range(len(cells)):
            for col in range(len(cells[row])):
                if cells[row][col].position == self.position:
                    return cells[row][col]
                
    def positionPiece(self, cells):
        self.rect.center = self.getCell(cells).rect.center

    def directions(self, pieces, function, liste):
        pass

    def setPossibleMoves(self, pieces):
        pass

    def setAttackMoves(self, pieces):
        pass

    def moveIsPossible(self, move, pieces):
        pass

    def movIsAttackable(self, move, pieces):
        pass

    def draw(self):
        self.screen.blit(self.img, self.rect)