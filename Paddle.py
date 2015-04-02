import pygame
import Game_Object

class Paddle(Game_Object.Game_Object):

    def __init__(self, game_screen, x_size, y_size, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size

    def game_object_update(self):
        #Adjust the y_position of the paddle by the y_vel
        self.y_position += self.y_vel

        #Check to make sure the paddle hasn't collided with the
        #edges of the screen, either top or bottom.
        if self.y_position + self.y_size > self.game_screen.get_height():
            self.y_position = self.game_screen.get_height() - self.y_size

        if self.y_position <= 0:
            self.y_position = 0

    def game_object_draw(self):
        pygame.draw.rect(self.game_screen, (255, 0, 0), [self.x_position,
                                                         self.y_position,
                                                         self.x_size,
                                                         self.y_size])