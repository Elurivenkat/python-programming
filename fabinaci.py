num=int(input("enter the number:"))
frst=0
sec=1
for i in range(num):
    print(frst,end=" ")
    thrd=frst+sec
    frst=sec
    sec=thrd