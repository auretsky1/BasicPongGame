import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode()
(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False



if __name__ == "__main__":
    print("Pong")
    print("Python3 Game")