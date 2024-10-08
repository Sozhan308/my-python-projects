''' 
Details of the project : https://github.com/pytopia/Project-Based-Python/blob/main/Lectures/04%20Your%20First%20Python%20Project/01%20Project%20-%20Number%20Guesser%20Game.ipynb

'''

import random

def generate_random_number():
  '''
  Generates random numbers between 1 and 100
  '''
  num = int(random.randrange(1,100))
  return num


def implement_scoring_system():
  ''' Calculate score for guessing the number with hints'''
  score = 100
  num = generate_random_number()
  print(""" 
  Let's start the game, 
  kindly guess the number
  """)
  guessed_number = int(input("Guess the number #1:"))
  while(num != guessed_number):
    score = score - 1
    print("Here is a Hint for you to guess the number correctly")
    if(num > guessed_number):
      print(f"The number is greater than the {guessed_number}")
    else:
      print(f"The number is lesser than the {guessed_number}")   
    print("Try to guess now")
    guessed_number = int(input("Guess the number again:"))
  return score
  
def main():
  score = implement_scoring_system()
  print("Finally, you got the correct guess. Your Score: ", score)

if __name__=="__main__":
  main()
    
