import pygame
from src.libs.board import Board
from src.libs.pieces.pawn import Pawn
from src.libs.pieces.rook import Rook
from src.libs.pieces.knight import Knight
from src.libs.pieces.bishop import Bishop
from src.libs.pieces.queen import Queen
from src.libs.pieces.king import King
from src.client.client import Client
class Game:
    def __init__(self, screen, colorTeam="white"):
        self.screen = screen
        self.colorTeam = colorTeam
        self.board = Board(self.screen)
        self.pieceSelected = None
        self.pieces = []
        self.whitePieces = []
        self.blackPieces = []
        self.initPieces()
        host = str(input("Enter the host: "))
        port = int(input("Enter the port: "))
        self.client = Client(host, port)
        self.logs = []
        self.yourTurn = False

    def startClient(self):
        name = input("Name : ")
        self.client.setName(name)
        self.colorTeam = input("Team : ")
        self.yourTurn = True if self.colorTeam == "white" else False
        self.client.start()
        self.board.color = self.colorTeam
        self.board.initCells()

    def initPieces(self):
        self.pieces = []
        self.whitePieces = []

        id = 0

        for i in range(8):
            self.whitePieces.append(Pawn(self.screen, chr(97 + i) + "2", "white", id))
            id += 1

        self.whitePieces.append(Rook(self.screen, "a1", "white", id))
        id += 1
        self.whitePieces.append(Knight(self.screen, "b1", "white", id))
        id += 1
        self.whitePieces.append(Bishop(self.screen, "c1", "white", id))
        id += 1
        self.whitePieces.append(Queen(self.screen, "d1", "white", id))
        id += 1
        self.whitePieces.append(King(self.screen, "e1", "white", id))
        id += 1
        self.whitePieces.append(Bishop(self.screen, "f1", "white", id))
        id += 1
        self.whitePieces.append(Knight(self.screen, "g1", "white", id))
        id += 1
        self.whitePieces.append(Rook(self.screen, "h1", "white", id))
        id += 1
        
        self.blackPieces = []

        for i in range(8):
            self.blackPieces.append(Pawn(self.screen, chr(97 + i) + "7", "black", id))
            id += 1

        self.blackPieces.append(Rook(self.screen, "a8", "black", id))
        id += 1
        self.blackPieces.append(Knight(self.screen, "b8", "black", id))
        id += 1
        self.blackPieces.append(Bishop(self.screen, "c8", "black", id))
        id += 1
        self.blackPieces.append(Queen(self.screen, "d8", "black", id))
        id += 1
        self.blackPieces.append(King(self.screen, "e8", "black", id))
        id += 1
        self.blackPieces.append(Bishop(self.screen, "f8", "black", id))
        id += 1
        self.blackPieces.append(Knight(self.screen, "g8", "black", id))
        id += 1
        self.blackPieces.append(Rook(self.screen, "h8", "black", id))
        id += 1

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
                    if self.pieceSelected == piece:
                        self.pieceSelected = None
                        piece.getCell(self.board.cells).active = False
                    else:
                        self.pieceSelected = piece
                        piece.getCell(self.board.cells).active = True
                        self.pieceSelected.setMoves(self.pieces)
                else:
                    piece.getCell(self.board.cells).active = False
    
    def movePiece(self, event):
        mousePos = pygame.mouse.get_pos()
        
        for row in range(len(self.board.cells)):
            for col in range(len(self.board.cells[row])):
                cell = self.board.cells[row][col]
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if cell.rect.collidepoint(mousePos) and self.pieceSelected is not None:
                        if cell.position in self.pieceSelected.possibleMoves and self.yourTurn:
                            oldPos = self.pieceSelected.position
                            self.pieceSelected.position = cell.position

                            if self.isCheck():
                                self.pieceSelected.position = oldPos
                                self.pieceSelected = None
                            else:
                                if self.pieceSelected.name == "Pawn" and self.pieceSelected.isFirstMove:
                                    self.pieceSelected.isFirstMove = False

                                self.client.sendPosition(self.pieceSelected.id, self.pieceSelected.position)
                                self.pieceSelected = None
                                self.yourTurn = False
                        elif cell.position in self.pieceSelected.attackMoves and self.yourTurn:
                            oldPos = self.pieceSelected.position
                            oldPiece = None
                            for colorTeam in self.pieces:
                                for piece in colorTeam:
                                    if piece.position == cell.position:
                                        oldPiece = piece
                                        colorTeam.remove(piece)
                                        break
                                    
                            self.pieceSelected.position = cell.position

                            if self.isCheck():
                                self.pieceSelected.position = oldPos
                                self.pieceSelected = None
                                oldPiece.position = cell.position
                                color = 0 if oldPiece.color == "white" else 1
                                self.pieces[color].append(oldPiece)
                            else:
                                self.client.sendPosition(self.pieceSelected.id, self.pieceSelected.position)
                                self.pieceSelected = None
                                self.yourTurn = False
                        elif cell.position not in self.pieceSelected.possibleMoves and cell.position not in self.pieceSelected.attackMoves and cell.position != self.pieceSelected.position:
                            self.pieceSelected = None

    def isCheck(self):
        king = None
        for colorTeam in self.pieces:
            for piece in colorTeam:
                if piece.name == "King" and piece.color == self.colorTeam:
                    king = piece
                    break

        for colorTeam in self.pieces:
            for piece in colorTeam:
                if piece.color != self.colorTeam:
                    piece.setMoves(self.pieces)
                    if king.position in piece.attackMoves:
                        return True
        return False
    
    def isCheckMate(self):
        king = None
        for colorTeam in self.pieces:
            for piece in colorTeam:
                if piece.name == "King" and piece.color == self.colorTeam:
                    king = piece
                    break

        king.setMoves(self.pieces)
        if len(king.possibleMoves) == 0 and self.isCheck():
            return True
        return False
    
    def update(self):
        if len(self.logs) < len(self.client.enemyMoves):
            log = self.client.enemyMoves[-1]
            id, position = log.split(":")
            self.logs.append(log)

            teamColor = 0 if self.colorTeam == "white" else 1
            enemyColor = 1 if self.colorTeam == "white" else 0
            for enemyPiece in self.pieces[enemyColor]:
                if enemyPiece.id == int(id):
                    enemyPiece.position = position

                    for teamPiece in self.pieces[teamColor]:
                        if teamPiece.position == position:
                            self.pieces[teamColor].remove(teamPiece)
                            break

                    if enemyPiece.name == "Pawn" and enemyPiece.isFirstMove:
                        enemyPiece.isFirstMove = False
                    break
            
            self.yourTurn = True
        
        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.positionPiece(self.board.cells)

    def draw(self):
        self.board.draw()

        if self.pieceSelected is not None and len(self.pieceSelected.possibleMoves) > 0:
            self.board.drawPossibleMoves(self.pieceSelected.possibleMoves)

        if self.pieceSelected is not None and len(self.pieceSelected.attackMoves) > 0:
            self.board.drawAttackMoves(self.pieceSelected.attackMoves)

        for colorTeam in self.pieces:
            for piece in colorTeam:
                piece.draw()