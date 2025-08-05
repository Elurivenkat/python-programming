num=int(input("enter the number:"))
rev=0
temp=num
while num>0:
    last=num%10
    rev=rev*10+last
    num=num//10
print(rev)
if rev==temp:
    print("palondrome")
else:
    print("not palindrone")        
