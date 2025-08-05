li=[1,2,-3,4,-5,6,-7,8,9]
positive=0
negative=0
for i in li:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
print("positive count: ", positive)
print("negative count: ",negative)            