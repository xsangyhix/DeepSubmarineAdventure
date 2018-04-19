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

# Initializing the snowflakes
snow_list = []
number_of_snowflakes = 100
snowflake_radius = 2
snowflake_speed = 2
for i in range(number_of_snowflakes):
    x = random.randrange(50, screen_width - 50)
    y = random.randrange(0, screen_height)
    snow_list.append([x, y])

# ------------------ Main Program Loop -------------------
while not game_exit:
    # ---------- Main event loop
    for event in pygame.event.get():  # User action
        if event.type == pygame.QUIT:  # User clicked close
            game_exit = True  # Setting the condition to end the Main Program loop

    # --- Game logic should go here

    # Repositioning snowflakes that are off the screen

    for snowflake in snow_list:
        if snowflake[1] > screen_height + 2 * snowflake_radius:
            snowflake[0] = random.randrange(50, screen_width - 50)
            snowflake[1] = -2 * snowflake_radius
        else:
            snowflake[1] += snowflake_speed

    # --- Drawing code should go here

    # First, clear the screen to base color. Don't put other drawing commands
    # above this, or they will be erased by this command.
    game_screen.fill(pygame.Color('black'))

    # Drawing after the screen has been filled with the base color

    # Drawing the snowflakes
    for snowflake in snow_list:
        pygame.draw.circle(game_screen,
                           pygame.Color('white'),
                           snowflake,
                           snowflake_radius)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_clock.tick(game_fps)

# --- Exiting pygame
pygame.quit()
