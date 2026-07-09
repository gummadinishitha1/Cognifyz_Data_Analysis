# ==========================================
# Cognifyz Internship
# Level 2 - Task 1
# Restaurant Ratings Analysis
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
# Distribution of Aggregate Ratings
# -------------------------------
rating_counts = df["Aggregate rating"].value_counts().sort_index()

print("\nDistribution of Aggregate Ratings:")
print(rating_counts)

# -------------------------------
# Most Common Rating
# -------------------------------
most_common_rating = df["Aggregate rating"].mode()[0]

print(f"\nMost Common Rating: {most_common_rating}")

# -------------------------------
# Average Number of Votes
# -------------------------------
average_votes = df["Votes"].mean()

print(f"\nAverage Number of Votes: {average_votes:.2f}")

# -------------------------------
# Save Results
# -------------------------------
result = pd.DataFrame({
    "Rating": rating_counts.index,
    "Restaurant Count": rating_counts.values
})

result.to_csv("Task1_Result.csv", index=False)

print("\nResult saved as Task1_Result.csv")

# -------------------------------
# Histogram
# -------------------------------
plt.figure(figsize=(8,5))

plt.hist(
    df["Aggregate rating"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")

plt.grid(alpha=0.3)

plt.savefig("Aggregate_Rating_Distribution.png")

plt.show()

print("Chart saved as Aggregate_Rating_Distribution.png")