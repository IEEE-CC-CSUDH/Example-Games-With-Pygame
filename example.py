#
#
#   This example was created as a reference Python program 
#   for the IEEE CC's 2021 Game Jam
#   
#   ===================== Details =========================
#   Name: template.py
#   Description: This project is meant to serve as a basis
#                to create your own games using Pygame
#   Author: Giovanni Rivera (@grivera64)
#   Date: 04/14/2021
#
#

# Import pygame
import pygame

from pygame.locals import *

import setup

# Initialize the pygame program
pygame.init()

# Initialize the setup function (in setup.py)
setup.setup()

# main while loop for game updates while the game is running
while (setup.is_running):

    # Spawn the next enemy if 100 loops have passed by
    if setup.enemy_timer <= 0:

        setup.enemieslist.append(setup.enemy.Enemy(2.5))
        setup.enemy_timer = 100
    
    # End of if
    
    # Sets the fps that this while loop executes at
    setup.clock.tick(60)
    
    # Fills the background color to BLACK (0, 0, 0)
    setup.DISPLAY_SURF.fill((0, 0, 0))
    
    # Display player or enemy if player is not dead
    if not setup.player.check_dead():

        setup.player.draw()                                                  # Draw the player

        # Look through all of the enemies in enemieslist
        for i in range(len(setup.enemieslist)):

            setup.enemieslist[i].draw()                                      # Draw the enemies

    # Else, display the game over screen
    else:

        setup.DISPLAY_SURF.blit(setup.text, setup.text_rect)

    # End of if-else

    # Check all events that occured in this scene
    for event in pygame.event.get():
        
        # if the X button was pressed, exit loop
        if event.type == QUIT:

            setup.is_running = False
            continue
        # End if

        # Check if there was an input from the player's keyboard (Up, Down, Left, or Right)
        setup.player.check_input(event)

    # End of for

    # Don't update the player and enemy position if there is 
    if not setup.player.check_dead():

        # Moves the player
        setup.player.move()

        # Check every enemy on the enemieslist
        for i in range(len(setup.enemieslist)):

            curr_enemy = setup.enemieslist[i]
            curr_enemy.move(setup.player.positionx, setup.player.positiony)
            setup.player.check_collision(curr_enemy)

        # End of for

    # End of if

    # Update the game and screen
    pygame.display.update()

    # Change the timer to spawn the next enemy
    setup.enemy_timer -= 1

# end of while loop

# quit game
pygame.quit()

# quit python script
exit()