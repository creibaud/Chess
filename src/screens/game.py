import pygame
import src.includes.screen as screen
import src.includes.colors as colors
from src.libs.game import Game

class GameScreen:
    def __init__(self, screen, clock, colorTeam):
        self.screen = screen
        self.clock = clock
        self.run = True
        self.game = Game(self.screen, colorTeam)
    
    def start(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.screen.fill(colors.GRAY)

            self.game.handleResize()
            self.game.update()
            self.game.draw()

            pygame.display.update()
            self.clock.tick(screen.FPS)

    def stop(self):
        pygame.quit()