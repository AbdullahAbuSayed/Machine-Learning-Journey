n= int(input("total name :"))
name_list=[]
for r in range(n):
    name=input(f"Enter your {r+1} name :")
    name_list.append(name)
    print (name)

for k in name_list:
    print(f"your name is {k}")
