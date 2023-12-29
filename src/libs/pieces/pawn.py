from src.libs.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, screen, position, color, id):
        super().__init__(screen, "Pawn", f"assets/pieces/{color}/pawn.png", position, color, id)
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
    
    def setMoves(self, pieces):
        self.setPossibleMoves(pieces)
        self.setAttackMoves(pieces)