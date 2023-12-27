import pygame
from src.libs.board import Board
from src.libs.pieces.pawn import Pawn
from src.libs.pieces.rook import Rook
from src.libs.pieces.knight import Knight
from src.libs.pieces.bishop import Bishop
from src.libs.pieces.queen import Queen
from src.libs.pieces.king import King
class Game:
    def __init__(self, screen, colorTeam):
        self.screen = screen
        self.colorTeam = colorTeam
        self.board = Board(self.screen, self.colorTeam)
        self.pieceSelected = None
        self.pieces = []
        self.whitePieces = []
        self.blackPieces = []
        self.initPieces()

    def initPieces(self):
        self.pieces = []
        self.whitePieces = []

        for i in range(8):
            self.whitePieces.append(Pawn(self.screen, "assets/pieces/white/pawn.png", chr(97 + i) + "2"))

        self.whitePieces.append(Rook(self.screen, "assets/pieces/white/rook.png", "a1"))
        self.whitePieces.append(Knight(self.screen, "assets/pieces/white/knight.png", "b1"))
        self.whitePieces.append(Bishop(self.screen, "assets/pieces/white/bishop.png", "c1"))
        self.whitePieces.append(Queen(self.screen, "assets/pieces/white/queen.png", "d1"))
        self.whitePieces.append(King(self.screen, "assets/pieces/white/king.png", "e1"))
        self.whitePieces.append(Bishop(self.screen, "assets/pieces/white/bishop.png", "f1"))
        self.whitePieces.append(Knight(self.screen, "assets/pieces/white/knight.png", "g1"))
        self.whitePieces.append(Rook(self.screen, "assets/pieces/white/rook.png", "h1"))
        
        self.blackPieces = []

        for i in range(8):
            self.blackPieces.append(Pawn(self.screen, "assets/pieces/black/pawn.png", chr(97 + i) + "7"))

        self.blackPieces.append(Rook(self.screen, "assets/pieces/black/rook.png", "a8"))
        self.blackPieces.append(Knight(self.screen, "assets/pieces/black/knight.png", "b8"))
        self.blackPieces.append(Bishop(self.screen, "assets/pieces/black/bishop.png", "c8"))
        self.blackPieces.append(Queen(self.screen, "assets/pieces/black/queen.png", "d8"))
        self.blackPieces.append(King(self.screen, "assets/pieces/black/king.png", "e8"))
        self.blackPieces.append(Bishop(self.screen, "assets/pieces/black/bishop.png", "f8"))
        self.blackPieces.append(Knight(self.screen, "assets/pieces/black/knight.png", "g8"))
        self.blackPieces.append(Rook(self.screen, "assets/pieces/black/rook.png", "h8"))

        self.pieces.append(self.whitePieces)
        self.pieces.append(self.blackPieces)

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

    def selectPiece(self, event):
        mousePos = pygame.mouse.get_pos()
        
        actualPieces = self.whitePieces if self.colorTeam == "white" else self.blackPieces
        for piece in actualPieces:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if piece.rect.collidepoint(mousePos):
                    self.pieceSelected = piece
                    piece.getCell(self.board.cells).active = True
                else:
                    piece.getCell(self.board.cells).active = False

    def update(self):
        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.positionPiece(self.board.cells)

    def draw(self):
        self.board.draw()

        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.draw()