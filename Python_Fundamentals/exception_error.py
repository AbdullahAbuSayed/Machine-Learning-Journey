try:
    x= int(input("Input your num :"))
    dev = 10/x
except ZeroDivisionError:
    print("cant devide by 0")
except ValueError:
    print("Type numbers only")
else:
    print(dev)
finally:
    print("End of the program")
    