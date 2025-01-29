import dis
a=4
b=5
def sum():
    sum=a+b
    return sum

def diff():
    diff=a-b
    return diff

def multi():
    multi=a*b
    return multi

def div():
    div=a/b
    return div

def forloop():
    for i in range (0,5):
        return i

def main():
    dis.dis(sum)
    dis.dis(diff)
    dis.dis(multi)
    dis.dis(div)
    dis.dis(forloop)
    
main()