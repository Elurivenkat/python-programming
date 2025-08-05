num=int(input("enter the number: "))
rev=0
while num>0:
    lastdigit=num%10
    rev=rev*10+lastdigit
    num=num//10
print(rev)    