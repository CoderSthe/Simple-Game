import pygame
import random

pygame.init() 

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.image.load("image.png")
monster1 = pygame.image.load("monster1.png")
monster2 = pygame.image.load("monster2.png")
monster3 = pygame.image.load("monster3.png")
prize = pygame.image.load("prize.png")

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


while 1:

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(monster1, (monster1XPosition, monster1YPosition))
    screen.blit(monster2, (monster2XPosition, monster2YPosition))
    screen.blit(monster3, (monster3XPosition, monster3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
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
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:

        playerXPosition -= 1

    if keyRight == True:

        playerXPosition += 1
    
    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    
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
        print("You lose!")
        
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    if (monster1XPosition < 0 - monster1_width) and (monster2XPosition < 0 - monster2_width) and (monster3XPosition < 0 - monster3_width) or playerBox.colliderect(prizeBox):
        print("You win!")
        
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemy approach the player.
    monster1XPosition -= 0.30
    monster2XPosition -= 0.30
    monster3XPosition -= 0.30
    prizeXPosition -= 0.30
