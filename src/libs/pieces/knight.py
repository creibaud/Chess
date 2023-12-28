from src.libs.pieces.piece import Piece

class Knight(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "Knight", f"assets/pieces/{color}/knight.png", position, color)