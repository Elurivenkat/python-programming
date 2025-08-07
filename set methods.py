#add(obj)
s1={100,200,300,400,500,600,600,800}
s1.add(900)
print(s1)
print("----")
#pop()
s1.pop()
print(s1)
#remove()
s1.remove(600)
print(s1)# if ele not present in the set shows key error
#discard()
s1.discard(900)
print(s1)
print("----")
#copy
h=s1.copy()
print(h)
print("----")
#isdisjoint
s1={100,200,300,400,500,600,700,800,100,900}
s2={600,700,2000,4000,500,8000,10000,150,240}
print(s1.isdisjoint(s2))
print("----")
#issubset
print(s1.issubset(s2))
print("----")
#issuperset()
print(s1.issuperset(s2))
#update
s1.intersection_update(s2)
print(s1)
#symmetric_difference_update()
s1.symmetric_difference_update(s2)
print(s1)














