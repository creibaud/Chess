from src.libs.board import Board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(self.screen, "white")

    def update(self):
        self.board.update()

    def draw(self):
        self.board.draw()