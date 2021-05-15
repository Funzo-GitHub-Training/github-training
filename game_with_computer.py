# Exo2: Game with Computer:

import random

x = random.randint(0, 100)
y = int(input("enter a number to guess my own! "))

print(y)

while x != y:
 if x < y:
    y = int(input("wrong your number is bigger than mine.  Enter another one! "))
 else:
  if x > y:
     y = int(input("wrong your number is lower than mine.Enter another one! "))

if x == y:
  print("Good number.")  