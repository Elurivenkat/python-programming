srt=int(input("enter the number:"))
end=int(input("enter the number:"))
for num in range(srt,end+1):
    sum=0
    temp=num
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==temp:
     print(temp)                
