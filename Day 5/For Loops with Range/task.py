x=0
for number in range(1,101):
    x += number

print(x)
y=0
for x in range(1,101):
    print(x)

for i in range(1, 101):  # Loop from 1 to 100 inclusive
    if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif i % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:
        print(i)  # Print the number itself