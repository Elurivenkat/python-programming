li=[[10,20,30,40],[50,60,70,80]]
for i in li:
    for j in i:
        print(j)

li=[10,20,30,40,50,60]
k=2
rotated=li[k:]+li[:k]
print(rotated) 

li=["apple"," ","banana"," ","cherry"]
a=[i for i in li if i!=" "]
print(a)

num=[10,20,30,40,50,60]
chunk_size=2
for i in range(0,6,2):
    chunk=num[i:i+2]
    print(chunk)

num=[10,20,30,40,50,60]
num.sort()
print("second smallest number:",num[1])
print("second largest number:",num[-1])

li=[1,2,3,-5,-6,-8,10,12,-22]
positive=negative=even=odd=0
for i in li:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    if i%2==0:
        even+=1
else:
    odd+=1 
print("positive number:",positive)  
print("negative number:",negative)                
print("even number:",even)                
print("odd number:",odd)          

a=[10,20,30,40]
b=[20,30,50,60]
common=[i for i in a if i in b]
print(common)

a=[2,3,4,5]
b=[4,5,6,7]
diff=[i for i in a if i not in b]
print(diff)

a=[1,2,2,3,3,4,5,5,6]
duplicate=[]
for i in a:
    if a.count(i)>1 and i not in duplicate:
        duplicate.append(i)
print(duplicate)

a=[1,2,2,3,3,4,5,5,6]
new=[]
for i in a:
    if i not in new:
        new.append(i)
print(new)

s=[ i*i for i in range(1,11)]
print(s)

e=[ i for i in range(1,100) if i%2==0]
print(e)

w=("hello","astro")
u=[ i.upper() for i in w ]
print(u)

li=[12,45,65,76,87,90]
u=[ i for i in li if i>50]
print(u)

li=[-1,-2,45,3,-6]
n=[ 0 if i<0 else i for i in li]
print(n)

nums=[1,2,3,4,5,66,7]   
result = 1
for i in nums:
    result *= i
print(result) 

nums = [1, -2, 3, -4]
nums = [x for x in nums if x >= 0]
print(nums)

print(nums==nums[::-1])
print(nums)







