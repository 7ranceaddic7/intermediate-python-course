import os
import random

def main():

  os.system('cls')

  dice_rolls = 2
  dieSum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    dieSum += roll
    print(f'You rolled a {roll}')
  if dieSum==2:
    print('You rolled SnakeEyes! Critical Fail!')
  elif dieSum==12:
      print(f'You rolled a total of {dieSum}'" Critical HIT!")
  else:
    print(f'You rolled a total of {dieSum}')

if __name__== "__main__":
  main()
