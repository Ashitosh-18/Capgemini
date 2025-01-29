def max_min(l1):
    max_elem=float('-inf')      
    min_elem=float('inf')
    
    for i in l1:
        if i>max_elem:
            max_elem=i
        if i<min_elem:
            min_elem=i
            
    return max_elem,min_elem

def main():
    l1=list(map(int,input("enter the elements:").split()))
    max_elem,min_elem=max_min(l1)
    print(f"max element is {max_elem}, min element is {min_elem}")
main()

# def maxx(l1):
#     max_elem=float('-inf')      
    
#     for i in l1:
#         if i>max_elem:
#             max_elem=i
            
#     return max_elem
    
# def minn(l1):
#     min_elem=float('inf')
    
#     for i in l1:
#         if i<min_elem:
#             min_elem=i
            
#     return min_elem
          
    

# def main():
#     l1=list(map(int,input("enter the elements:").split()))
#     res1=maxx(l1)
#     print("Maximum element is :",res1)
#     res2=minn(l1)
#     print("Minimum element is:",res2)
# main()