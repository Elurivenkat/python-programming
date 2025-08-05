num=int(input("enter the number:"))
sum=0
temp=num
while num>0:
    last=num%10
    fact=1
    for i in range(1,last+1):
        fact=fact*i
    sum+=fact
    num=num//10
if sum==temp:
    print("strong")
else:
    print("not")            