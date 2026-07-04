import pandas as pd

# -----------------------------
# Read the dataset
# -----------------------------
df = pd.read_csv("Dataset.csv")

# -----------------------------
# Display first 5 rows
# -----------------------------
print("First 5 Rows of the Dataset:\n")
print(df.head())

# -----------------------------
# Display column names
# -----------------------------
print("\nColumn Names:\n")
print(df.columns)

# ====================================================
# Task 1: City with the Highest Number of Restaurants
# ====================================================

city_counts = df["City"].value_counts()

print("\n==========================================")
print("City with the Highest Number of Restaurants")
print("==========================================")
print(city_counts.head(1))

# ====================================================
# Task 2: Average Rating for Restaurants in Each City
# ====================================================

average_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)

print("\n==========================================")
print("Average Restaurant Rating by City")
print("==========================================")
print(average_rating)

# ====================================================
# Task 3: City with the Highest Average Rating
# ====================================================

highest_rating_city = average_rating.head(1)

print("\n==========================================")
print("City with the Highest Average Rating")
print("==========================================")
print(highest_rating_city)

# ====================================================
# Save Results to CSV
# ====================================================

result = pd.DataFrame({
    "Average Rating": average_rating
})

result.to_csv("City_Analysis_Result.csv")

print("\n==========================================")
print("Results saved successfully!")
print("File Name: City_Analysis_Result.csv")
print("==========================================")