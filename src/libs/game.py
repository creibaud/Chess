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
        self.showPossibleMoves = False

    def initPieces(self):
        self.pieces = []
        self.whitePieces = []

        for i in range(8):
            self.whitePieces.append(Pawn(self.screen, chr(97 + i) + "2", "white"))

        self.whitePieces.append(Rook(self.screen, "a1", "white"))
        self.whitePieces.append(Knight(self.screen, "b1", "white"))
        self.whitePieces.append(Bishop(self.screen, "c1", "white"))
        self.whitePieces.append(Queen(self.screen, "d1", "white"))
        self.whitePieces.append(King(self.screen, "e1", "white"))
        self.whitePieces.append(Bishop(self.screen, "f1", "white"))
        self.whitePieces.append(Knight(self.screen, "g1", "white"))
        self.whitePieces.append(Rook(self.screen, "h1", "white"))
        
        self.blackPieces = []

        for i in range(8):
            self.blackPieces.append(Pawn(self.screen, chr(97 + i) + "7", "black"))

        self.blackPieces.append(Rook(self.screen, "a8", "black"))
        self.blackPieces.append(Knight(self.screen, "b8", "black"))
        self.blackPieces.append(Bishop(self.screen, "c8", "black"))
        self.blackPieces.append(Queen(self.screen, "d8", "black"))
        self.blackPieces.append(King(self.screen, "e8", "black"))
        self.blackPieces.append(Bishop(self.screen, "f8", "black"))
        self.blackPieces.append(Knight(self.screen, "g8", "black"))
        self.blackPieces.append(Rook(self.screen, "h8", "black"))

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
                    self.showPossibleMoves = True
                    self.pieceSelected.setPossibleMoves(self.pieces)
                else:
                    piece.getCell(self.board.cells).active = False
                    self.showPossibleMoves = False

    def update(self):
        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.positionPiece(self.board.cells)

    def draw(self):
        self.board.draw()

        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.draw()

        if self.showPossibleMoves:
            self.board.drawPossibleMoves(self.pieceSelected.possibleMoves)