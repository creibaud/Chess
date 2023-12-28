from src.libs.pieces.piece import Piece

class King(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "King", f"assets/pieces/{color}/king.png", position, color)

    def directions(self, pieces, function, liste):
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in moves:
            move = chr(ord(self.position[0]) + dx) + str(int(self.position[1]) + dy)
            if function(move, pieces):
                liste.append(move) 
    
    def setPossibleMoves(self, pieces):
        self.possibleMoves = []
        self.directions(pieces, self.moveIsPossible, self.possibleMoves)

    def setAttackMoves(self, pieces):
        self.attackMoves = []
        self.directions(pieces, self.moveIsAttackable, self.attackMoves)

    def moveIsPossible(self, move, pieces):
        if move[0] not in "abcdefgh" or int(move[1]) not in range(1, 9):
            return False

        for colorTeam in pieces:
            for piece in colorTeam:
                if piece.position == move:
                    return False
        return True
    
    def moveIsAttackable(self, move, pieces):
        if move[0] not in "abcdefgh" or int(move[1]) not in range(1, 9):
            return False

        enemyTeam = 1 if self.color == "white" else 0

        for piece in pieces[enemyTeam]:
            if piece.position == move:
                return True
        return False