rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print(f"{user} is not an option.")
    
print("Computer chose:")
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
else:
    print("Computer didn't want to play.")

if user == 0:
    if computer == 0:
        print("Draw")
    elif computer == 1:
        print("You lose")
    elif computer == 2:
        print("You win")
elif user == 1:
    if computer == 0:
        print("You win")
    elif computer == 1:
        print("Draw")
    elif computer == 2:
        print("You lose")
elif user == 2:
    if computer == 0:
        print("You lose")
    elif computer == 1:
        print("You win")
    elif computer == 2:
        print("Draw")
else:
    print("")