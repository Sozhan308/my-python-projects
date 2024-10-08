def provide_hint(guess, actual_number):
  ''' Provide hint based on diff b/w guess and actual number '''
  if(guess < actual_number):
    return f"Try with higher number than {guess}"
  else:
    return f"Try again with lower number than {guess}"