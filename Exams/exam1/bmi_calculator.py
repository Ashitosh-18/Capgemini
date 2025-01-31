def get_input():
    wt=int(input("enter your weight:"))
    ht=float(input("enter your height:"))
    
    return(wt,ht)

def bmi_cal(wt,ht):
    val=wt/(ht**2)
    return val

def main():
    while True:
        wt,ht=get_input()
        res=bmi_cal(wt,ht)
        
        if res<18.5:
            print ("You are under weight")
        
        if 18.5<res<24.9:
            print ("you are normal")
        
        if res>24.9:
            print ("you are overvweight")
        
        k=input("do you want calculate again press yes/no:")
        if k!='yes':
            break
        
        
main()
    