li=[1,2,3,4,5,6,7,8]
for i in li:
    if i%2==0:
        print(i)

li=[1,2,3,4]
sum=0
for i in li:
    sum+=i
    print(sum)
print("----")    
li=[1,-2,4,-3,-5,6,7,8,-9]
positive=0
negative=0
for i in li:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
print(positive)
print(negative)
print("----")
nums=[1,2,34,78,45,98]
max_num=nums[0]
for i in nums:
    if i>max_num:
        max_num=i

print(max_num)
print("-----")

for i in range(1,50):
    if i%2==0:
        continue
    print(i)
print("---")
for i in range(1,80):
    if i==26:
        break
    print(i)
print("---")
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("-----")
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
print("----")
for i in range(1,10):
    if i%2==0:
        print("fizz")
        continue

    elif i%3==0:
        print("buzz")
        continue
    print(i)
print("----")
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
print("---")

for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
print("---")
for i in range (6,)
for i in range(6,0,-1):
    for j in range(i):    
        print("*",end=" ")
    print()            
                      