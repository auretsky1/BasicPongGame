import pygame

class Game_Object(object):
    #Constructor
    def __init__(self, game_screen, x_position=0, y_position=0,
                 x_vel=0, y_vel=0, size=0, border_thickness=0):
        self.game_screen = game_screen
        self.x_position = x_position
        self.y_position = y_position
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.size = size
        self.border_thickness = border_thickness

    #Update the game object
    def game_object_update(self):
        pass

    #Draw the game object to the screen
    def game_object_draw(self):
        pass

    def change_x_vel(self, amount):
        self.x_vel += amount

    def change_y_vel(self, amount):
        self.y_vel += amount

    def stop_moving(self):
        self.y_vel = 0
        self.x_vel = 0


