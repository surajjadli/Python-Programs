# define a function to return reverse of list

def rev_lst(l):
    return l[::-1]

#using pop
def revlst(l):
    ls = []
    for i in range(len(l)):
        ls.append(l.pop())
    return ls

lst = [1,2,3,4]

print(lst)
print(rev_lst(lst))

print(lst)
print(revlst(lst))