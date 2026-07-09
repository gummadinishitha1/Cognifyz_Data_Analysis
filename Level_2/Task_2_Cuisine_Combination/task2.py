# ==========================================
# Cognifyz Internship
# Level 2 - Task 2
# Cuisine Combination Analysis
# ==========================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Dataset.csv")

# -------------------------------
# Display first five rows
# -------------------------------
print("\nFirst Five Rows:")
print(df.head())

# -------------------------------
# Most Common Cuisine Combinations
# -------------------------------
cuisine_counts = (
    df["Cuisines"]
    .value_counts()
    .head(10)
)

print("\nTop 10 Most Common Cuisine Combinations:")
print(cuisine_counts)

# -------------------------------
# Average Rating for Each Cuisine Combination
# -------------------------------
average_ratings = (
    df.groupby("Cuisines")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Cuisine Combinations with Highest Average Ratings:")
print(average_ratings.round(2))

# -------------------------------
# Save Results
# -------------------------------
result = pd.DataFrame({
    "Cuisine Combination": cuisine_counts.index,
    "Restaurant Count": cuisine_counts.values
})

result.to_csv("Task2_Result.csv", index=False)

print("\nResult saved as Task2_Result.csv")

# -------------------------------
# Bar Chart
# -------------------------------
plt.figure(figsize=(12,6))

plt.bar(
    cuisine_counts.index,
    cuisine_counts.values
)

plt.title("Top 10 Most Common Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("Cuisine_Combination.png")

plt.show()

print("Chart saved as Cuisine_Combination.png")