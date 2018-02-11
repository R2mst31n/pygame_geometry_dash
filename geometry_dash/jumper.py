"""

From:
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py

"""

import pygame
from all_values import *
from all_classes import * 
# Global constants

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(white)
        
        self.mask=pygame.mask.from_surface(self.image)
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None


    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        for block in self.level.platform_list:
            if(pygame.sprite.collide_mask(self, block)!=None):        
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        for block in self.level.platform_list:
            if(pygame.sprite.collide_mask(self, block)!=None):

                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom

                # Stop our vertical movement
                self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= size[1] - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = size[1] - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        
        for block in self.level.platform_list:
            if(pygame.sprite.collide_mask(self, block)!=None or self.rect.bottom >= size[1]):
                self.change_y= -10
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        #if len(platform_hit_list) > 0 or self.rect.bottom >= size[1]:
         #   self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

class Levels(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game.
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(BLUE)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


# Create platforms for the level
class Init_Level(Levels):
    """ Definition for level 1. """

    def __init__(self, player,grd):
        """ Create level  """

        # Call the parent constructor
        Levels.__init__(self, player)
        # Array with width, height, x, and y of platform
        count_x=len(grd)
        width=size[0]//count_x
        height=size[1]//10
        now_x=0
        for column in range(count_x):
            grd[column].reverse()
            for row in range(len(grd[column])):
                colour=black
                if (grd[column][row]=='1'):
                    block_img=Character(width,height,now_x,
                                        size[1]-height*(row+1),"block.png",white)
                    print("height is: ",size[1]-height*(row+1),"\n")
                    block_img.player=self.player
                    self.platform_list.add(block_img)
                    
                elif(grd[column][row]=='2'):
                     trian_img=Character(width,height,now_x,
                                         size[1]-height*(row+1),"triangle.png",white)
                     trian.img.player=self.player
                     self.platform_list.add(trian_img)
            now_x +=width
def play_game(screen,lvl_number):
    """ Main Program """
    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append( Init_Level(player,Level().get_level(lvl_number)) )

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = size[1] - player.rect.height
    active_sprite_list.add(player)

    done = False
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                return 10

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > size[0]:
            player.rect.right = size[0]

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)

        pygame.display.flip()

    #pygame.quit()





