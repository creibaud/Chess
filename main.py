import pygame
import src.includes.screen as screenSettings
from src.screens.game import GameScreen

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screenSettings.WIDTH, screenSettings.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess")

icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

gameScreen = GameScreen(screen, clock, "white")
gameScreen.start()
gameScreen.stop()