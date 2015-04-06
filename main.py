import pygame
import Game_Handler


#Constants
screen_size = (600, 600)
screen_flags = 0
screen_depth = 0


#Color constants
screen_clear_color = (0, 0, 0)

#Variables
is_game_running = True

#Initialize pygame
pygame.init()

#Setup the program window
pygame.display.set_caption("Pong Game")

#Initialize the screen
game_screen = pygame.display.set_mode(screen_size, screen_flags, screen_depth)
game_handler = Game_Handler.Game_Handler(game_screen)

#Create the game clock
game_clock = pygame.time.Clock()

#Main game loop
while is_game_running:
    #Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_handler.process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game_handler.process_event(event)
            if event.key == pygame.K_DOWN:
                game_handler.process_event(event)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                game_handler.process_event(event)
            if event.key == pygame.K_DOWN:
                game_handler.process_event(event)

    #Do game logic
    game_handler.game_logic()

    #Clear the screen
    game_screen.fill(screen_clear_color)

    #Draw game objects
    game_handler.draw_game_objects()


    #Draw the screen
    pygame.display.flip()

    #Frame-rate
    game_clock.tick(60)