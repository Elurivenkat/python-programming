s={100,200,300,400,500}
print(type(s))
print(s)
print("----")
#basic operation in set 
#Union
s1={100,200,300,400}
s2={100,200,400,500,600}
print(s1.union(s2))
print("----")
#intersection
print(s1.intersection(s2))
print("----")
#difference
print(s1.difference(s2))
print("----")
#symmetric
print(s1.symmetric_difference(s2))
print("----")
#union used to extended fron s1 to s2
#used take common element on bth sets

