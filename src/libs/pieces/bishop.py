from src.libs.pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, f"assets/pieces/{color}/bishop.png", position, color)