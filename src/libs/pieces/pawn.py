from src.libs.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "Pawn", f"assets/pieces/{color}/pawn.png", position, color)
        self.isFirstMove = True
    
    def setPossibleMoves(self, pieces):
        self.possibleMoves = []
        
        moves = {
            "white": [1, 2],
            "black": [-1, -2]
        }

        move = self.position[0] + str(int(self.position[1]) + moves[self.color][0])
        if self.moveIsPossible(move, pieces):
            self.possibleMoves.append(move)
            move = self.position[0] + str(int(self.position[1]) + moves[self.color][1])
            if self.moveIsPossible(move, pieces) and self.isFirstMove:
                self.possibleMoves.append(move)

    def setAttackMoves(self, pieces):
        self.attackMoves = []
        moves = {
            "white": [(-1, 1), (1, 1)],
            "black": [(-1, -1), (1, -1)]
        }

        for dx, dy in moves[self.color]:
            move = chr(ord(self.position[0]) + dx) + str(int(self.position[1]) + dy)
            if self.moveIsAttackable(move, pieces):
                self.attackMoves.append(move)

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