from src.libs.pieces.piece import Piece

class Queen(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "Queen", f"assets/pieces/{color}/queen.png", position, color)