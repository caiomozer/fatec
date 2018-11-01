#Game rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

#Use this function when bored

import random

class goodbye(Exception): pass #this exception is raised to break the game loop and quit


#Function that start a new game or exit.
def new_game():
  new_game = input("Play again? y/n\n")
  if new_game == 'n':
    raise goodbye
    
#the game <3
def jan_ken():

#keeping score 'cus why not!?
  total_draw = 0
  score_computer = 0
  score_player = 0
  total_plays = 0
  weapon = ['rock', 'scissors', 'paper']

  try:
    while True:
      
      while True:
        player = input("Choose your weapon: {}\n".format(weapon)).lower()
        if player in weapon:
          break
      
      computer = random.choice(weapon) #the computer choice is made with pseudorandom selection
      print("Computer chooses: {}".format(computer))

      if player == computer:
        print("Its a Draw!")
        total_draw += 1
        total_plays += 1
        print("Total plays: {}\nTotal Draws: {}\nComputer Score: {}\nPlayer Score: {}\n".format(total_plays,total_draw,score_computer,score_player))
        new_game()

      if weapon.index(computer) == (weapon.index(player)+1) %3: # compare list indexes to determine the winner
        print("Player Wins the match!")
        score_player += 1
        total_plays += 1
        print("Total plays: {}\nTotal Draws: {}\nComputer Score: {}\nPlayer Score: {}\n".format(total_plays,total_draw,score_computer,score_player))
        new_game()

      if weapon.index(player) == (weapon.index(computer)+1) %3:
        print("Computer Wins the match!")
        score_computer += 1
        total_plays += 1
        print("Total plays: {}\nTotal Draws: {}\nComputer Score: {}\nPlayer Score: {}\n".format(total_plays,total_draw,score_computer,score_player))
        new_game()
  except goodbye:
    pass

jan_ken()