#define a function to filter odd and even in list
# for ex:-
#input  [1,2,3,4,5,6,7,8,9]
#output  [[1,3,5,7,9],[2,4,6,8]]

def sep_evn_odd(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    
    return [even,odd]

lst = [1,2,3,4,5,6,7,8,9]
print(sep_evn_odd(lst))