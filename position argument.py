def pro(item,quality,pay):
    print(item,quality,pay)
pro("cloth",1,300)
#keyword argument
def reg(name,age,gender):
    print(name,age,gender)
reg(age=22,name="astro",gender="male") 
#default argument
def book(name,age,location="bengalore"):
    print(name,age,location)
book("astro",22,location="hyd")
book("ven",21)    

#variable length argument(*)
#when ever don't know no of arguments you want pass to the parameter *args accept as any no of arguments
def var(*items):
    print(items)
var("fish","coffe",2626)

def hotel(*items):
    for i in items:
        print(i)
hotel("hi","mutton","curry",570)
#variable **kwrg 
# when ever dont know no of argument you want to pass in the form of key value pairs to the parameter
def hot(**kwrg):
    for i in kwrg.items():
        print(i)
hot(name="astro",a="coffe",id=234)

