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
