import pandas as pd

data={
    'Name':['Alice','Bob'],
    'Age':['25','30'],
    'City':['New York','Los Angeles']
}

df=pd.DataFrame(data)
print(df)