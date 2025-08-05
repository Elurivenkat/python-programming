num=int(input("enter the number:"))
if num%4==0:
    print("leap year")
elif num%100==0:
    print("not")
elif num%400==0:
    print("leap year")
else:
    print("not leap year")            