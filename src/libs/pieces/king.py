from src.libs.pieces.piece import Piece

class King(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, "King", f"assets/pieces/{color}/king.png", position, color)