import random

class Cube:
    def __init__(self, wigs):
        self.wigs = wigs
    
    def roll(self):
        return random.randint(1, self.wigs)

      
def set_wigs() -> int:
  while True:
    try:
      wigs : int = int(input("Enter number of wigs"))
      return wigs
    except ValueError:
      print("ivalid argument, try again.")
      
if __name__ == '__main__':
  wigs = set_wigs()
  cube = Cube(wigs)
  
  user_input = input("Do you want to roll? Y/N: ")
  while user_input.upper() != 'N':
    if user_input.upper() == 'Y':
      print(cube.roll())
    else:
       print("ivalid argument, try again.")
  

