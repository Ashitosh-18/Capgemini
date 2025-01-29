t1=()
print("it is an empty tuple ",t1)

t2=(0,)
print("only 1 element",t2)

t3=(0,'Ni',1.2,3)
print("4 element tuple ",t3)

t4=0,'Ni',1.2,3
print("4 element tuple but without brackets",t4)

t5=('abc',('efg','hij'))
print("nested tuples",t5)

t6=tuple('spam')
print(t6)

t7=(0,('apple','mango','grapes'),1.2,3,'hello')
print(t7[2])

print(t7[1][2])

print(t7[2:4])

print(len(t7))






