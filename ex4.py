# python program to take user name and a character and count the character in name 

name,ch = input("enter a name and character separated by comma ").split(",")

print(len(name))
print(name.lower().count(ch.lower()))
