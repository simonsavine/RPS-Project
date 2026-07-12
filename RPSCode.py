import random
import pygame
import sys
import pygame_gui

# Change resolution to fit your monitor resolution.
WIDTH, HEIGHT = 1400, 800

pygame.display.set_caption("Rock, Paper, or Scissors? Enter your choice below: ")
CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((350, 275), (900, 50), manager=MANAGER,
                                                      object_id="#main_text_entry"                       

class RPS:

  def __init__(self):
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}
    self.choices = choices
    player_input = player_input()
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

  def choice(player_decision):
    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()

        SCREEN.fill("white")

        player_choice = pygame.font.SysFont("bahnschrift", 100).render(f"") 

        pygame.display.update()
  

  def player_input():
    while True:
      RR = CLOCK.tick(60) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT():
          pygame.quit()
          sys.exit()
        
        if event.type == pygame_gui.UI_TEXT_ENTY_FINISHED and event.ui_object_id == "#main_text_entry":
          choice(event.text)

        MANAGER.process_evets(event)

      MANAGER.update(RR)

      SCREEN.fill("white")

      MANAGER.draw_ui(SCREEN)

      pygame.display.update()

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