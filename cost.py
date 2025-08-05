cost=int(input("enter the price: "))
if cost>100000:
    print("tax is 15%")
elif (cost>=50000 and cost<=100000):
    print("tax is 10%") 
elif (cost>=80000 and cost<=20000):
    print("tax is 5%")
else:
    print("no tax")