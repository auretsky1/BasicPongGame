import pygame
import random
import math
import Game_Object
import Game_Text

class Ball(Game_Object.Game_Object):

    # Constructor
    def __init__(self, game_screen, x_size, y_size, speed=5, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size
        self.speed = speed

        # The following variables hold the x/y position during a collision detection
        self.x_col_point = 0
        self.y_col_point = 0
        self.paddle_x_col_point = 0
        self.paddle_y_col_point = 0

        # An initial speed variable that is used for resetting the speed when the ball is reset
        self.initial_speed = speed

        # Initial angle of movement
        self.direction_angle = 0

        # Flag to be used for collision checking special cases
        self.special_collision = False

        # Maximum speed that the ball should move
        self.max_speed = 12

    # Update the ball object
    def game_object_update(self, paddle_one, paddle_two, game_score, ai_game_score):
        # Adjust the position of the ball by the x_vel & y_vel
        self.y_position += self.y_vel
        self.x_position += self.x_vel

        # Check to make sure the ball hasn't collided with the
        # edges of the screen, either top or bottom.
        if self.y_position + self.y_size >= self.game_screen.get_height() or self.y_position <= 0:
            self.y_vel *= -1

        # Check to make sure the ball hasn't collided with the
        # left or right side of the screen, and if it did reset it's position. Updates game score
        if self.x_position + self.x_size >= self.game_screen.get_width():
            self.reset_ball()
            Game_Text.Game_Text.change_score(game_score)

        if self.x_position <= 0:
            self.reset_ball()
            Game_Text.Game_Text.change_score(ai_game_score)

        # Process collision checks for each of the two paddles
        for paddle in (paddle_one, paddle_two):
            # Check for collision with paddle
            has_collided = self.ball_paddle_intersect_check(paddle)

            # If collision reverse track of ball until not a collision
            if has_collided:
                # Before retracting upon the velocity set the collision point
                self.x_col_point = self.x_position
                self.y_col_point = self.y_position
                self.paddle_x_col_point = paddle.x_position
                self.paddle_y_col_point = paddle.y_position

                # Perform regular collision handling if intersection occurred and paddle didn't move into ball
                while has_collided:
                    self.x_position -= self.x_vel
                    self.y_position -= self.y_vel
                    if paddle.y_vel != 0:
                        paddle.x_position -= paddle.x_vel
                        paddle.y_position -= paddle.y_vel
                    has_collided = self.ball_paddle_intersect_check(paddle)

                # Create a flag that determines if the ball is above/below the paddle
                if not (self.y_position > paddle.y_position and (self.y_position + self.y_size) < paddle.y_position + paddle.y_size):
                    self.special_collision = True
                if not ((self.y_vel < 0 and paddle.y_vel < 0) or (self.y_vel > 0 and paddle.y_vel > 0)):
                    self.special_collision = False

                # If special collision (paddle moving into ball) process accordingly
                if self.special_collision:
                    self.ball_paddle_collision_handler_moving(paddle)

                # Else process normally
                else:
                    # Now check which side of the paddle the ball is on and handle accordingly
                    self.ball_paddle_collision_handler(paddle)

                # Either way set the flag back to false
                self.special_collision = False

    # Handles velocity changes for various ball/paddle collisions
    def ball_paddle_collision_handler(self, current_paddle):
        # Variables that hold the changes in velocity as a percent based on where the player hit the paddle
        half_paddle_size = current_paddle.y_size / 2  # This holds half the size of the paddle
        paddle_center_location = (current_paddle.y_position + (current_paddle.y_size / 2))  # Where the center of the paddle is
        ball_center_location = (self.y_position + (self.y_size / 2)) # Where the center of the ball is
        center_y_distance = abs(paddle_center_location - ball_center_location) # The distance from the center of the ball to paddle
        velocity_change_ratio = (center_y_distance / half_paddle_size) # The ratio of distance to center and size of the paddle

        # Check to see if ball is on the left of the paddle
        if self.x_position <= current_paddle.x_position:
            self.speed += abs(velocity_change_ratio * current_paddle.y_vel * 0.2)  # Increase speed in portion to paddle
            self.direction_angle = self.calculate_reflection_angle(0, self.get_current_angle())
            self.set_velocity(self.direction_angle)

        # Check to see if ball is on the right of the paddle
        elif self.x_position >= (current_paddle.x_position + current_paddle.x_size):
            self.speed += abs(velocity_change_ratio * current_paddle.y_vel * 0.2)  # Increase speed in portion to paddle
            self.direction_angle = self.calculate_reflection_angle(0, self.get_current_angle())
            self.set_velocity(self.direction_angle)

        # Check to see if ball is above the top of the paddle
        if self.y_position <= current_paddle.y_position:
            #self.speed += abs(velocity_change_ratio * current_paddle.y_vel * 0.02)  # Increase speed in portion to paddle
            self.direction_angle = self.calculate_reflection_angle(1, self.get_current_angle())
            self.set_velocity(self.direction_angle)

        # Check to see if ball is below the bottom of the paddle
        elif self.y_position >= (current_paddle.y_position + current_paddle.y_size):
            #self.speed += abs(velocity_change_ratio * current_paddle.y_vel * 0.02)  # Increase speed in portion to paddle
            self.direction_angle = self.calculate_reflection_angle(1, self.get_current_angle())
            self.set_velocity(self.direction_angle)

    # Handles velocity changes for various ball/paddle collisions
    def ball_paddle_collision_handler_moving(self, current_paddle):
        # Variable that will determine if there is currently a collision
        has_collided = True

        # Reverse the travel along the velocity line of the ball
        while self.x_position != self.x_col_point:
                    self.x_position += self.x_vel
                    self.y_position += self.y_vel
                    current_paddle.x_position += current_paddle.x_vel
                    current_paddle.y_position += current_paddle.y_vel

        # Travel along the velocity line of the ball until there is no collision
        while has_collided:
                    self.x_position += self.x_vel
                    self.y_position += self.y_vel
                    has_collided = self.ball_paddle_intersect_check(current_paddle)

        # Check to see if ball is above the top of the paddle
        if self.y_position <= current_paddle.y_position:
            self.y_vel *= -1  # Paddle did not move into ball, process normally

        # Check to see if ball is below the bottom of the paddle
        elif self.y_position >= (current_paddle.y_position + current_paddle.y_size):
            self.y_vel *= -1

    # Checks to see if the ball and paddle have intersected
    def ball_paddle_intersect_check(self, current_paddle):
        # Variables holding the relevant points in the ball to be checked against
        ball_rad = self.x_size / 2
        ball_center_x = self.x_position + (self.x_size / 2)
        ball_center_y = self.y_position + (self.y_size / 2)
        x_intersect = ball_center_x
        y_intersect = ball_center_y

        # Check each vertex of the paddle to see if it's closest to the ball's center
        if ball_center_x < current_paddle.x_position:
            x_intersect = current_paddle.x_position

        elif ball_center_x > (current_paddle.x_position + current_paddle.x_size):
            x_intersect = current_paddle.x_position + current_paddle.x_size

        if ball_center_y > current_paddle.y_position + current_paddle.y_size:
            y_intersect = current_paddle.y_position + current_paddle.y_size

        elif ball_center_y < current_paddle.y_position:
            y_intersect = current_paddle.y_position

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

    # Resets the ball to the center of the screen
    def reset_ball(self):
        self.stop_moving()
        self.x_position = ((self.game_screen.get_width()/2)-5)
        self.y_position = ((self.game_screen.get_height()/2)-5)

    # Initialize the velocity of the ball after it has been reset (can also be used while moving)
    def init_velocity(self):
        # Reset the initial speed
        self.speed = self.initial_speed

        # Seed the random number generator and produce a random number equal to the angle the ball will travel
        random.seed()
        possible_angles = (45, 135, 225, 315)
        random_angle = random.randint(0, 3)
        self.direction_angle = math.radians(possible_angles[random_angle])

        # Set the velocity in proportion of the angle using Pythagorean Theorem
        self.y_vel = self.speed * math.sin(self.direction_angle)
        self.x_vel = self.speed * math.cos(self.direction_angle)

    # Hard set the velocity for when the paddle collides into the ball (angle expressed as degrees)
    def set_velocity(self, angle):
        # Before setting the new velocity, make sure that the speed has not gone beyond the maximum speed
        if (self.speed > self.max_speed):
            self.speed = self.max_speed

        self.y_vel = self.speed * math.sin(angle)
        self.x_vel = self.speed * math.cos(angle)

    # Calculate the angle of reflection when the ball hits the paddle
    def calculate_reflection_angle(self, side_or_tb, current_angle):
        # Set the current_angle to be in degrees
        current_angle = math.degrees(current_angle)

        # Peform reflection angle calculation based off of where the paddle was struck
        if side_or_tb == 0:  # The left/right side was hit
            # Angle in quadrant 2 or 4 (quadrant 1 or 3 of math modules unit circle)
            if (current_angle > 0 and current_angle < 90) or (current_angle > 180 and current_angle < 270):
                new_angle_in_degrees = current_angle + (180 - (((current_angle % 180) % 90) * 2))
            # Angle in quadrant 1 or 3 (quadrant 2 or 4 of math modules unit circle)
            elif (current_angle > 90 and current_angle < 180) or (current_angle > 270 and current_angle < 360):
                new_angle_in_degrees = current_angle - (180 - (((current_angle % 180) % 90) * 2))
        elif side_or_tb == 1:  # The top/bottom was hit
            # Angle in quadrant 2 or 4 (quadrant 1 or 3 of math modules unit circle)
            if (current_angle > 0 and current_angle < 90) or (current_angle > 180 and current_angle < 270):
                new_angle_in_degrees = current_angle - (180 - (((current_angle % 180) % 90) * 2))
            # Angle in quadrant 1 or 3 (quadrant 2 or 4 of math modules unit circle)
            elif (current_angle > 90 and current_angle < 180) or (current_angle > 270 and current_angle < 360):
                new_angle_in_degrees = current_angle + (180 - (((current_angle % 180) % 90) * 2))

        # Return the reflection angle in degrees
        return math.radians(new_angle_in_degrees)

    # Change the current angle based off of the point at which the ball collides with the paddle
    def calculate_english_angle(self, current_angle, change_ratio):
        # Set the current_angle to be in degrees
        current_angle = math.degrees(current_angle)

        # Calculate the inverse of the current angle
        current_angle = (current_angle - 180)
        if current_angle < 0:
            current_angle += 360  # If the degrees are negative, add 360 degrees to get positive value
        if current_angle > 360:
            current_angle -= 360  # If the degrees are above 360, subtract 360 degrees to get positive value

        # The angle as it should be passed in to self.calculate_reflect
        angle_change = (2 * ((current_angle % 180) % 90))

        # Perform reflection angle calculation based off of where the paddle was struck
        # Angle in quadrant 2 or 4 (quadrant 1 or 3 of math modules unit circle)
        if (current_angle > 0 and current_angle < 90) or (current_angle > 180 and current_angle < 270):
            # Calculate the angle_with_change for collisions in this quadrant
            angle_with_change = (current_angle + angle_change)
            if angle_with_change < 0:  # If the angle_change is less than 0 and 360 degrees to get positive value
                angle_with_change += 360
            if angle_with_change > 360:
                angle_with_change -= 360  # If the degrees are above 360, subtract 360 degrees to get positive value

            # Set the new angle based off the angle_with_change
            new_angle_in_degrees = change_ratio * (angle_with_change)

        # Angle in quadrant 1 or 3 (quadrant 2 or 4 of math modules unit circle)
        elif (current_angle > 90 and current_angle < 180) or (current_angle > 270 and current_angle < 360):
            # Calculate the angle_with_change for collisions in this quadrant
            angle_with_change = (current_angle - angle_change)
            if angle_with_change < 0:  # If the angle_change is less than 0 and 360 degrees to get positive value
                angle_with_change += 360
            if angle_with_change > 360:
                angle_with_change -= 360  # If the degrees are above 360, subtract 360 degrees to get positive value

            # Set the new angle based off the angle_with_change
            new_angle_in_degrees = change_ratio * angle_with_change

        # Return the reflection angle in degrees
        return math.radians(new_angle_in_degrees)

    # Get the current angle of travel based off the x_vel and y_vel
    def get_current_angle(self):
        # The number of quadrant (90 degrees) that must be added to get an accurate angle
        quadrant = 0

        # Determine the cartesian quadrant (expressed for a computer screen) in which the ball travels through
        if self.x_vel > 0 and self.y_vel > 0: # Quadrant 1
            quadrant = 0
        elif self.x_vel < 0 and self.y_vel > 0: # Quadrant 2
            quadrant = 1
        elif self.x_vel < 0 and self.y_vel < 0: # Quadrant 3
            quadrant = 2
        elif self.x_vel > 0 and self.y_vel < 0: # Quadrant 4
            quadrant = 3

        # Set the angle in radians based off of tan(angle) = y/x and add in 90 degrees for each quadrant
        angle_from_right_triangle = math.atan(abs((self.y_vel / self.speed) / (self.x_vel / self.speed)))
        angle_in_radians = angle_from_right_triangle + math.radians(quadrant * 90)
        return angle_in_radians

    # Draw the ball object to the screen
    def game_object_draw(self):
        pygame.draw.ellipse(self.game_screen, (0, 0, 255), [self.x_position,
                                                            self.y_position,
                                                            self.x_size,
                                                            self.y_size])
