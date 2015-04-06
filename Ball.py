import pygame
import Game_Object
import Game_Handler
import random
import math
import Paddle


class Ball(Game_Object.Game_Object):

    def __init__(self, game_screen, x_size, y_size, speed, direction, reset, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size
        self.reset = reset
        self.speed = speed
        self.direction = direction
    def game_object_update(self):
        #Adjust the y_position of the paddle by the y_vel
        self.y_position += self.y_vel
        self.x_position += self.x_vel

        #Check to make sure the paddle hasn't collided with the
        #edges of the screen, either top or bottom.
        if self.y_position + self.y_size >= self.game_screen.get_height() or self.y_position <= 0:
            self.y_vel = (-(self.y_vel))
        if self.x_position + self.x_size >= self.game_screen.get_width() or self.x_position <= 0:
            if self.reset == 1:
                Ball.stop_moving(self)
                self.x_position = ((self.game_screen.get_width()/2)-5)
                self.y_position = ((self.game_screen.get_height()/2)-5)
                self.reset = 0


    def game_object_draw(self):
        pygame.draw.ellipse(self.game_screen, (0, 0, 255), [self.x_position,
                                                            self.y_position,
                                                            self.x_size,
                                                            self.y_size])