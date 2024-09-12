print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))
weight = int(input("What is your weight in lbs?: "))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age?: "))
    if age <= 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay 5")
    else:
        print("Pay $12")
    if weight >= 150:
        print("Too fat, need to get fitter")
    elif 45 <= age <= 55:
        print("Free on us")
    else:
        print("Fit enough")
        print("You can ride the rollercoaster")
else:
    print("Sorry you have to get taller before you can ride.")
