import pandas as pd

# Create dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah', 'Ian', 'Jane'],
    'Age': [25, 30, 28, 35, 40, 29, 32, 31, 45, 38],
    'Gender': ['F','M','M','F','M','F','M','F','M','F'],
    'Department': ['HR','IT','Marketing','IT','HR','Marketing','IT','HR','Marketing','IT'],
    'YearsExperience': [2,5,3,10,15,4,7,6,20,12],
    'Salary': [40000, 55000, 45000, 80000, 90000, 48000, 65000, 60000, 120000, 95000]
}

df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("employee_data.csv", index=False)
print("Dataset created successfully")




# Full Code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 3: Load and View Dataset

# Check dataset structure, columns, and statistics.

# Full Code
df = pd.read_csv("employee_data.csv")

# View first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Shape and column names
print("\nDataset Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Step 4: Handle Missing Values


# Detect missing values and fill or drop them.


# Check missing values
print("Missing Values per Column:")
print(df.isnull().sum())

# Example: fill numeric with mean (if any missing)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Example: fill categorical with mode
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Department'].fillna(df['Department'].mode()[0], inplace=True)

print("After Handling Missing Values:")
print(df.isnull().sum())

# Step 5: Remove Duplicates

# Check duplicates
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
print("After Removing Duplicates:", df.shape)

# Step 6: Check Data Types and Convert if Needed

print("Data Types Before Conversion:")
print(df.dtypes)

# Convert YearsExperience to int (already int here)
df['YearsExperience'] = df['YearsExperience'].astype(int)

# Convert Salary to float
df['Salary'] = df['Salary'].astype(float)

print("\nData Types After Conversion:")
print(df.dtypes)

# Step 7: Descriptive Statistics

print(df.describe())

print("Mean Salary:", df['Salary'].mean())
print("Median Salary:", df['Salary'].median())
print("Mode Salary:", df['Salary'].mode()[0])

# Step 8: Univariate Analysis

# Age distribution
sns.histplot(df['Age'], kde=True, color='skyblue')
plt.title("Age Distribution")
plt.show()

# Salary distribution
sns.histplot(df['Salary'], kde=True, color='green')
plt.title("Salary Distribution")
plt.show()

# Gender count
sns.countplot(x='Gender', data=df)
plt.title("Gender Count")
plt.show()

# Department count
sns.countplot(x='Department', data=df)
plt.title("Department Count")
plt.show()

# Step 9: Bivariate Analysis

# Age vs Salary
sns.scatterplot(x='Age', y='Salary', hue='Gender', data=df)
plt.title("Age vs Salary")
plt.show()

# Department vs Salary
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title("Salary by Department")
plt.show()

# Step 10: Correlation

numeric_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix (Numeric Columns)")
plt.show()


# Step 11: Outlier Detection and Handling

# Detect outliers in Salary
sns.boxplot(x=df['Salary'])
plt.title("Salary Outlier Detection")
plt.show()

# Remove outliers using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Salary'] >= Q1 - 1.5*IQR) & (df['Salary'] <= Q3 + 1.5*IQR)]
print("After removing outliers, Dataset Shape:", df.shape)

# Step 12: Trend and Pattern Analysis

# Average Salary by Department
sns.barplot(x='Department', y='Salary', data=df, palette='Set1')
plt.title("Average Salary by Department")
plt.show()

# YearsExperience vs Salary
sns.lineplot(x='YearsExperience', y='Salary', data=df, marker='o')
plt.title("Experience vs Salary")
plt.show()

# Step 13: Summary Insights

# Average salary by department
avg_salary_dept = df.groupby('Department')['Salary'].mean()
print("Average Salary by Department:\n", avg_salary_dept)

# Average salary by gender
avg_salary_gender = df.groupby('Gender')['Salary'].mean()
print("\nAverage Salary by Gender:\n", avg_salary_gender)
