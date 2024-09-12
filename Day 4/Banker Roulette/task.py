import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))
rNum = random.random()
print(rNum)
if 0.20 >= rNum >=0:
    print(friends[0])
if 0.40 >= rNum >=0.20:
    print(friends[1])
if 0.60 >= rNum >=0.40:
    print(friends[2])
if 0.80 >= rNum >=0.60:
    print(friends[3])
if 1 >= rNum >=0.8:
    print(friends[4])

r_index = random.randint(0, 4)
print(friends[r_index])