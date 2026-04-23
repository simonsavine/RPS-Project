from RPSCode import RPS

import pygame

pygame.init()

# Change resolution to fit your monitor!
screen = pygame.display.set_mode((1100,850))
pygame.display.set_caption("Rock Paper Scissors")

paper_img = pygame.image.load('Paper.png')
rock_img = pygame.image.load('Rock.png')
scissors_img = pygame.image.load('Scissors.png')
start1_img = pygame.image.load('Start1.png')

# Re-size images as you please:
sp = pygame.transform.scale(paper_img, (300,300))
sr = pygame.transform.scale(rock_img, (300,300))
ss = pygame.transform.scale(scissors_img, (300,300))
ss1 = pygame.transform.scale(start1_img, (300,300))

# Rotated images:
ss1_rot = pygame.transform.rotate(ss1, 35)

# Flipped images:
ss1_flipped = pygame.transform.flip(ss1, True, False)
ss1_rot_flipped = pygame.transform.flip(ss1_rot, True, False)
paper_flipped = pygame.transform.flip(sp, True, False)
rock_flipped = pygame.transform.flip(sr, True, False)
scissors_flipped = pygame.transform.flip(ss, True, False)


clock = pygame.time.Clock()
delta_time = 0.1

# Make the hands move 3 times in animation
# The idea here is to switch between Start 1 and Start 2 very quickly 3 times
# Transparent to remove images from game terminal

rps = RPS()
player_ans = rps.player_input
computer_ans = rps.computer_choice


def playerChoiceAnimation():
    # Blit Player choice!
        if player_ans == 'rock':
            screen.blit(rock_flipped, (140, 250))
            pygame.display.flip()
            pygame.time.delay(300)

        elif player_ans == 'paper':
            screen.blit(paper_flipped, (140, 250))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            screen.blit(scissors_flipped, (140, 250))
            pygame.display.flip()
            pygame.time.delay(300)

def computerChoiceAnimation():
    # Blit Computer choice!

        if computer_ans == 'rock':
            screen.blit(sr, (660, 250))
            pygame.display.flip()
            pygame.time.delay(300)

        elif computer_ans == 'paper':
            screen.blit(sp, (660, 250))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            screen.blit(ss, (660, 250))
            pygame.display.flip()
            pygame.time.delay(300)

def startAnimation():
    
    for i in range(3):
        screen.fill((0,0,0))
        screen.blit(ss1, (660, 250))
        screen.blit(ss1_flipped, (140, 250))

        pygame.display.flip()
        pygame.time.delay(300)

        screen.fill((0,0,0))
        screen.blit(ss1_rot, (660, 250))

        # Problem here
        screen.blit(ss1_rot_flipped, (140, 250))

        pygame.display.flip()
        pygame.time.delay(300)
    
    screen.fill((0,0,0))
    playerChoiceAnimation()
    computerChoiceAnimation()
    
running = True
while running:

    startAnimation()

    # Input animation def here, make the hands move 3 times

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
print("Hello!!")

