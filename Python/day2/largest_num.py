def display(data):
    print(f"The largest number is {data}")
    
def get_input():
    a=int(input("enter a value:"))
    mx=a
    val='a'
    
    b=int(input("enter b value:"))
    if b>mx:
        mx=b
        val='b'
        
    c=int(input("enter c value:"))
    if c>mx:
        mx=c
        val='c'
    
    return(mx,val)

# def largest_val(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     elif b>a:
#         if b>c:
#             return b
#         else:
#             return c
        
def main():
    k=get_input()
    display(k)
main()