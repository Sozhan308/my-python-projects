'''https://github.com/pytopia/Project-Based-Python/blob/main/Lectures/06%20Level%20I/01%20Rock%20Paper%20Scissors/README.md'''

import random


class RockPaperScissors:

  def get_computer_choice(self):
    mylist = ["rock", "paper", "scissor"]
    return random.choice(mylist)
  
  def playRound(humanChoice,computerChoice, humanScore, ComputerScore):
    if(humanChoice.casefold() == "scissor" and computerChoice.casefold() == "paper") or (humanChoice.casefold() == "paper" and computerChoice.casefold() == "rock" ) or (humanChoice.casefold() == "rock" and computerChoice.casefold() == "scissor" ):
      humanScore += 1
    elif(humanChoice.casefold() == "paper" and computerChoice.casefold() == "scissor") or (humanChoice.casefold() == "rock" and computerChoice.casefold() == "paper" ) or (humanChoice.casefold() == "scissor" and computerChoice.casefold() == "rock" ):
      ComputerScore += 1
    else:
      pass
    return humanScore, ComputerScore
      
class PlayGame(RockPaperScissors):
  
  def playGame(self,Rounds,humanSelection,computerSelection,humanScore,ComputerScore):
    for i in range(Rounds):
      RockPaperScissors.playRound(humanSelection,computerSelection, humanScore, ComputerScore)
    if(humanScore > ComputerScore):
      print("Final winner is human")
    elif(ComputerScore > humanScore):
      print("Final winner is computer")
    else:
      print("Tie")
  
def main():
  
  rockpaperscissors = RockPaperScissors()
  humanSelection = input("Enter your choice")
  computerSelection = rockpaperscissors.get_computer_choice()
  humanScore=0
  ComputerScore=0
  playGame = PlayGame()
  playGame.playGame(5,humanSelection,computerSelection,humanScore,ComputerScore)
  
  
if __name__ == "__main__":
  main()