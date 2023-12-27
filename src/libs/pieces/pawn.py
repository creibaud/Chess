from src.libs.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, screen, position, color):
        super().__init__(screen, f"assets/pieces/{color}/pawn.png", position, color)
        self.isFirstMove = True
        self.possibleMoves = []
    
    def setPossibleMoves(self, pieces):
        teamPieces = []
        enemyPieces = []

        if self.color == "white":
            teamPieces = pieces[0]
            enemyPieces = pieces[1]
        else:
            teamPieces = pieces[1]
            enemyPieces = pieces[0]

        self.possibleMoves = []