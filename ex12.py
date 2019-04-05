# define a function that take list as a parameter
# square the content of list
def sq_lst(l):
    sq = []
    for i in l:
        sq.append(i*i)
    print(sq)

lst = [1,2,3,4]
sq_lst(lst)