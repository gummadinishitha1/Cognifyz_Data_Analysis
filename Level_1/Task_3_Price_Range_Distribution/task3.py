# ==========================================
# Cognifyz Internship - Level 1 Task 3
# Price Range Distribution
# ==========================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv("Dataset.csv")

# -------------------------------
# Display first few rows
# -------------------------------
print("\nFirst Five Rows:")
print(df.head())

# -------------------------------
# Count restaurants in each price range
# -------------------------------
price_counts = df["Price range"].value_counts().sort_index()

print("\nRestaurant Count in Each Price Range:")
print(price_counts)

# -------------------------------
# Calculate percentage
# -------------------------------
price_percentage = (
    df["Price range"]
    .value_counts(normalize=True)
    .sort_index() * 100
)

print("\nPercentage of Restaurants in Each Price Range:")
print(price_percentage.round(2))

# -------------------------------
# Save results to CSV
# -------------------------------
result = pd.DataFrame({
    "Restaurant Count": price_counts,
    "Percentage (%)": price_percentage.round(2)
})

result.to_csv("Task3_Result.csv")

print("\nResult saved as Task3_Result.csv")

# -------------------------------
# Create Bar Chart
# -------------------------------
plt.figure(figsize=(8,5))

plt.bar(
    price_counts.index.astype(str),
    price_counts.values
)

plt.title("Distribution of Restaurants by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.savefig("Price_Range_Distribution.png")

plt.show()

print("\nChart saved as Price_Range_Distribution.png")