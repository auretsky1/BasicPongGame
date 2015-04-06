import pygame
import Game_Object


class Paddle(Game_Object.Game_Object):

    def __init__(self, game_screen, x_size, y_size, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size

    def game_object_update(self, current_ball):
        # Adjust the y_position of the paddle by the y_vel
        self.y_position += self.y_vel

        # Check to make sure the paddle hasn't collided with the
        # edges of the screen, either top or bottom.
        if self.y_position + self.y_size > self.game_screen.get_height():
            self.y_position = self.game_screen.get_height() - self.y_size

        if self.y_position <= 0:
            self.y_position = 0

        # Check to see if the paddle is moving, and if so if it's moved into the ball
        if self.y_vel != 0:
            if self.paddle_ball_intersect_check(current_ball):
                if self.y_vel > 0:
                    current_ball.push_down(self)
                    current_ball.neg_abs_vel(1)

                if self.y_vel < 0:
                    current_ball.push_up(self)
                    current_ball.abs_vel(1)

    def game_object_draw(self):
        pygame.draw.rect(self.game_screen, (255, 0, 0), [self.x_position,
                                                         self.y_position,
                                                         self.x_size,
                                                         self.y_size])

    # Checks to see if the ball and paddle have intersected
    def paddle_ball_intersect_check(self, ball):
        # Variables holding the relevant points in the ball to be checked against
        ball_rad = ball.x_size / 2
        ball_center_x = ball.x_position + (ball.x_size / 2)
        ball_center_y = ball.y_position + (ball.y_size / 2)
        x_intersect = ball_center_x
        y_intersect = ball_center_y

        # Check each vertex of the paddle to see if it's closest to the ball's center
        if ball_center_x < self.x_position:
            x_intersect = self.x_position

        elif ball_center_x > (self.x_position + self.x_size):
            x_intersect = self.x_position + self.x_size

        if ball_center_y > self.y_position + self.y_size:
            y_intersect = self.y_position + self.y_size

        elif ball_center_y < self.y_position:
            y_intersect = self.y_position

        # Check for intersect based off of the given points
        # Begin by setting the distance between the closest point and center of the ball
        x_distance = ball_center_x - x_intersect
        y_distance = ball_center_y - y_intersect
        distance = (x_distance * x_distance) + (y_distance * y_distance)

        # Now check to see if the distance is less than the radius of the ball squared
        if distance < (ball_rad * ball_rad):
            return True
        else:
            return False

    # Player wants to move up
    def move_up(self):
        y_change = (-((self.game_screen.get_height()/2)/60))
        self.change_y_vel(y_change)

    # Player wants to move down
    def move_down(self):
        y_change = ((self.game_screen.get_height()/2)/60)
        self.change_y_vel(y_change)
