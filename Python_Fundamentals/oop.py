### Class
class student:
    subject ="math"
    year = 2019
    clg = "ngc"

student1=student()
print(student)
print(student1.clg,student1.subject)

## Constractor init

class car:
    wheel = "4 wheeler"
    def __init__(self,model,num):
         self.model = model
         self.num = num
         print("called automatically")
    color="black"
car3=car() #Not work because init have to be initialize
print(car3.color)
car1=car("Toyota",123)
print(car1.wheel,car1.color)
# print(car1.model)
car2=car("BMW",555)
print(car2.color,car2.wheel)


########  METHID

## Instance Method
class laptop:
     storage_type = "ssd"

     @classmethod
     def variant(cls):
          print(f"This variant is {cls.storage_type} variant")
        
     def __init__(self,color,ram,ssd):
          self.color = color
          self.ram = ram
          self.ssd = ssd
    
     @staticmethod
     def price(cPrice,dPrice):
          print(f"Total Price {cPrice*dPrice}")
    


     def get_print(self):
          print(f"This laptop color is {self.color} and spec is {self.ram} gb ram and {self.ssd} gb {self.storage_type}")
          
laptop1=laptop("Black",16,512)
laptop1.get_print()    

### Class Methods
laptop1.variant()


### Static Method
laptop1.price(10,20)


class store:
    count = 0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        store.count+=1

    def get_info(self):##instance method
        print(f"Product is {self.name} and price is {self.price} Tk ")
    
    @classmethod
    def total_product(cls):
        print(cls.count)
    
    @staticmethod
    def discount(price,discount):
        print(f"Total discount{(price*discount)/100}")

product1=store("chips",10)
product2=store("tv",1000)
product1.get_info()
product1.total_product()
product1.discount(10,20)