import pygame
import pygame_gui
import sys
import random

pygame.init()

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((WIDTH / 2 - 250, HEIGHT / 2 - 30), (500, 60)),
    manager=MANAGER,
    object_id="#main_text_entry"
)                 

class RPS:
  
  def choice(self, player_decision):
    if player_decision in ("rock", "paper", "scissors"):
        SCREEN.fill("white")
        CLOCK.tick(60)
        pygame.display.update()
        pygame.time.delay(500)
        return player_decision

  def player_text(self):
    running = True
    while running:
      RR = CLOCK.tick(60) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

        # Player input becomes text after pressing ENTRY key:

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
          text = event.text.lower().strip()

          result = self.choice(text)

          if result:               
             return result
          
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    exit()

        MANAGER.process_events(event)

      MANAGER.update(RR)

      SCREEN.fill("white")

      MANAGER.draw_ui(SCREEN)

      pygame.display.update()

  def __init__(self):
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}
    self.choices = choices
    player_input = self.player_text()
    self.player_input = player_input

    outcomes = {
      (1, 2) : 2,
      (1, 3) : 1,
      (2, 1) : 1,
      (2, 3) : 2,
      (3, 1) : 2,
      (3, 2) : 1
    }
    self.outcomes = outcomes

    computer_choice = random.choice(['rock','paper','scissors'])
    self.computer_choice = computer_choice

    player_input_num = choices[self.player_input]
    self.player_input_num = player_input_num

    computer_choice_num = choices[self.computer_choice]
    self.computer_choice_num = computer_choice_num

    # Maps to 1, Player wins, maps to 2, Computer wins.
  

  def playerChoice(self):
    return self.player_input

  def computerChoice(self):
    return self.computer_choice

  def mapping(self):
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}

    player_input_num = choices[self.player_input]
    computer_choice_num = choices[self.computer_choice]

    # Maps to 1, Player wins, maps to 2, Computer wins.
    outcomes = {
      (1, 2) : 2,
      (1, 3) : 1,
      (2, 1) : 1,
      (2, 3) : 2,
      (3, 1) : 2,
      (3, 2) : 1
    }

  def draw(self):
    # Case of a draw
      if self.player_input_num == self.computer_choice_num:
        print("It's a draw!")
        return

  def player_win(self):
    # Player wins!
    if self.outcomes[self.player_input_num, self.computer_choice_num] == 1:
      print(self.player_input, "beats", self.computer_choice, "and Player wins!")

  def computer_win(self):
    # Computer wins!
    if self.outcomes[self.player_input_num, self.computer_choice_num] == 2:
      print(self.computer_choice, "beats", self.player_input, "and Computer wins!")


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

delta_time = 0.1

# Make the hands move 3 times in animation
# The idea here is to switch between Start 1 and Start 2 very quickly 3 times
# Transparent to remove images from game terminal

PLAYER_HORIZONTAL, PLAYER_VERTICAL = WIDTH / 6, HEIGHT / 3
COMPUTER_HORIZONTAL, COMPUTER_VERTICAL = WIDTH - WIDTH / 6 - SPRITE_WIDTH, HEIGHT / 3

def playerChoiceAnimation():
    # Blit Player choice!

        if player_ans == 'rock':
            SCREEN.blit(rock_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        elif player_ans == 'paper':
            SCREEN.blit(paper_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            SCREEN.blit(scissors_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

def computerChoiceAnimation():
    # Blit Computer choice!

        # The SCREEN blit shouldn't be fixed to (660, 250)!!

        if computer_ans == 'rock':
            SCREEN.blit(sr, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        elif computer_ans == 'paper':
            SCREEN.blit(sp, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

        else:
            SCREEN.blit(ss, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
            pygame.display.flip()
            pygame.time.delay(300)

def startAnimation():
    
    for i in range(3):
        SCREEN.fill("white")
        SCREEN.blit(ss1, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))
        SCREEN.blit(ss1_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))

        pygame.display.flip()
        pygame.time.delay(300)

        SCREEN.fill("white")
        SCREEN.blit(ss1_rot, (COMPUTER_HORIZONTAL, COMPUTER_VERTICAL))

        SCREEN.blit(ss1_rot_flipped, (PLAYER_HORIZONTAL, PLAYER_VERTICAL))

        pygame.display.flip()
        pygame.time.delay(300)
    
    SCREEN.fill("white")
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
            else:
               return

running = True
while running:
    
    rps = RPS()
    player_ans = rps.player_input
    computer_ans = rps.computer_choice

    TEXT_INPUT.set_text('') 

    SCREEN.fill("white")
    startAnimation()

    pygame.time.delay(2000)
    
    waitForInput()

