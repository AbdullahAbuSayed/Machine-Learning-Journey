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

class Employee:
    st_time = "10 am"
    end_time = "6 pm"
    def cng_time(self,new_time):
        self.end_time=new_time
        
    def break_time(self,b_time):
        self.b_time=b_time


class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject

t1=Teacher("english")
t1.cng_time("7 pm")
t1.break_time("3 pm")
print(t1.subject,t1.end_time,t1.b_time)