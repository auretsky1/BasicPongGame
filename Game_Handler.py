import Paddle
import Ball
import pygame

class Game_Handler(object):
    #Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.game_objects = []

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

        #Initialize game ball

        #Initialize game score

    def game_logic(self):
        for game_object in self.game_objects:
            game_object.game_object_update()

    def draw_game_objects(self):
        for game_object in self.game_objects:
            game_object.game_object_draw()

    def process_event(self, event):
        #Variables used for event processing
        y_up = (-((self.game_screen.get_height()/6)/60))
        y_down = ((self.game_screen.get_height()/6)/60)

        #Process player paddle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game_paddle_one.change_y_vel(y_up)
            if event.key == pygame.K_DOWN:
                self.game_paddle_one.change_y_vel(y_down)
        if event.type == pygame.KEYUP:
            self.game_paddle_one.stop_moving()

        #Process player options (start game/end game/etc)