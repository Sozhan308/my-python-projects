'''Problem: https://github.com/pytopia/Project-Based-Python/tree/main/Lectures/06%20Level%20I/02%20Password%20Generator'''

from abc import ABC, abstractmethod
import random
import string
import nltk
from nltk.corpus import words
from random import sample

class PasswordGenerator(ABC):
  '''Abstract class for Password generation'''
  
  @abstractmethod
  def passwordGenerator(self, *args, **kwargs):
    self.type=type
  
class RandomPasswordGenerator(PasswordGenerator):
  
  def passwordGenerator(self, length):
    combine_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(combine_characters, k=length))
    return password
  

class MemorablePasswordGenerator(PasswordGenerator):
  
  def passwordGenerator(self, num_of_words, seperator):
    nltk.download('words')
    word_list = words.words()
    memorable_passowrd = f'{seperator}'.join(sample(word_list,k=num_of_words))
    return memorable_passowrd
  
class PinCodeGenerator(PasswordGenerator):
  
  def passwordGenerator(self, length):
    pin_code = ''.join(random.choices(string.digits, k=length))
    return pin_code
    
    
def main():
  # PG = PinCodeGenerator()
  # PG = MemorablePasswordGenerator()
  PG = RandomPasswordGenerator()
  print(PG.passwordGenerator(10))
  
if __name__ == "__main__":
  main()