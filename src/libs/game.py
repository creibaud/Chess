import pygame
from src.libs.board import Board
from src.libs.pieces.piece import Piece
class Game:
    def __init__(self, screen, colorTeam):
        self.screen = screen
        self.colorTeam = colorTeam
        self.board = Board(self.screen, self.colorTeam)
        self.pieces = []
        self.initPieces()

    def initPieces(self):
        whitePieces = []

        for i in range(8):
            whitePieces.append(Piece(self.screen, "assets/pieces/white/pawn.png", chr(97 + i) + "2"))

        whitePieces.append(Piece(self.screen, "assets/pieces/white/rook.png", "a1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/knight.png", "b1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/bishop.png", "c1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/queen.png", "d1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/king.png", "e1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/bishop.png", "f1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/knight.png", "g1"))
        whitePieces.append(Piece(self.screen, "assets/pieces/white/rook.png", "h1"))
        
        blackPieces = []

        for i in range(8):
            blackPieces.append(Piece(self.screen, "assets/pieces/black/pawn.png", chr(97 + i) + "7"))

        blackPieces.append(Piece(self.screen, "assets/pieces/black/rook.png", "a8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/knight.png", "b8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/bishop.png", "c8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/queen.png", "d8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/king.png", "e8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/bishop.png", "f8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/knight.png", "g8"))
        blackPieces.append(Piece(self.screen, "assets/pieces/black/rook.png", "h8"))

        self.pieces.append(whitePieces)
        self.pieces.append(blackPieces)

    def piecesResize(self):
        pieceSize = self.board.cells[0][0].width

        for colorTeam in self.pieces:
            for piece in colorTeam:
                path = piece.path
                piece.img = pygame.image.load(path)
                piece.img = pygame.transform.scale(piece.img, (pieceSize, pieceSize))
                piece.rect = piece.img.get_rect()

    def handleResize(self):
        self.board.rectResize()
        self.board.cellsResize()
        self.piecesResize()

    def update(self):
        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.positionPiece(self.board.cells)

    def draw(self):
        self.board.draw()

        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.draw()