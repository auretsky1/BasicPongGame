import pygame
import Game_Object


class Game_Text(Game_Object.Game_Object):

    # Constructor
    def __init__(self, game_screen, score, font, *args):
        Game_Object.Game_Object.__init__(self, game_screen, *args)
        self.score = score
        self.font = font
        self.score_change = 1

    # Change the score by the preset score_change value
    def change_score(self):
        self.score += self.score_change

    # Reset the score to zero
    def reset_score(self):
        self.score = 0

    # Update the game score object
    def game_object_update(self):
        if self.score == 10:
            self.reset_score()

    # Draw the game score to the screen
    def game_object_draw(self):
        font = pygame.font.SysFont("Callisto", 50)
        score_text = font.render(str(self.score), True, (255, 255, 255))
        self.game_screen.blit(score_text, (self.x_position, self.y_position))


