def get_input():
    n=int(input("Enter n:"))
    
    return n

def pattern(n):
    for i in range(1,n+1):
        print('*'*i)
        
def main():
    n=get_input()
    res=pattern(n)
    print(res)
    
main()