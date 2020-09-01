import os
import random

def main():

  os.system('cls')

  dice_rolls = int(input("How many dice shall I roll? "))
  dice_size = int(input("How many sides to each die? "))
  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    print(f'You rolled a {roll} and {roll} and {roll}')
  if dice_sum==(dice_size):
    print('You rolled SnakeEyes! Critical Fail!')
  elif dice_sum==(dice_rolls*dice_size):
      print(f'You rolled a total of {dice_sum}'" Critical HIT!")
  else:
    print(f'You rolled a total of {dice_sum}')
if __name__== "__main__":
  main()
