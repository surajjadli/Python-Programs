#define a function that takes a number(n)
#return a dict containing cubes of numbers frrom 1 to n 

#example
#cube_finder(3)
# {1:1, 2:8, 3:27}

def cube_finder(n):
    cube = {}
    for i in range1,n+1):
        cube[i] = i**3
    return cube

n = int(input("enter a number "))
print(cube_finder(n))
