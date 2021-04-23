# Import pygame
import pygame

from pygame.locals import *

# Other imports for the game
import random
import setup

# Represent an Enemy that the player must avoid
class Enemy:

    # The constructor of an Enemy Object
    def __init__(self, speed):
        self.positionx = 0 + int(random.randrange(0, 2)) * setup.SCREEN_WIDTH
        self.positiony = random.randrange(0, setup.SCREEN_HEIGHT)
        self.speed = speed
        pass
    
    # Draw the enemy
    def draw(self):
        pygame.draw.circle(setup.DISPLAY_SURF, setup.RED, (self.positionx, self.positiony), 10)
        pass

    # Move the enemy accordingly to a player's x and y position
    def move(self, player_x: int, player_y: int):
        if (player_x >= self.positionx):
            self.positionx += (self.speed * 0.5) 
        else:
            self.positionx += (-0.5 * self.speed)

        if (player_y >= self.positiony):
            self.positiony += (self.speed * 0.5) 
        else:
            self.positiony += (-0.5 * self.speed)
        pass