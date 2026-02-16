import pandas as pd
import numpy as np

file_path = 'data.txt'
data = pd.read_csv(
    file_path,
    sep='|',
    encoding='latin-1',
    engine='python',
    on_bad_lines='skip'
)


print("Data loaded successfully!")
print(data.shape)
print(data.head())
print(data.columns)
print(data.info())

data.columns = data.columns.str.strip()
data.columns = data.columns.str.upper()
data.columns = data.columns.str.replace(' ', '_')
print("Columns after cleaning:")
print(data.columns)
print(list(data.columns))
data=data.dropna(how="all")

important_cols= [
    
    'ACCIDENT_TYPE',
    'DEGREE_INJURY',
    'DAYS_LOST',
    'ACCIDENT_DT',
    'UG_LOCATION'
]
data = data.dropna(subset=[
    'ACCIDENT_TYPE',
    'DEGREE_INJURY'
])



data['ACCIDENT_DT'] = pd.to_datetime(data['ACCIDENT_DT'], errors='coerce')
data['YEAR'] = data['ACCIDENT_DT'].dt.year
data['DAYS_LOST'] = pd.to_numeric(data['DAYS_LOST'], errors='coerce')
data_small=data.sample(n=5000, random_state=42)
print(data_small.isnull().sum())
print(data_small.describe())

data_small.to_csv('cleaned_msha_mining_data.csv', index=False)
print("Cleaned data saved to 'cleaned_msha_mining_data.csv'")

import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))

data_small['UG_LOCATION'].value_counts().plot(kind='bar')

plt.title("Accidents by Underground Location")
plt.xlabel("Underground Location")
plt.ylabel("Number of Accidents")

plt.xticks(rotation=45, ha='right')   # 🔥 Important
plt.tight_layout()                    # 🔥 Important

plt.show()



plt.figure(figsize=(12,6))

data_small['ACCIDENT_TYPE'].value_counts().head(10).plot(kind='bar')

plt.title("Top Accident Types")
plt.xlabel("Accident Type")
plt.ylabel("Number of Accidents")

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()


data_small['YEAR'].value_counts().sort_index().plot()
plt.title("Accident Trend Over Years")
plt.show()




