import pandas as pd
# Creating a dictionary with sample data
data = {
    "Customer_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 28],
    "Email": ["alice@example.com", "bob@example.com", "charlie@example.com", "david@example.com", "eve@example.com"],
    "Country": ["USA", "Canada", "UK", "Germany", "India"],
    "Purchase_Amount": [250.75, 300.50, 120.00, 500.00, 450.25]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
# Save to a new CSV file
df.to_csv("new_customers.csv", index=False)

print("CSV file 'new_customers.csv' created successfully!")

# Read the newly created CSV file
df_new = pd.read_csv("new_customers.csv")
print(df_new)
