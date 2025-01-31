def second_lar(nums):
    nums.sort(reverse=True)
    return nums

def main():
    nums=list(map(int,input("enter the numbers with space:").split()))
    res=second_lar(nums)
    print(res[1])
    
main()