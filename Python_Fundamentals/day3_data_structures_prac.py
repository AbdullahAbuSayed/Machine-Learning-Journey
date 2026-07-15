# ==========================================
# 1. STRINGS & SLICING
# ==========================================

### String
# word = "I am rafi"
# age = "I am 24 years old"
# print (word)
# print(word[2])
# print(len(word))
# print(word + " " + age)

### slicing
# print(word[5:9])
# print(word[5:])


# ==========================================
# Formatting
# ==========================================

### Normal formatting

# a = 10
# b = 5
# sum = a + b

# print("The sum of {} and {} is {}".format(a,b,sum) )
# print("The sum of {1} and {0} is {2}".format(a,b,sum) )

### f-string formatting

# print(f"the sum of {a} and {b} is {a+b}")

## ==========================================
## Built in data types
## ==========================================

### Lists

list1 = [1,9,8,"nhjb",8,7,0,0,0]
# print(list1)
# print(list1[2])
# print(list1[1:4])
# print(len(list1))
# print(type(list1))
# list1.append(10)
# print(list1)
# list1.insert(3,"oioi")
# print(list1)
# print(list1.sort())

## Lenear search
ind = 0
total = 0
for val in list1:
    if val ==0:
        print(f"0 is in {ind} no index")
    
        total += 1
    ind +=1
print(f"Total 0 in list is {total}")