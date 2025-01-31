def get_input():
    salary=int(input("enter your salary:"))
    age=int(input("enter your age:"))
    credit_score=int(input("enter your credit score:"))
    
    return(salary,age,credit_score)

def eligibility(salary,age,credit_score):
    if salary<20000:
        return "Loan rejected : Your salary must be above 20000"
    
    elif age<18:
        return "Loan rejected : You must be 18 years or older"
    
    elif credit_score<700:
        return "Loan rejected : Your credit score must be above 700"
    
    else:
        return "Loan approved"
    
def main():
    s,a,c=get_input()
    ans=eligibility(s,a,c)
    print(ans)
    
main()
        
    
    