import pygame

class Piece:
    def __init__(self, screen, name, path, position, color, id):
        self.screen = screen
        self.name = name
        self.path = path
        self.img = pygame.image.load(self.path)
        self.position = position
        self.color = color
        self.rect = self.img.get_rect()
        self.id = id
        self.possibleMoves = []
        self.attackMoves = []

    def getCell(self, cells):
        for row in range(len(cells)):
            for col in range(len(cells[row])):
                if cells[row][col].position == self.position:
                    return cells[row][col]
                
    def positionPiece(self, cells):
        self.rect.center = self.getCell(cells).rect.center

    def setPossibleMoves(self, pieces):
        pass

    def setAttackMoves(self, pieces):
        pass

    def setMoves(self, pieces):
        pass

    def moveIsPossible(self, move, pieces):
        if len(move) > 2:
            return False
        
        if move[0] not in "abcdefgh" or int(move[1]) not in range(1, 9):
            return False

        for colorTeam in pieces:
            for piece in colorTeam:
                if piece.position == move:
                    return False
        return True
    
    def moveIsAttackable(self, move, pieces):
        if len(move) > 2:
            return False
        
        if move[0] not in "abcdefgh" or int(move[1]) not in range(1, 9):
            return False

        enemyTeam = 1 if self.color == "white" else 0

        for piece in pieces[enemyTeam]:
            if piece.position == move:
                return True
        return False

    def draw(self):
        self.screen.blit(self.img, self.rect)