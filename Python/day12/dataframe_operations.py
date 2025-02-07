import pandas as pd

# Creating DataFrame
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

df = pd.DataFrame(data)

# Set multi-index (without inplace=True)
df = df.set_index(['Region', 'State', 'Year'])

# Corrected lookup (Region should be 'South', not 'south')
sales_value = df.loc[('South', 'Tamil Nadu', 2021), 'Sales']

print(f"Sales in Tamil Nadu (2021): {sales_value}")



