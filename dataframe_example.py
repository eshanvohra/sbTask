# DataFrames in Python (using pandas)
# A DataFrame is a 2-dimensional labeled data structure with columns that can be of different types

import pandas as pd
import numpy as np

print("=== DataFrame Basics ===\n")

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}

df = pd.DataFrame(data)
print("1. Basic DataFrame:")
print(df)
print("\nDataFrame shape:", df.shape)
print("DataFrame columns:", df.columns.tolist())
print("DataFrame data types:")
print(df.dtypes)

print("\n=== Accessing Data ===")

# Accessing specific columns
print("\n2. Accessing columns:")
print("Names:", df['Name'].tolist())
print("Ages:", df['Age'].tolist())

# Accessing specific rows
print("\n3. Accessing rows:")
print("First row:")
print(df.iloc[0])
print("\nLast row:")
print(df.iloc[-1])

# Accessing specific cells
print("\n4. Accessing specific cells:")
print("Age of Alice:", df.loc[0, 'Age'])
print("Salary of Bob:", df.loc[1, 'Salary'])

print("\n=== Filtering and Selection ===")

# Filtering data
print("\n5. People older than 30:")
older_than_30 = df[df['Age'] > 30]
print(older_than_30)

print("\n6. People with salary > 60000:")
high_salary = df[df['Salary'] > 60000]
print(high_salary)

print("\n7. People from specific cities:")
ny_people = df[df['City'] == 'New York']
print(ny_people)

print("\n=== Basic Operations ===")

# Statistical operations
print("\n8. Statistical summary:")
print("Average age:", df['Age'].mean())
print("Average salary:", df['Salary'].mean())
print("Age statistics:")
print(df['Age'].describe())

# Adding new columns
print("\n9. Adding new columns:")
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
df['Salary_Category'] = df['Salary'].apply(lambda x: 'Low' if x < 55000 else 'High' if x > 65000 else 'Medium')
print(df)

print("\n=== Grouping and Aggregation ===")

# Grouping data
print("\n10. Grouping by Age_Group:")
grouped = df.groupby('Age_Group')
print("Average salary by age group:")
print(grouped['Salary'].mean())

print("\n11. Grouping by City:")
city_grouped = df.groupby('City')
print("Number of people per city:")
print(city_grouped.size())

print("\n=== Creating DataFrames from Different Sources ===")

# From a list of lists
print("\n12. DataFrame from list of lists:")
data_list = [
    ['Product A', 100, 10.50],
    ['Product B', 150, 15.75],
    ['Product C', 200, 8.25]
]
df_products = pd.DataFrame(data_list, columns=['Product', 'Quantity', 'Price'])
print(df_products)

# From CSV-like string
print("\n13. DataFrame from CSV string:")
csv_data = """Name,Department,Salary
John,IT,75000
Sarah,HR,65000
Mike,IT,80000
Lisa,Marketing,70000"""
df_csv = pd.read_csv(pd.StringIO(csv_data))
print(df_csv)

print("\n=== DataFrame Methods ===")

print("\n14. DataFrame info:")
print(df.info())

print("\n15. First 3 rows:")
print(df.head(3))

print("\n16. Last 2 rows:")
print(df.tail(2))

print("\n17. Sorting by Age (descending):")
print(df.sort_values('Age', ascending=False))

print("\n=== Handling Missing Data ===")

# Creating DataFrame with missing values
print("\n18. DataFrame with missing values:")
df_missing = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'Age': [25, 30, None, 28, 32],
    'City': ['NY', None, 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, None, 70000, 55000, 65000]
})
print(df_missing)

print("\n19. Checking for missing values:")
print(df_missing.isnull())

print("\n20. Filling missing values:")
df_filled = df_missing.fillna({'Name': 'Unknown', 'Age': 0, 'City': 'Unknown', 'Salary': 0})
print(df_filled)

print("\n=== Summary ===")
print("DataFrames are powerful for:")
print("- Data manipulation and analysis")
print("- Reading/writing various file formats (CSV, Excel, JSON, etc.)")
print("- Statistical operations and aggregations")
print("- Data cleaning and preprocessing")
print("- Integration with other data science libraries") 