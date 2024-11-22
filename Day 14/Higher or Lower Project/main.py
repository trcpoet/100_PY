import random

from game_data import data
from art import logo,vs

def format_data(account):
    """ #Takes the account data and returns the printable format. """
    account_name = account["name"]
    # account_followers = account["follower_count"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

#Check if user is correct
def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == 'b'

print(logo)
score=0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #Generate a random account from the dictionary game_data

    #Make account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': \n").lower()

    #clear the screen
    print("\n"*20)
    print(logo)
    ##Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    #Score keeping
    if is_correct:
        score += 1
        print(f"you're right! Current score {score} \n" )
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


#Make the game repeatable and




























# name = data.get("name")
# followers = data.get("follower_count")
# description = data.get("description")
# country = data.get("country")

# name = data["name"]
# followers = data["follower_count"]
# description = data["description"]
# country = data["country"]

# def compare():
#     for dict in data:
#         for key, value in dict.items():
#             print(key, ":", value)
#         print("")
#
#
# compare()
#
# def func(dict):
#     return dict["name"]
# def func2(dict):
#     return dict["follower_count"]
# def func3(dict):
#     return dict["description"]
# def func4(dict):
#     return dict["country"]
#
# name = list(map(func, data))
# followers = list(map(func2, data))
# description = list(map(func3, data))
# country = list(map(func4, data))
#
# print("Compare A:", name, followers, description, country)
