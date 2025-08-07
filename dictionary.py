d={1:100,2:200,3:300,4:400}
print(type(d))
print(d)#creating of dictionary
print("----")
#update
d[1]=300
print(d)
print("----")
d[5]=500
print(d)
#deletion
del d[3]
print(d)
#methods in dictionary
#get(k)
print(d.get(1))
print("----")
#get(k,default value)
print(d.get(9,"page not found"))
#keys()
print(d.keys())
#values()
print(d.values())
#items
print(d.items())
#clear() this method is used clear all items
#copy() this method is used one dic to another dictionary
#pop()
print(d.pop(1))
#update
d2={5:500,6:600,7:700,8:800}
print(d.update(d2))
print(d)
#setdefault
print(d.setdefault(3,300))
print(d)
#dictionary comprehension
s={ i:i*i for i in range(1,10)}
print(s)
c={ i:i*i for i in range(1,10) if i%2==0}
print(c)
e={i:i*i for i in range(1,10) if i%2!=0}
print(e)
#zip(key,value)
a=[1,2,3,4]
b=[100,200,300,400]
print(dict(zip(a,b)))