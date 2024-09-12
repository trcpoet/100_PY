import random
import my_module

# rInt = random.randint(1, 99)
#
# print(rInt)
# print(my_module.my_fav_num)
#
#
# rNum = random.random()* 10
# # for random.random(0), 0.0 <= N <= 1.0
# print(rNum)

# rFloat = random.uniform(1, 10)
# # generates a number from a to b, with a and b inclusive
# print(rFloat)



chance_number = random.random()*100
if chance_number <50:
    print("Heads")
else:
    print("Tails")
print(chance_number)