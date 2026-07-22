import json
json_st='{"name":"maria", "age":25,"isStd":true}'
py_dst= json.loads(json_st)
print(py_dst)
print(type(py_dst))

py_dst2={'name': 'usama', 'age': 21, 'isStd': True}
json_st2= json.dumps(py_dst2)
print(json_st2)
print(type(json_st2))

with open("Python_Fundamentals/json_sample.json","r") as f:
   
    data = json.load(f)
    print(data)

with open("Python_Fundamentals/json_sample.json","w") as ff:
   
    data = json.dump(py_dst2,ff)
    