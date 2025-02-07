import pandas as pd

data = []

n=int(input("Enter the number of customers you want insert"))

for i in range(n):
    print(f"\nEnter details for customer {i+1}:")
    customer_id = input("Customer ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    country = input("Country: ")

    # Append the data as a dictionary
    data.append({"Customer_ID": customer_id, "Name": name, "Age": age, "Email": email, "Country": country})

# Convert list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("text_tocsv_topandas.csv", index=False)

print("\nCSV file 'text_tocsv_topandas.csv' created successfully!")

# Read the CSV file into a DataFrame
df_new = pd.read_csv("text_tocsv_topandas.csv")

# Print the data
print("\nData read from 'text_tocsv_topandas.csv':")
print(df_new)
