file=open("sample.txt","w")  # open file in write mode

file.write("Hello, this is a sample text")  # write data

file.close()  #close file

# Reading the entire file
with open("sample.txt","r") as file:
    content=file.read()
    print(content)
    
# Reading line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())
    