import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojies = {ROCK:'🧱', PAPER:'📃', SCISSORS:'✂'}
choices = tuple(emojies.keys())

def get_user_choice():
  while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ')[0].lower().strip()
    if user_choice in choices:
      return user_choice
    else:
      print('Invalid choice!')

def display_emojies(user_choice, computer_choice):
  print(f'\nYou choose {emojies[user_choice]}')
  print(f'Computer choose {emojies[computer_choice]}')

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
      print('Draw!')
  elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == PAPER and computer_choice == ROCK) or 
    (user_choice == SCISSORS and computer_choice == PAPER)):
    print('You win')
  else:
    print('You lost')

def play_game():
  while True:
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)

    display_emojies(user_choice, computer_choice)

    determine_winner(user_choice, computer_choice)

    should_continue = input('\nContinue? (y/n): ')[0].strip().lower()
    if should_continue == 'n':
      break

play_game()