try:
    age = int(input("How old are you?"))
except ValueError:
        print("You have typed an invalid number, try again with a numerical response like '15'")
        age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}.")

# ValueError: invalid literal for int() with base 10: ' twelve '