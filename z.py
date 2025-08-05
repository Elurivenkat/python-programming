li=[100,200,300,400,500,600]
for i in li:
    print(i)

li1=[100,200,300,400,500]
print("before adding number",li1)
li1.append(600)
print("after adding number",li1)
print(li1)

li2=[250,350,450,550,650]
print("before inserting",li2)
li2.insert(0,150)
print("after inserting",li2)
print(li2)

li3=[220,440,320,520]
print("before removing",li3)
li3.remove(520)
print("after removing",li3)
print(li3)

li4=[29,40,5,33,22,77,88,90,80]
sublist=li4[2:8]
print("original list",li4)
print("sublist",sublist)

li5=[29,40,5,33,22,66]
print(li5[1:4])
li5.reverse()
print("reverse list",li5)

li6=[29,40,5,33,22,77,88,90,80]
print("before sorting list",li6)
li6.sort(reverse= True)
print("after sorting list",li6)
print(li6)

li7=[29,40,5,33,22,77,88,90,80]
length=len(li7)
print("the length of list",length)
  
li7=[29,40,5,33,22,77,88,90,80] 
print(88 in li7)

li7=[29,40,5,33,22,77,88,90,80]
print("before pop element",li7)
print("after pop element",li7.pop())
print(li7)

li7=[29,40,5,33,22,77,88,90,80]
del li7[5]
print(li7)

li=[2,3,4,5,5,6,7,7]
a=list(set(li))
print(a)
li


li=[1,2,3,4,5,6,7]
a=sum(li)/len(li)
print( "avearge",a)

li=[2,3,4,5,67,89]
li[0],li[-1]=li[-1],li[0]
print(li)

li=[2,4,3,5,6,7,8,9]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd) 

li=[3,4,6,7,8,93,56]
k=2
a=li[k:]+li[:k]
print(a)

w=["hello","","hi","","bye"]
print([i for i in w if i!=""])

li=[1,2,3,4,5,6,7,8,9]
li.sort()
print("second smllest:",li[1])
print("second lagrest:",li[-2])
print(li)
li.append(10)
print(li)
num=[1,2,1,2,3,4,5,12,1,2,3,12]
a=list(set(num))
print(a)

