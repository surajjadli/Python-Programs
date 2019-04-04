#python program to find greatest of two 
def findgre(n1,n2):
    if n1 > n2:
        print(f"{n1} is greater")
    elif n2 > n1:
        print(f"{n2} is greater")
    else:
        print("both are equal")

num1 = int(input("enter a first number"))
num2 = int(input("enter a  second number"))

findgre(num1,num2)