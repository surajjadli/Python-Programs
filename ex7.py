# sum of natural number 
# ask user for limit 
# print total

limit = int(input("enter a number =>"))

total = 0
i = 1

while i <= limit:
    total+=i
    i += 1
    
print(total)