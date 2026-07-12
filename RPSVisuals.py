from RPSCode import RPS
import pygame
import sys
import pygame_gui

pygame.init()

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Rock Paper Scissors")

paper_img = pygame.image.load('images/Paper.png')
rock_img = pygame.image.load('images/Rock.png')
scissors_img = pygame.image.load('images/Scissors.png')
start1_img = pygame.image.load('images/Start1.png')

# Re-size images as you please:
SPRITE_WIDTH, SPRITE_HEIGHT = 300, 300

sp = pygame.transform.scale(paper_img, (SPRITE_WIDTH,SPRITE_HEIGHT))
sr = pygame.transform.scale(rock_img, (SPRITE_WIDTH,SPRITE_HEIGHT))
ss = pygame.transform.scale(scissors_img, (SPRITE_WIDTH,SPRITE_HEIGHT))
ss1 = pygame.transform.scale(start1_img, (SPRITE_WIDTH,SPRITE_HEIGHT))

# Rotated images:
ss1_rot = pygame.transform.rotate(ss1, 35)

# Flipped images:
ss1_flipped = pygame.transform.flip(ss1, True, False)
ss1_rot_flipped = pygame.transform.flip(ss1_rot, True, False)
paper_flipped = pygame.transform.flip(sp, True, False)
rock_flipped = pygame.transform.flip(sr, True, False)
scissors_flipped = pygame.transform.flip(ss, True, False)


clock = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

delta_time = 0.1

# Make the hands move 3 times in animation
# The idea here is to switch between Start 1 and Start 2 very quickly 3 times
# Transparent to remove images from game terminal

rps = RPS()
player_ans = rps.player_input
computer_ans = rps.computer_choice


PLAYER_HORIZONTAL, PLAYER_VERTICAL = WIDTH / 6, HEIGHT / 3
COMPUTER_HORIZONTAL, COMPUTER_VERTICAL = WIDTH - WIDTH / 6 - SPRITE_WIDTH, HEIGHT / 3

def playerChoiceAnimation():
    # Blit Player choice!

        if player_ans == 'rock':
            screen.blit(rock_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        elif player_ans == 'paper':
            screen.blit(paper_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            screen.blit(scissors_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

def computerChoiceAnimation():
    # Blit Computer choice!

        # The screen blit shouldn't be fixed to (660, 250)!!

        if computer_ans == 'rock':
            screen.blit(sr, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        elif computer_ans == 'paper':
            screen.blit(sp, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            screen.blit(ss, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

def startAnimation():
    
    for i in range(3):
        screen.fill("white")
        screen.blit(ss1, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
        screen.blit(ss1_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))

        pygame.display.flip()
        pygame.time.delay(300)

        screen.fill("white")
        screen.blit(ss1_rot, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))

        screen.blit(ss1_rot_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))

        pygame.display.flip()
        pygame.time.delay(300)
    
    screen.fill("white")
    playerChoiceAnimation()
    computerChoiceAnimation()

def waitForInput():
     running = True

     while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()

running = True
while running:

    startAnimation()

    waitForInput()
    

    # Let the player have a good look at the outcome
    # Only exit when player is ready and presses ESC

