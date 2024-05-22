import random

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

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
choices=[rock,paper,scissors]

random1=random.randint(1,3)



if user_input==0:
    print(choices[user_input])
    print("Computer chose:")
    print(choices[random1-1])
elif user_input==1:
    print(choices[user_input])
    print("Computer chose:")
    print(choices[random1-1])
elif user_input==2:
    print(choices[user_input])
    print("Computer chose:")
    print(choices[random1-1])
else:
    print("Wrong Choice")

if user_input==0 and random1==1:
    print("You lose")
elif user_input==0 and random1==2:
    print("You win")
elif user_input==1 and random1==0:
    print("You win")
elif user_input==1 and random1==2:
    print("You lose")
elif user_input==2 and random1==0:
    print("You lose")
elif user_input==2 and random1==1:
    print("You win")
elif user_input==random1:
    print("Draw")



