# ##==========================================
# ##1. STRINGS & SLICING
# ##==========================================

# ## String
# word = "I am rafi"
# age = "I am 24 years old"
# print (word)
# print(word[2])
# print(len(word))
# print(word + " " + age)

# ## slicing
# print(word[5:9])
# print(word[5:])


# ##==========================================
# ##Formatting
# ##==========================================

# ## Normal formatting

# a = 10
# b = 5
# sum = a + b

# print("The sum of {} and {} is {}".format(a,b,sum) )
# print("The sum of {1} and {0} is {2}".format(a,b,sum) )

# ## f-string formatting

# print(f"the sum of {a} and {b} is {a+b}")

# # ==========================================
# # Built in data types
# # ==========================================

# ## Lists

# list1 = [1,9,8,"nhjb",8,7,0,0,0]
# print(list1)
# print(list1[2])
# print(list1[1:4])
# print(len(list1))
# print(type(list1))
# list1.append(10)
# print(list1)
# list1.insert(3,"oioi")
# print(list1)


# # Lenear search
# ind = 0
# total = 0
# for val in list1:
#     if val ==0:
#         print(f"0 is in {ind} no index")
    
#         total += 1
#     ind +=1
# print(f"Total 0 in list is {total}")


# ## Tuples

# tup= (1,1,2,43,5,66)
# print (tup)
# print(type(tup))
# for i in tup:
#     print(i)
# tup2= (8,0,9)
# print(tup2[2])
# list3=[4,9,8,tup2]
# print(list3)
# tup3=(4,9,7,list3)
# print (tup3)

# ## Dictionary

# student={
#     "name":"abdulalah",
#     "age": 26,
#     "cgpa" : 3.23,
#     4:"sem"

# }
# print(student)
# for i in student:
#     print(i)
# print(student["age"])
# #diff kinds of operaions

# ## sets n{}

# set1={1,22,33,3,4,4,5,5}
# print(set1)
# print(set1.add(9))
# for s in set1:
#     print(s)

# set2={"hh",2,1,33}

# print(set1.intersection(set2))
# print(set1.union(set2))


####  tuple to list
# marks =(
#     ("HI",99),
#     ("jsk",00),
#     ("kso",72)

# )
# print(type(marks))
# print(marks)
# marks=list(marks)
# print(type(marks))
# marks.append(("ljs",88))
# print(marks)
# marks=tuple(marks)
# print(type(marks))

#### dic project
num_of_products = int(input("how many products :"))
products= []
for i in range(num_of_products):
    product ={}
    num_of_feathers=int(input('num of feathers :'))
    for j in range(num_of_feathers):
        key=input("key :")
        value=input("value :")
        product[key]=value
    products.append(product)
print(products)
