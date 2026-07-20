#### Encaptulation - Wrapping data and functions into a single unit

# ### data hiding
# class BankAccount:
#     def __init__(self,Name,Balance):
        
#         self.Name=Name
#         self.__Balance=Balance ##_ means Protected and __ means private(have to make getter and setter)

#     def get_balance(self):  ##getter
#         return self.__Balance
#     def set_balance(self,newBalance):
#         self.__Balance=newBalance

# acc1=BankAccount("mr. No Name", 100000)

# acc1.set_balance(200000)
# print(acc1.Name,acc1.get_balance())

# ## Another way to access the private data
# print(acc1.Name,acc1._BankAccount__Balance)##without the get set



#### Inheritance - reuseing attr and methods from parent or base class

# ###single level inheritance
# class Employee:
#     st_time = "10 am"
#     end_time = "6 pm"
#     def cng_time(self,new_time):
#         self.end_time=new_time
        
#     def break_time(self,b_time):
#         self.b_time=b_time


# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject

# t1=Teacher("english")
# t1.cng_time("7 pm")
# t1.break_time("3 pm")
# print(t1.subject,t1.end_time,t1.b_time)

# ### Types of inheritance

# ## single level inheritance (a to b)- already learned

# ## Multilevel inheritance (a to b to c)

# ### Multiple Inheritance (multiple parent one child a and b to c)

# ## Multilevel inheritance
# class Assistant_Teacher(Teacher):
#     def __init__(self, salary,subject):
#         super().__init__(subject) ## For calling the constractor of the mother class
#         self.salary= salary

# assis1=Assistant_Teacher(25000,"PL")
# print(assis1.salary,assis1.end_time,assis1.subject)


# ### Multiple Inheritance
# class Student:
#     def __init__(self,cgpa):
#         self.cgpa = cgpa
    
# class Tc:
#     def __init__(self,task):
#         self.task=task

# class Captain(Student,Tc):
#     def __init__(self,cgpa,task,name):
#         super().__init__(cgpa)
#         Tc.__init__(self,task)        
#         self.name=name
    
# cap1=Captain(3.14,"Nothingg","Asad")
# print(cap1.name,cap1.cgpa,cap1.task)



#### Abstraction - hiding esential data snd showing the main things its a blueprint for others classes it doesnt have his own attributes(ABC)

from abc import ABC,abstractclassmethod
class Animal(ABC):
    @abstractclassmethod
    def sound(self,sound):
        self.sound=sound
        pass
class Lion(Animal):
    def sound(self):
     print("Roar")

lion=Lion()
lion.sound()


#### Polymorphysm - many functions same name wihn diff opperations
### 2 Types 
## 1. Function Overriding - For class parent and child (can modify the child functions)
## 2. Duck typing (2 functions have same name and there like similar but in different classes)

## 1. Function Overriding
class Role:
   def role(self):
      print("Nothing")

class Admin(Role):
   def role(self):
      print("Admin")

admin1=Admin()
admin1.role()

## 2. Duck typing
class His:
   def name(self):
      print("Rohan")

class Her:
   def name(self):
      print("Rishi")

his1=His()
her1=Her()
his1.name()
her1.name()