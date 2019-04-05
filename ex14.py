# pyhton program to reverse each string or item in list

def rev_lst_itm(l):
    new_lst = []
    for i in l:
        new_lst.append(i[::-1])
        
    return new_lst

lst = ['abc', 'tuv', 'xyz']

print(lst)
print(rev_lst_itm(lst))
