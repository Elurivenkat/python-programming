s=1
e=1000
for num in range(s,e+1):
    sum=0
    temp=num
    while num>0:
        last=num%10
        fact=1
        for i in range(1,last+1):
            fact*=i
        sum+=fact
        num=num//10
    if sum==temp:
        print(temp)    

                