# python program for number guessing
# generated a random no. from random.randint()
# if user_number is equal to random_number then print "YOU WIN"
# if less then print "too low"
#if greater then print "too high"

import random 
random_number = random.randint(1,100)

print(random_number)

user_number = int(input("enter a your number"))

if user_number > random_number:
    print("too high")
elif user_number < random_number:
    print("too low")
else:
    print("YOU WIN!!!")