# def get_input():
#     n=int(input("enter size of array:"))
#     arr=[]

l1=[]
print("An empty list",l1)

l2=[0,1,2,3]
print("list of four items:",l2)

l3=['abc',['def','ghi']]
print("A nested list",l3)

l4=list('spam')
print('list created from string spam',l4)

# str=input("enter your string: ")
# l4=list(str)
# print('list created from {str} spam',l4)

l5=list(range(-3,3))
print("list created from range(-3,3)",l5)

l6=[10,20,30,40]
print("Element at index 2 is:",l6[2])

l7=['x',[20,30,40,50],'y']
print("Element at l7[1][2] (nested list) is:",l7[1][2])

l8=[10,20,30,40,50,60,70]
print("slicing l8 from index 2 to 4",l8[2:5])

print("length of l8:",len(l8))

l9=[10,[100,200,300,400],50]
print("Element at l9[2] is:",l9[2])
print("Element at l9[1][3] (nested list) is:",l9[1][3])
print("slicing sublist l9[1][1:3] is",l9[1][1:3])







