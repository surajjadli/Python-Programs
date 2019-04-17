# program to count list inside list 

def cnt_lst(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=1
    return count 

lst = [1,2,3, [1,2], [5,4,3]]

print(cnt_lst(lst))