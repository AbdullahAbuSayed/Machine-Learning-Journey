sq = []
for i in range(1,6):
    k = i**2
    sq.append(k)
print(sq)

#### output iterate(range) condition

sq2=[i**2 for i in range(6)]
print(sq2)

num = [-4,-3,-5,0,-9,-84,9,5]
num = [0  if val<0 else val for val in num]
print(num)

st= ["jsbib","hjvjv","ibsiub"]
st=[word.upper() for word in st]
print(st)

