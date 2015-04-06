import Paddle
import Ball
import pygame
import random
import math



class Game_Handler(object):
    #Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.game_objects = []
        self.game_writing = []

        #Initialize game paddles
        self.game_paddle_one = Paddle.Paddle(game_screen, 20, 50, 20,
                                            ((game_screen.get_height()/2)-25),
                                            0, 0, 0, 1)

        self.game_paddle_two = Paddle.Paddle(game_screen, 20, 50,
                                             game_screen.get_width()-40,
                                             ((game_screen.get_height()/2)-25),
                                             0, 0, 0, 1)

        #Add the paddles to the list of game objects
        self.game_objects.append(self.game_paddle_one)
        self.game_objects.append(self.game_paddle_two)


        # Initialize game ball

        self.game_Ball = Ball.Ball(game_screen, 10, 10, 5, 0, 0,
                                   ((game_screen.get_width()/2)-5),
                                   ((game_screen.get_height()/2)-5),
                                   0, 0, 0, 1)

        #Add the ball to the list of game objects
        self.game_objects.append(self.game_Ball)

        #Initialize game score
        #self.game_Text = Game_Text.game_text(game_screen,

        #self.game_objects.append(self.game_Text)

    def game_logic(self):
        for game_object in self.game_objects:
            game_object.game_object_update()


    def draw_game_objects(self):
        for game_object in self.game_objects:
            game_object.game_object_draw()

    def process_event(self, event):
        #Variables used for event processing
        y_up = (-((self.game_screen.get_height()/2)/60))
        y_down = ((self.game_screen.get_height()/2)/60)
        direction_radians = random.randint(0, 361)
        self.game_Ball.direction = direction_radians
        x_value = self.game_Ball.speed * math.sin(direction_radians)
        y_value = self.game_Ball.speed * math.cos(direction_radians)


        #Process game ball

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.game_Ball.reset == 0:
                    self.game_Ball.change_x_vel(x_value)
                    self.game_Ball.change_y_vel(y_value)
                    self.game_Ball.reset = 1

        #Process player paddle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game_paddle_one.change_y_vel(y_up)
            if event.key == pygame.K_DOWN:
                self.game_paddle_one.change_y_vel(y_down)
        if event.type == pygame.KEYUP:
            self.game_paddle_one.stop_moving()


        #Process player options (start game/end game/etc)