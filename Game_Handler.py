import pygame
import Paddle
import Ball
import Game_Text
import Field_Line

class Game_Handler(object):

    # Constructor
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.game_objects = []
        self.game_writing = []

        # initialize vertical field line
        self.vertical_field_line = Field_Line.Field(game_screen, 2, 20,
                                                    (game_screen.get_width()/2) - 1,
                                                    0, 0, 0, 0, 1)
        # add vertical field line to objects
        self.game_objects.append(self.vertical_field_line)

        # Initialize game paddles
        self.game_paddle_one = Paddle.Paddle(game_screen, 10, 60, 20,
                                            ((game_screen.get_height()/2)-25),
                                            0, 0, 0, 1)

        self.game_paddle_two = Paddle.Paddle(game_screen, 10, 60,
                                             game_screen.get_width()-20-10,
                                             ((game_screen.get_height()/2)-25),
                                             0, 0, 0, 1)




        # Add the paddles to the list of game objects
        self.game_objects.append(self.game_paddle_one)
        self.game_objects.append(self.game_paddle_two)

        # Initialize game ball
        self.game_ball = Ball.Ball(game_screen, 10, 10, 3,
                                   ((game_screen.get_width()/2)-5),
                                   ((game_screen.get_height()/2)-5),
                                   0, 0, 0, 1)

        # Add the ball to the list of game objects
        self.game_objects.append(self.game_ball)
        # Initialize game score
        self.game_score = Game_Text.game_text(game_screen, 0, 0, 0, (game_screen.get_width()/2)- 80, 20, 0, 0, 0, 0)
        self.ai_game_score = Game_Text.game_text(game_screen, 0, 0, 0, (game_screen.get_width()/2) + 61, 20, 0, 0, 0, 0)

        # add game score to list of objects
        self.game_objects.append(self.game_score)
        self.game_objects.append(self.ai_game_score)



    def game_logic(self):
        self.game_objects[1].game_object_update(self.game_ball)
        self.game_objects[2].game_object_update(self.game_ball)
        self.game_objects[2].game_ai_update(self.game_screen, self.game_ball)
        self.game_objects[3].game_object_update(self.game_paddle_one, self.game_paddle_two, self.game_score, self.ai_game_score)
        self.game_objects[4].game_object_update()
        self.game_objects[5].game_object_update()
        self.game_objects[0].game_object_update()

    def draw_game_objects(self):
        for game_object in self.game_objects:
            game_object.game_object_draw()

    def process_event(self, event):
        # Process game ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game_ball.reset_ball()
                self.game_ball.init_velocity()

        # Process player paddle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game_paddle_one.move_up()
            if event.key == pygame.K_DOWN:
                self.game_paddle_one.move_down()
        if event.type == pygame.KEYUP:
            self.game_paddle_one.stop_moving()

        # Process player options (start game/end game/etc)