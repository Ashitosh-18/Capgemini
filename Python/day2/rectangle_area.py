def display(data):
    print(f"the area is {data}")
    
def get_input():
    received_len=input("length:")
    received_wid=input("Width:")
    
    return(received_len,received_wid)

def com_area(len,wid):
    area=int(len)*int(wid)
    return area

def main():
    (len,wid)=get_input()
    area=com_area(len,wid)
    display(area)
    
main()
    