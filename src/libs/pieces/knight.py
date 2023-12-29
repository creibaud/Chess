from src.libs.pieces.piece import Piece

class Knight(Piece):
    def __init__(self, screen, position, color, id):
        super().__init__(screen, "Knight", f"assets/pieces/{color}/knight.png", position, color, id)

    def setMoves(self, pieces):
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        self.possibleMoves = []
        self.attackMoves = []

        for dx, dy in moves:
            move = chr(ord(self.position[0]) + dx) + str(int(self.position[1]) + dy)
            if self.moveIsAttackable(move, pieces):
                self.attackMoves.append(move)

            if self.moveIsPossible(move, pieces):
                self.possibleMoves.append(move)