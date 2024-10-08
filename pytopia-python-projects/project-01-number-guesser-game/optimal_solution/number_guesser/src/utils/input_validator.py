def get_valid_input(prompt,start,end):
  ''' Get valid integer input between start and end '''
  while True:
    try:
      user_input = int(input(prompt))
      if(start <= user_input <= end):
        return user_input
      else:
        print(f"Enter input within the range between {start} and {end}")
    except ValueError:
      print(f"Invalid input, Please enter a number")
      