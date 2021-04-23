# Import pygame
import pygame

from pygame.locals import *

# Other imports of classes player and enemy
import player   # in player.py
import enemy    # in enemy.py

def setup():

    global SCREEN_WIDTH
    SCREEN_WIDTH = 500                                                      # affects the horizontal (x-axis) length
    global SCREEN_HEIGHT
    SCREEN_HEIGHT = 500                                                     # affects the vertical (y-axis) length

    global DISPLAY_SURF
    DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("The Terror of the Red Dot")

    # Create variables that store color values in RGB
    global WHITE
    WHITE = pygame.Color(255, 255, 255)
    global RED
    RED = pygame.Color(255, 0, 0)
    global BLACK
    BLACK = pygame.Color(0, 0, 0)


    # Other setup
    global is_running
    is_running = True                                                       # keeps track if the game ended
    global clock
    clock = pygame.time.Clock()                                             # allows for restricting fps (helps performance)

    # Setting up 'game over' text
    global font

    font = pygame.font.Font('freesansbold.ttf', 32)                         # Sets font

    global text
    text = font.render('Game Over', True, RED, BLACK)                       # Sets the text color and fill
    global text_rect
    text_rect = text.get_rect()                                             # Creates a text rectangle
    text_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)                # Centers the text rectangle

    # Create the game entities
    global player
    player = player.Player(3)                                               # Creates a Player object

    global enemieslist
    enemieslist = []                                                        # Creates a list (Arrays in other languages)
    enemieslist.append(enemy.Enemy(2.5))                                          # Creates an Enemy object 
                                                                            # (In a real game, there would be more than one enemy)

    global enemy_timer
    enemy_timer = 100