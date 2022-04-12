# In this game, the user must navigate using the arrow keys to avoid colliding with
# the various monsters.
# The user must collide with the trophy to win the game.
# Should the user collide with any of the monsters or fail to collide with the trophy
# the game will quit and they would've lost the game.


# import pygame and random to generate random numbers

import pygame
import random

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

# This creates the player and gives it the image found in this folder (same as the monster and prize images). 

player = pygame.image.load("image.png")
monster1 = pygame.image.load("monster1.png")
monster2 = pygame.image.load("monster2.png")
monster3 = pygame.image.load("monster3.png")
prize = pygame.image.load("prize.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

player_height = player.get_height()
player_width = player.get_width()
monster1_height = monster1.get_height()
monster1_width = monster1.get_width()
monster2_height = monster2.get_height()
monster2_width = monster2.get_width()
monster3_height = monster3.get_height()
monster3_width = monster3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

monster1XPosition =  screen_width + 150
monster1YPosition =  random.randint(0, screen_height - monster1_height)
monster2XPosition = screen_width + 300
monster2YPosition = random.randint(0, screen_height - monster2_height)
monster3XPosition = screen_width + 550
monster3YPosition = random.randint(0, monster3_height)

# Make the trophy start off screen and at a random Y position

prizeXPosition = screen_width + 600
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the arrow keys are pressed.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(monster1, (monster1XPosition, monster1YPosition))
    screen.blit(monster2, (monster2XPosition, monster2YPosition))
    screen.blit(monster3, (monster3XPosition, monster3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        # this moves the player to the left

        playerXPosition -= 1

    if keyRight == True:
        # this moves the player to the right

        playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the monster1:
    
    monster1Box = pygame.Rect(monster1.get_rect())
    monster1Box.top = monster1YPosition
    monster1Box.left = monster1XPosition

    # Bounding box for the monster2:
    
    monster2Box = pygame.Rect(monster2.get_rect())
    monster2Box.top = monster2YPosition
    monster2Box.left = monster2XPosition

    # Bounding box for the monster3:
    
    monster3Box = pygame.Rect(monster3.get_rect())
    monster3Box.top = monster3YPosition
    monster3Box.left = monster3XPosition

    # Bounding box for prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(monster1Box) or playerBox.colliderect(monster2Box) or playerBox.colliderect(monster3Box) or (prizeXPosition < 0 - prize_width):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quit game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    
    if (monster1XPosition < 0 - monster1_width) and (monster2XPosition < 0 - monster2_width) and (monster3XPosition < 0 - monster3_width) or playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quit game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player.
    
    monster1XPosition -= 0.30
    monster2XPosition -= 0.30
    monster3XPosition -= 0.30
    prizeXPosition -= 0.30