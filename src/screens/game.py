import pygame
import os
import src.includes.screen as screen
import src.includes.colors as colors
from src.libs.game import Game

class GameScreen:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.run = True
        self.game = Game(self.screen)
    
    def start(self):
        self.game.startClient()
        
        while self.run:
            if self.game.isCheckMate():
                print("Game Over")
                self.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                self.game.selectPiece(event)
                self.game.movePiece(event)

            self.screen.fill(colors.GRAY)

            self.game.handleResize()
            self.game.update()
            self.game.draw()

            pygame.display.update()
            self.clock.tick(screen.FPS)

    def stop(self):
        self.game.client.stop()
        pygame.quit()
        os._exit(0)