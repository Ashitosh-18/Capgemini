def find_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0) :
        return True
    
    else:
        return False
    
def main():
    while True:
        year=int(input("enter a year:"))
        ans=find_leap(year)
        if ans==True:
            print("It is a Leap year")
            
        else:
            print("Not a Leap year")
            
        k=input("you want to continue:yes/no ")
        if k!='yes':
            break
    
main()
        