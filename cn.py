a=18
if a>=18:
    print("eligible")
else:
    print("not")    

print('----')

num=int(input("enter the number: "))
if num%2==0:
    print("even")
else:
    print("odd")
print("---")

num=int(input("enter the number: "))
if num%7==0:
    print("divisible by 7")
else:
    print("not")    
print("----")

num=int(input("enter the number: "))
if num%5==0:
    print("hello")
else:
    print("bye")    
print('---')

li=[1,3,4,5,23,222,24,2,7]
for i in li:
    if i%2!=0:
        print(i)
print('---')

ebill=int(input("enter the units: "))
if ebill==100:
    print("no charge")
elif ebill>100:
    print("5rupees per unit")
elif ebill>=100:
    ("10rupees per unit") 
print('---')           

num=int(input("enter the number: "))
last_digit=num%10
print("the lastdigit is:",last_digit)   
print('---')

num=int(input("enter the number: "))
last_digit=num%10
if last_digit%3==0:
    print("divisible by 3")
else:
    print("not")    
print("-------")

marks=int(input("enter the marks: "))
if (marks>90):
    print("grade A")
elif (marks>80 and marks<=90):
    print("grade B") 
elif (marks>=60 and marks<=80):
    print("grade C")
elif (marks<60):
    print("grade is D")
else:
    print("exit form app")      
print("----")

cost=int(input("enter the cost: "))
if (cost>100000):
    print("15percent tax")
elif (cost>50000 and cost<=100000):
    print("10percent tax")
elif (cost<=50000):
    print("5percent tax")
else:
    print("exit form app")           
