import sys, pygame

def check_events(ship):
    #Respond to key andd mouse press
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #IF KEYDOWN(pressed) the which right or left which ever is pressed set it's flag to True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        #IF KEYUP(unpressed) the which right or left which ever is unpressed set it's flag to False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

       
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()