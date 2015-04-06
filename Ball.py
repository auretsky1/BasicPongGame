import pygame
import random
import math
import Game_Object


class Ball(Game_Object.Game_Object):

    def __init__(self, game_screen, x_size, y_size, speed=0, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size
        self.speed = speed

    def game_object_update(self):
        #Adjust the position of the ball by the x_vel & y_vel
        self.y_position += self.y_vel
        self.x_position += self.x_vel

        #Check to make sure the ball hasn't collided with the
        #edges of the screen, either top or bottom.
        if self.y_position + self.y_size >= self.game_screen.get_height() or self.y_position <= 0:
            self.y_vel = (-(self.y_vel))

        #Check to make sure the ball hasn't collided with the
        #left or right side of the screen, and if it did reset it's position.
        if self.x_position + self.x_size >= self.game_screen.get_width() or self.x_position <= 0:
            self.reset_ball()

    def game_object_draw(self):
        pygame.draw.ellipse(self.game_screen, (0, 0, 255), [self.x_position,
                                                            self.y_position,
                                                            self.x_size,
                                                            self.y_size])

    #Resets the ball to the center of the screen
    def reset_ball(self):
        self.stop_moving()
        self.x_position = ((self.game_screen.get_width()/2)-5)
        self.y_position = ((self.game_screen.get_height()/2)-5)

    #Initialize the velocity of the ball after it has been reset (can also be used while moving)
    def init_velocity(self):
        #Seed the random number generator and produce a random number equal to the angle the ball will travel
        random.seed()
        direction_angle = random.randint(0, 361)

        #Set the velocity in proportion of the angle using pythagoreans therum
        self.y_vel = self.speed * math.sin(direction_angle)
        self.x_vel = self.speed * math.cos(direction_angle)

