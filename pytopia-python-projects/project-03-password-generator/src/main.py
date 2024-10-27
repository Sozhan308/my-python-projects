'''Problem: https://github.com/pytopia/Project-Based-Python/tree/main/Lectures/06%20Level%20I/02%20Password%20Generator'''

from abc import ABC, abstractmethod
import random
import string

class PasswordGenerator(ABC):
  '''Abstract class for Password generation'''
  
  @abstractmethod
  def PasswordGenerator(self, type):
    self.type=type
  
class RandomPasswordGenerator(PasswordGenerator):
  
  def PasswordGenerator(self, length):
    combine_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(combine_characters, k=length))
    return password
  

class MemorablePasswordGenerator(PasswordGenerator):
  pass