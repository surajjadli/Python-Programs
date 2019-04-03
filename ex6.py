# if user_name start with a or A and age is above 10 then
#print "you can watch movie"
#otherwise "sorry!! you can't watch movie"

user_name = input("enter your name =>")
user_age = int(input("enter your age =>"))

if user_name[0] == 'a' or user_name[0] == 'A' and user_age > 10:
    print("you can watch coco movie")
else:
    print("sorry! you can't watch coco movie")