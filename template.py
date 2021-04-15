#
#
#   This template was created as a reference Python program 
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

# Other imports for the game
import random 


# Initialize the pygame program
pygame.init()

# Create a window (in pygame, this is called a Surface Object)

SCREEN_WIDTH = 500                                                      # affects the horizontal (x-axis) length
SCREEN_HEIGHT = 500                                                     # affects the vertical (y-axis) length

DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("The Terror of the Red Dot")

# Create variables that store color values in RGB
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)

# Represent an Enemy that the player must avoid
class Enemy:

    # The constructor of an Enemy Object
    def __init__(self, speed):
        self.positionx = 0 + int(random.randrange(0, 2)) * SCREEN_WIDTH
        self.positiony = random.randrange(0, SCREEN_HEIGHT)
        self.speed = speed
        pass
    
    # Draw the enemy
    def draw(self):
        pygame.draw.circle(DISPLAY_SURF, RED, (self.positionx, self.positiony), 10)
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

# Class definition of a Player
class Player:

    # The constructor of a Player object
    def __init__(self, speed):

        # Class fields (current object variables)
        self.positionx = SCREEN_WIDTH / 2
        self.positiony = SCREEN_HEIGHT / 2
        self.SPEED = speed
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_dead = False
        pass
    
    # Draw a white circle to represent the player
    def draw(self):
        pygame.draw.circle(DISPLAY_SURF, WHITE, (self.positionx, self.positiony), 10)
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
    def check_collision(self, enemy: Enemy):

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


# Other setup
is_running = True                                                       # keeps track if the game ended
clock = pygame.time.Clock()                                             # allows for restricting fps (helps performance)


# Setting up 'game over' text
font = pygame.font.Font('freesansbold.ttf', 32)                         # Sets font
text = font.render('Game Over', True, RED, BLACK)                       # Sets the text color and fill
text_rect = text.get_rect()                                             # Creates a text rectangle
text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)                # Centers the text rectangle

# Create the game entities
player = Player(3)                                                      # Creates a Player object

enemieslist = []                                                        # Creates a list (Arrays in other languages)
enemieslist.append(Enemy(2.5))                                          # Creates an Enemy object 
                                                                        # (In a real game, there would be more than one enemy)

enemy_timer = 100

# main while loop for game updates while the game is running
while (is_running):

    # Spawn the next enemy if 100 loops have passed by
    if enemy_timer <= 0:

        enemieslist.append(Enemy(2.5))
        enemy_timer = 100
    
    # End of if
    
    # Sets the fps that this while loop executes at
    clock.tick(60)
    
    # Fills the background color to BLACK (0, 0, 0)
    DISPLAY_SURF.fill((0, 0, 0))
    
    # Display player or enemy if player is not dead
    if not player.check_dead():

        player.draw()                                                  # Draw the player

        # Look through all of the enemies in enemieslist
        for i in range(len(enemieslist)):

            enemieslist.__getitem__(i).draw()                          # Draw the enemies

    # Else, display the game over screen
    else:

        DISPLAY_SURF.blit(text, text_rect)

    # End of if-else

    # Check all events that occured in this scene
    for event in pygame.event.get():
        
        # if the X button was pressed, exit loop
        if event.type == QUIT:

            is_running = False
            continue
        # End if

        # Check if there was an input from the player's keyboard (Up, Down, Left, or Right)
        player.check_input(event)

    # End of for

    # Don't update the player and enemy position if there is 
    if not player.check_dead():

        # Moves the player
        player.move()

        # Check every enemy on the enemieslist
        for i in range(len(enemieslist)):

            curr_enemy = enemieslist[i]
            curr_enemy.move(player.positionx, player.positiony)
            player.check_collision(curr_enemy)

        # End of for

    # End of if

    # Update the game and screen
    pygame.display.update()

    # Change the timer to spawn the next enemy
    enemy_timer -= 1

# end of while loop

# quit game
pygame.quit()

# quit python script
exit()