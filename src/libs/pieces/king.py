from src.libs.pieces.piece import Piece

class King(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "King", f"assets/pieces/{color}/king.png", position, color)

    def setMoves(self, pieces):
        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        self.possibleMoves = []
        self.attackMoves = []

        for dx, dy in moves:
            move = chr(ord(self.position[0]) + dx) + str(int(self.position[1]) + dy)
            if self.moveIsAttackable(move, pieces):
                self.attackMoves.append(move)

            if self.moveIsPossible(move, pieces):
                self.possibleMoves.append(move)