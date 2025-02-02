import csv

filename = "data.csv"

# Open file in write mode initially & add a header
with open(filename,"w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Value1", "Value2", "Value3"])  # Header row

# Open file in append mode to keep adding new rows
with open(filename,"a",newline="") as file:
    writer = csv.writer(file)

    while True:
        val1 = input("Enter first value: ")
        val2 = input("Enter second value: ")
        val3 = input("Enter third value: ")
        
        # Write values to the file
        writer.writerow([val1, val2, val3])
        
        cont = input("Do you want to enter more data? (yes/no): ")
        if cont != "yes":
            break

print(f"Data saved in {filename}")
