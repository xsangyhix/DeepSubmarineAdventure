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

# Initializing the rectangle
rect_x = 50
rect_y = 50
rect_size_x = 50
rect_size_y = 50
pygame.draw.rect(game_screen, pygame.Color('white'), [rect_x, rect_y, 50, 50])

# Speed and direction of the rectangle
rect_speed_x = 3
rect_speed_y = 3
rect_speed = [rect_speed_x, rect_speed_y]

# ------------------ Main Program Loop -------------------
while not game_exit:
    # ---------- Main event loop
    for event in pygame.event.get():  # User action
        if event.type == pygame.QUIT:  # User clicked close
            game_exit = True  # Setting the condition to end the Main Program loop

    # --- Game logic should go here

    # Bouncing the rectangle by flipping the speed vector
    if rect_x <= 0:
        rect_speed[0] = abs(rect_speed[0])
    if rect_x >= screen_width - rect_size_x:
        rect_speed[0] = -1 * abs(rect_speed[0])

    if rect_y <= 0:
        rect_speed[1] = abs(rect_speed[1])
    if rect_y >= screen_height - rect_size_y:
        rect_speed[1] = -1 * abs(rect_speed[1])

    # --- Drawing code should go here

    # First, clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased by this command.
    game_screen.fill(pygame.Color('black'))

    # Drawing after the screen has been filled with black
    pygame.draw.rect(game_screen, pygame.Color('white'), [rect_x,
                                                          rect_y,
                                                          rect_size_x,
                                                          rect_size_y
                                                          ])

    pygame.draw.rect(game_screen, pygame.Color('red'), [rect_x + 10,
                                                        rect_y + 10,
                                                        rect_size_x - 20,
                                                        rect_size_y - 20
                                                        ])
    rect_x += rect_speed[0]
    rect_y += rect_speed[1]

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    game_clock.tick(game_framerate)

# --- Exiting pygame
pygame.quit()
