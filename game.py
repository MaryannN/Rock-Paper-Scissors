#coding=utf-8

##Watched Python Skills for AI Part IV live from Local Hack Day: Learn 2022
##Python rock paper scissors code from glicth - https://glitch.com/~python-rock-paper-scissors

#comments here from mlh
## my comments

import random ##built in function

winner = False
valid_moves = ["rock", "paper", "scissors"]
state = [""] # we start with an empty string in the state to prevent problems later in the workshop!
winners = []

##Added game welcome
print("πWelcome to Rock Paper Scissors!π\n Best of five wins, Good Luck!")

# π This function asks our user to enter a move!
##added \n in front
def ask_move():
  move = input("\nπ€ What move do you want to play?\n Type rock, paper or scissors!\nMove: ")
  
  # If the move isn't rock, paper or scissors, return an error
  if move not in valid_moves:
      print("That is not a valid move")
  else:
    return move
  
 
# π This function returns the most frequent move in our list
def most_common(list):
  rock_count = 0
  paper_count = 0
  scissors_count = 0

  for move in list: ## go thru everything in the list
    if move == "rock":
      rock_count += 1 # increment rock count by 1
    elif move == "paper":
      paper_count += 1
    elif move == "scissors":
      scissors_count += 1
    
  # return the most common
  if rock_count >= scissors_count and rock_count >= paper_count:
    return "rock"
  elif paper_count >= rock_count and paper_count >= scissors_count:
    return "paper"
  else:
    return "scissors"

  
# π This function sets the rules that our opponent uses to decide their move!
def make_move():
  number = len(state) % 3
  catchphrase = ["\nZoinks!", "\nBazinga!", "\nYeetus!"] ## Changed Bazinga to list
  print(catchphrase[number])  ##prints catchphrase based on move played
  ##move = valid_moves[number]  commented out
  last_move = state[-1] ##refers to last element (last move player made)
  
  if random.randint(0,1) == 0:
    """  ##commented out
    if last_move == "rock": ##plays to beat last move player made, still exploitable
        move = "paper"
      elif last_move == "paper":
        move = "scissors"
      else:
        move = "rock"
    """
  ##computer will now beat the most common state half the time  
    if most_common(state) == "rock":
      move = "paper"
    elif most_common(state) == "paper":
      move = "scissors"
    else:
      move = "rock"
  else:
    move = random.choice(valid_moves)
  return move
  
# π This function lets us check who won our game of rock paper scissors!
def check_winner(player_move, computer_move):
  if player_move == computer_move:
    return "draw"
  
  elif player_move == "rock":
    if computer_move == "scissors":
      return "player"
    else:
      return "opponent"
    
  elif player_move == "paper":
    if computer_move == "rock":
      return "player"
    else:
      return "opponent"
      
  elif player_move == "scissors":
    if computer_move == "paper":
      return "player"
    else:
      return "opponent"

# This function helps us work out who is the overall winner of the five games
# It outputs the most common element in a list
# This is a bit of slightly more advanced code than the rest of our game, so don't
# worry about understanding it!
def most_common(list):
  return max(set(list), key=list.count)


# This is our game loop!
while not winner:
  player_move = ask_move()
  computer_move = make_move()
  
  # Lets update our state!
  state.append(player_move)
  
  # Okay, lets see who won this round!
  round_winner = check_winner(player_move, computer_move)
  
  # Now we know who won, let's put a message in our console telling the player!
  ##added /n and dash separators for spacing and cleaner format
  if round_winner == "player":
    print("π Congratulations, you won!")
    print("\n------------------------------------------")
  elif round_winner == "opponent":
    print("β Oh no! You lost!")
    print("\n------------------------------------------")
  else:
    print("π You drew with your opponent! It's a tie!")
    print("\n------------------------------------------")
  
  # Next up, let's add our winner to our list of winners
  # Our game of rock, paper, scissors is a best of five game
  # This lets us keep track of who wins the best of five!
  winners.append(round_winner)
  
  # When five games have been played, output the winner then end the game
  if len(winners) == 5:
    winner = most_common(winners)
    print("π The winner of the five games was: {}".format(winner))