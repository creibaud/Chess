import pygame
import src.includes.colors as colors
import src.includes.grid as grid
from src.libs.cell import Cell

class Board:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        self.cells = []
        self.rectResize()
        self.initCells()

    def initCells(self):
        gridPositions = grid.WHITE if self.color == "white" else grid.BLACK
        cellColor = colors.WHITE
        cellSize = self.rect.width / 8

        for row in range(len(gridPositions)):
            self.cells.append([])
            for col in range(len(gridPositions[row])):
                cell = Cell(self.screen, self.rect.x + col * cellSize, self.rect.y + row * cellSize, cellSize, cellSize, gridPositions[row][col], cellColor)
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

    def cellResize(self):
        cellSize = self.rect.width / 8

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.cells[row][col].x = self.rect.x + col * cellSize
                self.cells[row][col].y = self.rect.y + row * cellSize
                self.cells[row][col].width = cellSize
                self.cells[row][col].height = cellSize
                self.cells[row][col].rect = pygame.Rect(self.cells[row][col].x, self.cells[row][col].y, self.cells[row][col].width, self.cells[row][col].height)
    
    def update(self):
        self.rectResize()
        self.cellResize()
    
    def draw(self):
        pygame.draw.rect(self.screen, colors.GRAY, self.rect)

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.cells[row][col].draw()