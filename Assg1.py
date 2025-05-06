import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('nba.csv')

# print(df.shape)
# print(df.size)
# print(df.columns)
# print(df.head(5))
# print(df.tail(5))
# print(df.describe)
# des = df.describe(include=['float'])
# print(np.round(des , 2))
# print(df.dtypes)
# print(df['Age'].value_counts())
# print(df[['Height','Weight']].value_counts())
# print(df.isnull())
# print(df.isnull().sum())


# df.plot.bar(figsize=(20, 8), color="lightcoral")
# # Show the plot (for interactive environments) or save it if you're in terminal
# plt.title("Your Plot Title")
# plt.xlabel("X Axis Label")
# plt.ylabel("Y Axis Label")
# plt.tight_layout()
# plt.savefig("bar_plot.png")


# missing_values = (
#     df.isnull().sum().sort_values(ascending=False)
# )  # Sort missing values in descending order
# missing_df = pd.concat(
#     [missing_values], axis=1, keys=["Total"]
# )  # Create a summary DataFrame
# print(missing_df.head())

# missing_df.head(10).plot(kind='bar')
# plt.title("Top Missing Values in Columns")
# plt.xlabel("Column Name")
# plt.ylabel("Number of Missing Values")
# plt.tight_layout()
# plt.show()
# plt.savefig("missing_values.png")


# missing = df.isna().sum()
# missing.plot.bar(
#     figsize=(10, 5), color="lightgreen", edgecolor="black"
# )  # Plot missing values

# plt.savefig("ace.png")

print(df.shape)
# Handling missing values
df = df.dropna()  # Drop rows with missing values
df = df.copy()
mean_salary = df["Salary"].mean()  # Calculate mean salary
df["Salary"] = df["Salary"].fillna(mean_salary)
print("Null values after update: ", df["Salary"].isnull().sum())
print(df.isna().sum())  # Check remaining missing values
print(df.shape)

df = df.copy()
df["Height"] = pd.to_numeric(df["Height"].str.replace("-", ""), errors="coerce")

# Check for any missing values after cleaning
print(df["Height"].isnull().sum())

# Convert numerical columns to integers
df["Number"] = pd.to_numeric(df["Number"], errors="coerce").fillna(0).astype(int)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0).astype(int)
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce").fillna(0).astype(int)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce").fillna(0).astype(int)

# Convert categorical columns to 'category' type
df["Team"] = df["Team"].astype("category")
df["Position"] = df["Position"].astype("category")
df["College"] = df["College"].astype("category")

# Check the updated data types and any missing values
print(df.isnull().sum())

df.info()
df = df.copy()  # Check data types after conversion
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")