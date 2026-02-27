# ==========================================
# DSA0423 – Activity 1
# School Cafeteria Survey (IDLE Version)
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV File
file_name = r"C:\Users\rohan\Desktop\cafeteria_survey_raw.csv"

df = pd.read_csv(file_name)

print("\n===== RAW DATA =====")
print(df.head())

print("\nDataset Shape:", df.shape)

# ------------------------------------------
# Step 2: Data Cleaning
# ------------------------------------------

# Standardize column name
df.columns = df.columns.str.strip()

column_name = df.columns[0]

# Convert to string, remove extra spaces, convert to lowercase
df[column_name] = df[column_name].astype(str).str.strip().str.lower()

# Fix common spelling errors
df[column_name] = df[column_name].replace({
    "chiken burger": "chicken burger",
    "pasta sald": "pasta salad",
    "veg wrap": "veggie wrap",
    "veggiewrap": "veggie wrap",
    "chickenburger": "chicken burger",
    "pastasalad": "pasta salad"
})

# Remove extra internal spaces
df[column_name] = df[column_name].str.replace(r"\s+", " ", regex=True)

# Convert to Title Case
df[column_name] = df[column_name].str.title()

# Remove duplicates (optional)
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

print("\n===== CLEANED DATA =====")
print(df.head())

# ------------------------------------------
# Step 3: Count Preferences
# ------------------------------------------

dish_counts = df[column_name].value_counts()

print("\n===== DISH PREFERENCE COUNTS =====")
print(dish_counts)

# ------------------------------------------
# Step 4: Save Cleaned File
# ------------------------------------------

df.to_csv("cleaned_cafeteria_survey.csv", index=False)
print("\nCleaned file saved as: cleaned_cafeteria_survey.csv")

# ------------------------------------------
# Step 5: Bar Chart Visualization
# ------------------------------------------

plt.figure()
dish_counts.plot(kind='bar')
plt.title("Cafeteria Menu Preference Survey")
plt.xlabel("Dish")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== ACTIVITY COMPLETED SUCCESSFULLY =====")
