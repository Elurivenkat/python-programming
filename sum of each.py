num=int(input("enter the number:"))
sum=0
while num>0:
    last=num%10
    sum=sum+last
    num=num//10
print(sum)    