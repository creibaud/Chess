import pygame
import settings.main as settings
from tools.text import Text
from tools.button import Button

class Screen:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((settings.screen.WIDTH, settings.screen.HEIGHT))
        pygame.display.set_caption("Chess")

        self.icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(self.icon)

        self.homeRun = True
        self.gameRun = False

    def startGame(self):
        self.homeRun = False
        self.gameRun = True

    def returnToHome(self):
        self.gameRun = False
        self.homeRun = True

    def homeScreen(self):
        self.screen = pygame.display.set_mode((settings.screen.WIDTH, settings.screen.HEIGHT))
        startGameButton = Button(self.screen, self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 + 100, 200, 75, settings.colors.GRAY, settings.colors.DARK_GRAY, "START", settings.colors.WHITE, pygame.font.SysFont("Arial", 30), self.startGame)

        textLogo = "CHESS"
        fontLogo = pygame.font.SysFont("Arial", 100)
        logoText = Text(self.screen, self.screen.get_width() / 2 - (fontLogo.size(textLogo)[0] / 2), self.screen.get_height() / 2 - (fontLogo.size(textLogo)[1] / 2) + 40, textLogo, settings.colors.WHITE, fontLogo)

        while self.homeRun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.homeRun = False
                
                startGameButton.handleClick(event)
        
            self.screen.fill(settings.colors.GRAY)

            self.screen.blit(self.icon, (0, 0))
            logoText.draw()

            startGameButton.handleHover()
            startGameButton.draw()

            pygame.display.update()
            self.clock.tick(settings.screen.FPS)

    def gameScreen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        exitGameButton = Button(self.screen, self.screen.get_width() - 150, 50, 100, 50, settings.colors.RED, settings.colors.DARK_RED, "QUIT", settings.colors.WHITE, pygame.font.SysFont("Arial", 30), self.returnToHome)

        while self.gameRun:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameRun = False

                exitGameButton.handleClick(event)
        
            self.screen.fill(settings.colors.GRAY)

            exitGameButton.handleHover()
            exitGameButton.draw()

            pygame.display.update()
            self.clock.tick(settings.screen.FPS)
    
    def run(self):
        while self.homeRun or self.gameRun:
            if self.homeRun:
                self.homeScreen()

            if self.gameRun:
                self.gameScreen()

    def quit(self):
        pygame.quit()