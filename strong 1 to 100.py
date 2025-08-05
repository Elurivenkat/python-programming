srt=int(input("enter the number:"))
end=int(input("enter the number:"))
for num in range(srt,end+1):
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
        print(temp)    
            
