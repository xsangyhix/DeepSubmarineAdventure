import pygame


pygame.init()

# Used to manage how fast the screen updates
game_clock = pygame.time.Clock()
game_framerate = 60

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
    for event in pygame.event.get(): # User action
        if event.type == pygame.QUIT: # User clicked close
            game_exit = True # Setting the condition to end the Main Program loop

    # --- Game logic shoud go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased by this command.
    game_screen.fill(pygame.Color('white'))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_clock.tick(game_framerate)
