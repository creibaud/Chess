import pygame
import src.includes.colors as colors
import src.includes.grid as grid
from src.libs.cell import Cell
from src.tools.text import Text

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.color = "white"
        self.rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        self.cells = []
        self.rectResize()

    def initCells(self):
        gridPositions = grid.WHITE if self.color == "white" else grid.BLACK
        cellColor = colors.WHITE
        cellSize = self.rect.width / 8

        for row in range(len(gridPositions)):
            self.cells.append([])
            for col in range(len(gridPositions[row])):
                cell = Cell(self.screen, self.rect.x + col * cellSize, self.rect.y + row * cellSize, cellSize, cellSize, gridPositions[row][col], cellColor)
                if row == 0 and col == 0:
                    cell.borderTopLeft = 5
                elif row == 0 and col == 7:
                    cell.borderTopRight = 5
                elif row == 7 and col == 0:
                    cell.borderBottomLeft = 5
                elif row == 7 and col == 7:
                    cell.borderBottomRight = 5

                self.cells[row].append(cell)
                cellColor = colors.WHITE if cellColor == colors.BLACK else colors.BLACK
            cellColor = colors.WHITE if cellColor == colors.BLACK else colors.BLACK
    
    def rectResize(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        size = height if width > height else width
        size -= 0.1 * size
        size += (8 - size % 8)

        self.rect.width = size
        self.rect.height = size
        self.rect.centerx = width / 2
        self.rect.centery = height / 2

    def cellsResize(self):
        cellSize = self.rect.width / 8

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                cell.x = self.rect.x + col * cellSize
                cell.y = self.rect.y + row * cellSize
                cell.width = cellSize
                cell.height = cellSize
                cell.rect = pygame.Rect(cell.x, cell.y, cell.width, cell.height)
    
    def drawPossibleMoves(self, possibleMoves):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.position in possibleMoves:
                    cell.drawPossibleMove()

    def drawAttackMoves(self, attackMoves):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.position in attackMoves:
                    cell.drawAttackMove()
    
    def draw(self):
        pygame.draw.rect(self.screen, colors.GRAY, self.rect, border_radius=5)

        textColor = colors.BLACK
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                cell.draw()
                cellSize = cell.width

                if row == len(self.cells) - 1 or row == len(self.cells) - 1 and col == 0:
                    text = Text(self.screen, cell.position[0], 0, 0, "assets/fonts/roboto/Roboto-Regular.ttf", int(0.18 * cellSize), textColor)
                    text.x = cell.x + cellSize * 0.95 - text.text.get_width()
                    text.y = cell.y + cellSize * 0.98 - text.text.get_height()
                    text.rect.x = text.x
                    text.rect.y = text.y
                    text.draw()
                    
                if col == 0:
                    text = Text(self.screen, cell.position[1], 0, 0, "assets/fonts/roboto/Roboto-Regular.ttf", int(0.18 * cellSize), textColor)
                    text.x = cell.x + cellSize * 0.05
                    text.y = cell.y + cellSize * 0.05
                    text.rect.x = text.x
                    text.rect.y = text.y
                    text.draw()
                    
                textColor = colors.WHITE if textColor == colors.BLACK else colors.BLACK
            textColor = colors.WHITE if textColor == colors.BLACK else colors.BLACK