<<<<<<< HEAD
<<<<<<< HEAD
"""
This program is a 'Guess the number' game
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("What's your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print ("Maximum value is %d " % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ("Invalid guess")
  else:
    print ("Rolling")
    sleep(2)
    print ("First roll is %d " % (first_roll))
    sleep(1)
    print ("Second roll is %d " % (second_roll))
    total_roll = first_roll+second_roll
    print (total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("You won!")
    else:
      print ("You lost!")
roll_dice(6)
=======
"""
This program is a 'Guess the number' game
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("What's your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print ("Maximum value is %d " % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ("Invalid guess")
  else:
    print ("Rolling")
    sleep(2)
    print ("First roll is %d " % (first_roll))
    sleep(1)
    print ("Second roll is %d " % (second_roll))
    total_roll = first_roll+second_roll
    print (total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("You won!")
    else:
      print ("You lost!")
roll_dice(6)
>>>>>>> caa7a19daf82ef17cbd26673297aabeac62a1417
=======
"""
This program is a 'Guess the number' game
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("What's your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print ("Maximum value is %d " % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print ("Invalid guess")
  else:
    print ("Rolling")
    sleep(2)
    print ("First roll is %d " % (first_roll))
    sleep(1)
    print ("Second roll is %d " % (second_roll))
    total_roll = first_roll+second_roll
    print (total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("You won!")
    else:
      print ("You lost!")
roll_dice(6)
>>>>>>> a3c79e1e64543b0d6f078d5527564506ecdfc6db
