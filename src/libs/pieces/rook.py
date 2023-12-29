from src.libs.pieces.piece import Piece

class Rook(Piece):
    def __init__(self, screen, position, color, id):
        super().__init__(screen, "Rook", f"assets/pieces/{color}/rook.png", position, color, id)
    
    def setMoves(self, pieces):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.possibleMoves = []
        self.attackMoves = []

        for dx, dy in moves:
            x, y = ord(self.position[0]), int(self.position[1])
            while 97 <= x <= 104 and 0 <= y <= 8:
                move = chr(x + dx) + str(y + dy)
                if self.moveIsPossible(move, pieces):
                    self.possibleMoves.append(move)

                if self.moveIsAttackable(move, pieces):
                    self.attackMoves.append(move)
                    break

                if not self.moveIsPossible(move, pieces) and not self.moveIsAttackable(move, pieces):
                    break

                x += dx
                y += dy