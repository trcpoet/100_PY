print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
final_amount = (bill + (bill*(tip/100)))/people
bill_per_person= round(final_amount, 2)
print(f"The total bill per person is ${bill_per_person}")

