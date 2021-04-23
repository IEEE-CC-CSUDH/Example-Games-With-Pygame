
# Import pygame
import pygame

from pygame.locals import *

# Other Imports
import setup
import enemy


# Class definition of a Player
class Player:

    # The constructor of a Player object
    def __init__(self, speed):

        # Class fields (current object variables)
        self.positionx = setup.SCREEN_WIDTH / 2
        self.positiony = setup.SCREEN_HEIGHT / 2
        self.SPEED = speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_dead = False
        pass
    
    # Draw a white circle to represent the player
    def draw(self):
        pygame.draw.circle(setup.DISPLAY_SURF, setup.WHITE, (self.positionx, self.positiony), 10)
        pass

    # Check if a key was pressed or released
    def check_input(self, event):
        if event.type == KEYDOWN:
            self.set_speed(event)
        if event.type == KEYUP:
            self.stop(event)
        pass
    
    # Move the player
    def move(self):

        self.positionx += self.velocity_x
        self.positiony += self.velocity_y
        pass
    
    # Set the speed according to the key pressed
    def set_speed(self, event):
        if event.key == K_UP and self.velocity_y == 0:

            if self.velocity_x == 0:
                self.velocity_y = (-1 * self.SPEED)
                
            else:
                self.velocity_y = (-0.8 * self.SPEED)

        elif event.key == K_DOWN and self.velocity_y == 0:
            
            if self.velocity_x == 0:

                self.velocity_y = self.SPEED
            else:

                self.velocity_y = (0.8 * self.SPEED)

        elif event.key == K_LEFT and self.velocity_x == 0:
            
            if self.velocity_y == 0:

                self.velocity_x = -1 * self.SPEED
            else:

                self.velocity_x = (-0.8 * self.SPEED)

        elif event.key == K_RIGHT and self.velocity_x == 0:
            
            if self.velocity_y == 0:

                self.velocity_x = self.SPEED
            
            else:
                
                self.velocity_x = (0.8 * self.SPEED)
        pass

    # Halt the player when no keys are pressed
    def stop(self, event):
        if event.key == K_UP and self.velocity_y != 0:
            self.velocity_y = 0

            if abs(self.velocity_x) < self.SPEED:
                self.velocity_x *= 1.25

        elif event.key == K_DOWN and self.velocity_y != 0:
            self.velocity_y = 0

            if abs(self.velocity_x) < self.SPEED:
                self.velocity_x *= 1.25

        elif event.key == K_LEFT and self.velocity_x != 0:
            self.velocity_x = 0

            if abs(self.velocity_y) < self.SPEED:
                self.velocity_y *= 1.25


        elif event.key == K_RIGHT and self.velocity_x != 0:
            self.velocity_x = 0

            if abs(self.velocity_y) < self.SPEED:
                self.velocity_y *= 1.25
        pass

    # Check if the player collided with an enemy
    def check_collision(self, enemy):

        if (abs(self.positionx - enemy.positionx) < 2 and abs(self.positiony - enemy.positiony) < 2):
            self.kill_player()
        pass

    # Kill the player
    def kill_player(self):
        self.is_dead = True
        pass
    
    # Check if the player is dead
    def check_dead(self) -> bool:
        return self.is_dead