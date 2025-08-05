num=int(input("enter the value:"))
sum=0
a=num
while num>0:
    last=num%10
    sum=sum+last*last*last
    num=num//10
print(sum)
if sum==a:
    print("armstrong")
else:
    print("not")        