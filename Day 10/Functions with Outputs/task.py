
name = input("What is your name?")
bid = input("What is your bid? ")

play_again = True
while play_again:
    blind_auction = {
    name: bid,
    }
    play_again = input("Any other bidders? Yes or no").lower()
    if play_again == "yes":
        play_again = True
    else:
        play_again = False


winner = max(blind_auction[0][0])
print(f"The winner of the auction is {winner}")



