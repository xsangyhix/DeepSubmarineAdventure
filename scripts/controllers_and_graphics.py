import pygame
import random


def draw_stickman(screen, x, y):
    # Head
    pygame.draw.ellipse(screen,
                        pygame.Color('black'),
                        [x + 1, y, 10, 10],
                        0)

    # Legs
    pygame.draw.line(screen,
                     pygame.Color('black'),
                     [x + 5, y + 17],
                     [x + 10, y + 27],
                     2)
    pygame.draw.line(screen,
                     pygame.Color('black'),
                     [x + 5, y + 17],
                     [x, y + 27],
                     2)

    # Body
    pygame.draw.line(screen,
                     pygame.Color('red'),
                     [x + 5, y + 17],
                     [x + 5, y + 7],
                     2)

    # Arms
    pygame.draw.line(screen,
                     pygame.Color('red'),
                     [x + 5, y + 7],
                     [x + 9, y + 17],
                     2)
    pygame.draw.line(screen,
                     pygame.Color('red'),
                     [x + 5, y + 7],
                     [x + 1, y + 17],
                     2)


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

# Initializing the stickman
x_pos = 50
y_pos = 50

x_speed = 0
y_speed = 0

# ------------------ Main Program Loop -------------------
while not game_exit:
    # ---------- Main event loop
    for event in pygame.event.get():  # User action
        if event.type == pygame.QUIT:  # User clicked close
            game_exit = True  # Setting the condition to end the Main Program loop

        # Get arrow keys pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # Get key released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    # --- Game logic should go here

    # Move the stickman
    x_pos += x_speed
    y_pos += y_speed

    # --- Drawing code should go here

    # First, clear the screen to base color. Don't put other drawing commands
    # above this, or they will be erased by this command.
    game_screen.fill(pygame.Color('white'))

    # Drawing after the screen has been filled with the base color
    draw_stickman(game_screen, x_pos, y_pos)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_clock.tick(game_fps)

# --- Exiting pygame
pygame.quit()
