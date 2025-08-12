#group of statement to perform a task
#advantages
#code reusability
#when ever dividing into multiple function it can easily track
def walking():
    print("get ready")
    print("tie shoes")
    print("water bottle")
walking()    #function without parameters
#function with parameters 
def add(a,b):
    print(a+b)
add(10,20)
#write a program simple calculate intrest
def cal(p,t,r):
    print(p*t*r/100)
cal(28,45,37)
#return keyword
#pythin returns more than two values 
# java returns only one value
def sh():
    return 
print(sh())
print("----")
def ses():
    return "clothes"
print(ses())
print("-----") 
def ret(a,b):
    return [a+b,a-b,a*b,a/b]
print(ret(10,20))
#local variable
# when ever declare the variable inside the method 
# can access inside the method only not outside
def loc():
    q=29
    print(q)
loc()
#global variable
b=10
def glo():
    print(b)
glo()
#global keyword 
#global expression
b=10
def glo():
    global b
    b=b*5
    print(b)
glo()                  
