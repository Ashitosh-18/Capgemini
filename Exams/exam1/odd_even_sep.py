def odd_even_split(nums):
    odd_num=[]
    even_num=[]
    
    for i in nums:
        if i%2==0:
            even_num.append(i)
            
        else:
            odd_num.append(i)
            
    return odd_num,even_num

def main():
    nums=list(map(int,input("enter the numbers with space b/w :").split()))
    odd,even=odd_even_split(nums)
    print(f"odd values are{odd} and even values are{even}")
    
main()