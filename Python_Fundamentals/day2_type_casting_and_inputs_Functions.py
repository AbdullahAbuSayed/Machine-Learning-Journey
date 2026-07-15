#Conditional Styatements
'''
a = int(input("Entetr your age: "))
if a>18 :
    print ("You are adult")
elif a==18:
    print("You atre 18")
else:
    print ("You are not adult")'''

#if elif

''''color_input = input("Enter the color (Red, Green, Yellow): ")

if color_input== "Red":
    print("You selected Red")
elif color_input== "Green":
    print("You selected Green")
elif color_input== "Yellow":
    print("You selected Yellow")
else:
    print("Invalid color selected")
    '''
''''num = int(input("Enter your number : "))

# Multiple by 5

if num==5:
    print("number is 5")
elif num%5==0:
    print ("Multiple of 5")
else :
    print("Number is not a multiple of 5 and not 5")'''

#Even Odd

''''n = int(input("enter a number"))
if (n%2==0):
    print("Devided by 2")
else:
    print("not devided by 2")
'''


# Nesting
'''
username = input("Enter your username :")
password = input("Enter Your Pass :")

if (username == "admin" and password == "1234"):
    print("Successful")
else:
    if (username != "admin" and password !="1234"):
        print("Wrong username and password")
    elif username!= "admin":
        print("Wrong username")
    else:
        print("wrong pass ")
'''

#Loop
#while
'''
i=1
while (i<=5):
    print("Hello World" , i)
    i +=1

print(i)


while (i>=1):
    print(i)
    
    i -=1
'''

## Print multiplication
# n = int(input("Enter the number you want to multiply :"))

# i=0
# while (i<10):
#     print (n, "*" ,i+1,"= ", n*(i+1) )
#     i +=1

# Break and Continue

# i = 1
# while (i <= 10):
#     if (i % 2 == 0):
        
#         continue
#     print(i)
#     i += 1


#### For Loop

# x = "Hello World"

# for i in x:
#     print (i)

# word ="ioishigvbiugvbiusg iyfydu giouf wyiusvhj giiiiiiiiiiiiiiiif utidyscyugukigf dscduyxkjgbjf aop;sh"

# count = 0
# for i in word:
#     if (i=="i"):
#      count += 1

# print (count)

# for c in range(10):
#     print(c+1) 

# for ch in word:
#     if (ch =="a" or "e" or "i" ):
#         count +=1

# print (count)



### sum of n

# count = 0
# for i in range(1,6,2):
#      count += i

# print(count)

# def sum(a,b,c):
#     s= (a+b+c)/3

#     print(s)

# sum(2,9,4)

### fact function

def calc(n):
    fact=1
    for i in range(1,n+1):
  
      fact *= i
    return fact

num = int(input("Ent a num"))
print(calc(num))



