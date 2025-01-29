def display(data):
    print(f"The avg of four numbers is {data}")
    
def get_input():
    first=int(input("enter first no:"))
    second=int(input("enter second no:"))
    third=int(input("enter third no:"))
    fourth=int(input("enter fourth no:"))
    
    return(first,second,third,fourth)

def com_avg(n1,n2,n3,n4):
    avg=(n1+n2+n3+n4)/4
    return avg
    
def main():
    (n1,n2,n3,n4)=get_input()
    avg=com_avg(n1,n2,n3,n4)
    display(avg)
main()
    