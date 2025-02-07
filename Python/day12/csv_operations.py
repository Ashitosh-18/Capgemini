import pandas as pd

csv_df = pd.read_csv(r"C:\Users\Ashitoshabhi\OneDrive\Desktop\Capgemini\Python\day12\customers-100.csv")
print(csv_df)

csv_df.to_json("customer.JSON",orient="records",indent=4)
df_sorted = csv_df.sort_values(by="First Name", ascending=False)
print(df_sorted)

print(csv_df.head())   # First 5 rows
print(csv_df.tail())   # Last 5 rows
print(csv_df.sample(5))  # Random 5 rows
print(csv_df.info())   # Summary of dataset
print(csv_df.describe())  # Statistical summary
print(csv_df.shape)    # (rows, columns)
print(csv_df.columns)  # List of column names


print(csv_df["First Name"])  # Selecting a single column
print(csv_df[["First Name", "Email"]])  # Selecting multiple columns
print(csv_df.iloc[0])  # Selecting the first row
print(csv_df.iloc[0:5])  # Selecting first 5 rows
print(csv_df.loc[csv_df["Country"] == "Sri Lanka"])  # Filter by country



# csv_csv_df.to_csv('output.csv',Index=False)