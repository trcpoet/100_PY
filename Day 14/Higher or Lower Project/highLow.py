import random

from game_data import data
from art import logo, vs
print(logo)

def check_answer(user_guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")


    guess = input("Make a guess. Choose 'a' or 'b': ".lower()

    a_followers = account_a["follower_count"]

    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print("Correct!")
    else:
        game_should_continue = False
        print("You lose.")
