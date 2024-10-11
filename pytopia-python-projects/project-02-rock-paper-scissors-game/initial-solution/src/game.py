'''https://github.com/pytopia/Project-Based-Python/blob/main/Lectures/06%20Level%20I/01%20Rock%20Paper%20Scissors/README.md'''

import random


class RockPaperScissors:

  def get_computer_choice(self):
    mylist = ["rock", "paper", "scissor"]
    return random.choice(mylist)
  
  def get_human_choice(self):
    return input("Enter your Choice: ")
  
  def playRound(self, humanChoice, computerChoice):
    if(humanChoice.casefold() == "scissor" and computerChoice.casefold() == "paper") or (humanChoice.casefold() == "paper" and computerChoice.casefold() == "rock" ) or (humanChoice.casefold() == "rock" and computerChoice.casefold() == "scissor" ):
      return "human"
    elif(humanChoice.casefold() == "paper" and computerChoice.casefold() == "scissor") or (humanChoice.casefold() == "rock" and computerChoice.casefold() == "paper" ) or (humanChoice.casefold() == "scissor" and computerChoice.casefold() == "rock" ):
      return "computer"
    else:
      return "tie"
      
class PlayGame(RockPaperScissors):
  
  def playGame(self,Rounds):
    humanScore = 0
    computerScore = 0
    for i in range(Rounds):
      computer_choice = self.get_computer_choice()
      human_choice = self.get_human_choice()
      print(f" Human: {human_choice} and Computer: {computer_choice}")
      result = self.playRound(human_choice,computer_choice)
      
      if(result == "human"):
        humanScore +=1
        print("human wins this round!!")
      elif(result == "computer"):
        computerScore +=1
        print("computer wins this round")
      else:
        print("this round is a tie")
        
    print(f"Final Scores => Human - {humanScore} | computer - {computerScore}")
    
    # Final Result
    
    if(humanScore > computerScore):
      print("Final winner is human")
    elif(computerScore > humanScore):
      print("Final winner is computer")
    else:
      print("Tie")
  
def main():

  playGame = PlayGame()
  playGame.playGame(5)
  
if __name__ == "__main__":
  main()