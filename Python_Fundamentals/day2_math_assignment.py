# Q1

salary = int(input("Enter Your Salary :"))
if (salary <30000 ):
    print("5%")
elif (salary>= 30000 and salary<= 70000):
    print("15%")
else:
    print("25%")

# Q2
def fun_even(a,b):
    for i in range(a,b+1):
        if (i%2==0):
            print(i)

x = int(input("A :"))
y = int(input("B : "))
fun_even(x,y)

#Q4
def count_digits(n):
   
        
    count = 0
    while n > 0:
        count += 1
        n = n // 10  # Remove the rightmost digit
        
    return count

# Example usage:
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))

##Q7
while  True:
   
   a= input("Enter a number : ((Type quit to quit) ::")
   
   if a=="quit":
       break
   
   if int(a)>0:
      print("Positive")
   else:
     print("neg")


print("End of the program")

   
     