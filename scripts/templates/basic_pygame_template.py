import pygame
import random

pygame.init()

# Used to manage how fast the screen updates
game_clock = pygame.time.Clock()
game_fps = 60

# Setting screen dimensions
screen_width = 800
screen_height = 600

screen_resolution = [screen_width, screen_height]

game_screen = pygame.display.set_mode(screen_resolution)

# Creating the exit condition for the main loop
game_exit = False

# ------------------ Main Program Loop -------------------
while not game_exit:
    # ---------- Main event loop
    for event in pygame.event.get():  # User action
        if event.type == pygame.QUIT:  # User clicked close
            game_exit = True  # Setting the condition to end the Main Program loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to base color. Don't put other drawing commands
    # above this, or they will be erased by this command.
    game_screen.fill(pygame.Color('white'))

    # Drawing after the screen has been filled with the base color

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_clock.tick(game_fps)

# --- Exiting pygame
pygame.quit()
