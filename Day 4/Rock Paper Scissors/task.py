import random

# p_choice = input("Select your choice: ")
# for p_choice in choices:
#     if p_choice == "rock" and choices == "rock":
#         print("tie")
#     elif p_choice == "rock" and choice == "paper":
#         print("Paper beats rock")
#     elif p_choice == "rock" and choice == "scissor":
#         print("Rock beats Scissor")
# # r_choices = random.randint(0,2)
# print(choices[r_choices])
#
choices = ["rock", "paper", "scissors"]

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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("The computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Tie!")








# p_choice = input("Select your choice (rock, paper, scissors): ").lower()
# r_choice = random.choice(choices)
# print(f"You chose {p_choice}")
# print(f"Computer chose {r_choice}")
#
# if p_choice == "rock":
#     print(rock)
# elif p_choice == "paper":
#     print(paper)
# elif p_choice == "scissors":
#     print(scissors)
#
# if r_choice == "rock":
#     print(rock)
# elif r_choice == "paper":
#     print(paper)
# elif r_choice == "scissors":
#     print(scissors)
#
# if p_choice == r_choice:
#     print("It's a tie")
# elif (p_choice == "rock" and r_choice == "scissors") or (p_choice == "paper" and r_choice == "rock") or (p_choice == "scissors" and r_choice == "paper"):
#     print("You win!")
# else:
#     print("You lose!")


