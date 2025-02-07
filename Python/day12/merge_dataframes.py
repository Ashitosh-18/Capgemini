import pandas as pd

sales_data = {
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000]
}

sales_df = pd.DataFrame(sales_data)

profit_data = {
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

profit_df = pd.DataFrame(profit_data)

# Merge based on common columns (Region, State, Year)
merged_df = pd.merge(sales_df, profit_df, on='State')

# Display merged DataFrame
print(merged_df,"\n")

merged_df = pd.merge(sales_df, profit_df, on='State', how='outer')
print(merged_df,"\n")

merged_df = pd.merge(sales_df, profit_df, on='State', how='left')
print(merged_df,"\n")

merged_df = pd.merge(sales_df, profit_df, on='State', how='right')
print(merged_df,"\n")

