import pygame
import Game_Object

class Ball(Game_Object.Game_Object):

    def __init__(self, game_screen):
        pass

    def game_object_draw(self):
        pygame.draw.circle(self.game_screen, (0, 0, 255), (200, 200), 50, 1)