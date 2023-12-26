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
        self.initCells()

    def initCells(self):
        gridPositions = grid.WHITE if self.color == "white" else grid.BLACK
        cellColor = colors.WHITE

        for row in range(len(gridPositions)):
            self.cells.append([])
            for col in range(len(gridPositions[row])):
                cell = Cell(self.screen, col, row, self.rect.width / 8, self.rect.height / 8, gridPositions[row][col], colors.RED)
                self.cells[row].append(cell)
                cellColor = colors.WHITE if cellColor == colors.DARK_GRAY else colors.DARK_GRAY
    
    def rectResize(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        size = height if width > height else width
        size -= 0.1 * size

        self.rect.width = size
        self.rect.height = size
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
    
    def update(self):
        self.rectResize()
    
    def draw(self):
        pygame.draw.rect(self.screen, colors.WHITE, self.rect)

        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.cells[row][col].draw()