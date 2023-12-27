from src.libs.pieces.piece import Piece

class Rook(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, f"assets/pieces/{color}/rook.png", position, color)