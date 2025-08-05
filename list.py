li1=[10,12,34,45]
li2=[12,34,56,36]
print(li1)
print(len(li1))
print(li1+li2)
print(li1*3)
print(12 in li1)
for i in li1:
    print(i)
for i in range(len(li1)):
 print(i)
s=[1,2,3,4,5,6,7,8] 
for i in enumerate(s):
   print(i)
print(max(s))
print(min(s))
print("-----")
li=[12,23,34,45,56,67]
print(li[2])
print(li[4])
print(li[1:3])
print(li[1:])
print(li[:4])
print(li[::-1])
li[2]=300
print(li)
li[1:3]=100,200
print(li)
del li[2]
del li[1:3]
print(li)      
