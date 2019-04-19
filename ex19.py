user = {}

user['name'] = input("enter your name")
user['age']  = int(input("enter your age"))
user['fav_movies'] = list(input().split(","))
user['fav_songs'] = list(input().split(","))

for key,values in user.items():
    print(f"{key} : {values}")