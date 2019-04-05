# def a function find common item in two list 
# and return lst with common item
# ex :-
# input [1,2,3,4] [1,2,6,7]
# output [1,2]

def com_itm_lst(l1,l2):
    new_lst = []

    for i in l1:
        for j in l2:
            if i == j:
                new_lst.append(i)
                break
        
    return new_lst
    

l1 = [1,2,3,4]
l2 = [1,2,6,7]
print(com_itm_lst(l1,l2))
