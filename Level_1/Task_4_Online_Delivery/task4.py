# ==========================================
# Cognifyz Internship - Level 1 Task 4
# Online Delivery Analysis
# ==========================================

# Import required libraries
import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset.csv")

# -------------------------------
# Display first few rows
# -------------------------------
print("\nFirst Five Rows:")
print(df.head())

# -------------------------------
# Count restaurants with and without online delivery
# -------------------------------
delivery_count = df["Has Online delivery"].value_counts()

print("\nRestaurants with and without Online Delivery:")
print(delivery_count)

# -------------------------------
# Calculate percentage
# -------------------------------
delivery_percentage = (
    df["Has Online delivery"]
    .value_counts(normalize=True) * 100
)

print("\nPercentage of Restaurants:")
print(delivery_percentage.round(2))

# -------------------------------
# Calculate average ratings
# -------------------------------
average_ratings = (
    df.groupby("Has Online delivery")["Aggregate rating"]
    .mean()
    .round(2)
)

print("\nAverage Ratings:")
print(average_ratings)

# -------------------------------
# Save results to CSV
# -------------------------------
result = pd.DataFrame({
    "Restaurant Count": delivery_count,
    "Percentage (%)": delivery_percentage.round(2),
    "Average Rating": average_ratings
})

result.to_csv("Task4_Result.csv")

print("\nResult saved as Task4_Result.csv")