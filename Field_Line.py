import pygame
import Game_Object


class Field(Game_Object.Game_Object):

    # Constructor
    def __init__(self, game_screen, x_size, y_size, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.x_size = x_size
        self.y_size = y_size

        self.field_line_list = []
        self.field_line_list_two = []
        self.field_line_list.append(self.y_position)

        while self.y_position in range(510):
            self.y_position += 20
            self.field_line_list_two.append(self.y_position)
            self.y_position += 20
            self.field_line_list.append(self.y_position)

    def game_object_update(self):

        pass

    def game_object_draw(self):
        for i in range(len(self.field_line_list)):
            pygame.draw.rect(self.game_screen, (255, 255, 255), [self.x_position,
                                                                 self.field_line_list[i],
                                                                 self.x_size,
                                                                 self.y_size])
        for i in range (len(self.field_line_list_two)):
            pygame.draw.rect(self.game_screen, (0, 0, 0), [self.x_position,
                                                           self.field_line_list_two[i],
                                                           self.x_size,
                                                           self.y_size])



