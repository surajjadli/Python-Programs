# ask user for more than one digit number
#ex 123
#then calculate their sum 1+2+3

number = input("enter a number =>")

total = 0
i = 0

while i < len(number):
    total += int(number[i])
    i += 1
print(total)