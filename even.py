li=[1,2,3,4,5,67,8,]
even=0
odd=0
for i in li:
    if i%2==0:
        even+=1
    elif i%2==1:
        odd+=1
print("even count:",even)
print("odd count:",odd)            