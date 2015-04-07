import pygame
import Game_Object



class game_text(Game_Object.Game_Object):

    def __init__(self, game_screen, score, font, score_change, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.score = score
        self.font = font
        self.score_change = score_change

    def change_score(self):
        self.score_change = 1
        self.score += self.score_change

    def reset_score(self):
        self.score = 0

    def game_object_update(self):
        if self.score == 10:
            self.reset_score()



    def game_object_draw(self):
        font = pygame.font.SysFont("Callisto", 50)
        score_text = font.render(str(self.score), True, (255, 255, 255))
        self.game_screen.blit(score_text,(self.x_position, self.y_position))


