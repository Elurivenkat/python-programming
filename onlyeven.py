li=[1,2,3,4,5,6,7,8]
for i in li:
    if i%2==1:
     print(i)
print("done")

for i in range(1,10):
   print(i)

for i in range(0,11,2):
   print(i)
print("----")

for i in range(1,12,2):
   print(i)
print(".....*")


for i in range(1,100):
   if i==25:
      continue
   print(i)


for i in range(1,20):
   if i%5==0:
      continue
   print(i)

word="pythonprogramming"
for ch in word:
   if ch not in 'aeiou':
      continue
   print(ch)

for i in range(1,31):
   if i%2==0:
      continue
   print(i)

for i in range(1,100,2):
   print(i)
print("-------")


li=[1,2,3,4,5,6,7,8,9]
total=0
for i in li:
   total+=i
   print(total)
print("done")


li=[2,4,34,56,78,87,55,11,45,90]
even=0
odd=0
for i in li:
   if i%2==0:
      even+=1
   elif i%2==1:
      odd+=1
print(even)
print(odd)


li=[1,2,3,4,5]
for i in li:
   if i%2==0:
      print(i)

for i in range(1,100):
   if i==25:
      pass
   print(i)      

      
        