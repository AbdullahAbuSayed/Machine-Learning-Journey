# ### Read

# f = open("Python_Fundamentals/sample.txt", "r")
# Data = f.read()
# print(Data)
# Data=f.readline()
# print(Data)

# f.close

# ##Write

# wr=open("Python_Fundamentals/sample.txt", "w")
# new=wr.write("Thsi is overwrited \n New data added")
# wr.close()

# ## Append is also same just write at the end

# ### w+, r+, a+

# ## with kw automatically handles open close

# with open("Python_Fundamentals/sample.txt", "r+") as e:
#     # e.write("New ")
#     # print(e.read()) ## pointer is in the beginning

#     e.read()
#     e.write("This is a trial")## pointer is at the end so its write last

#### similarly works with a+ and w+(works with pointer)

# import os
# y = open("Python_Fundamentals/sample2.txt", "x")


## delete
# os.remove("Python_Fundamentals/sample2.txt")

line =1
with open("Python_Fundamentals/sample.txt", "r") as ff:
    while True:
        data = ff.readline()
         
        if ("python" in data):
            print ("Found")
            print(f"Line {line}")
            break
    
        print(data)  
        line+=1
    
    