# ==========================================
# Cognifyz Internship
# Level 2 - Task 4
# Restaurant Chains Analysis
# ==========================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load the dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# -------------------------------
# Identify Restaurant Chains
# -------------------------------
chain_counts = df["Restaurant Name"].value_counts()

restaurant_chains = chain_counts[chain_counts > 1]

print("\nTop 10 Restaurant Chains:")
print(restaurant_chains.head(10))

# -------------------------------
# Analyze Ratings and Popularity
# -------------------------------
chain_analysis = (
    df.groupby("Restaurant Name")
    .agg({
        "Aggregate rating": "mean",
        "Votes": "mean"
    })
    .rename(columns={
        "Aggregate rating": "Average Rating",
        "Votes": "Average Votes"
    })
)

chain_analysis = chain_analysis.loc[restaurant_chains.index]
chain_analysis = chain_analysis.sort_values(
    by="Average Rating",
    ascending=False
)

print("\nTop Restaurant Chains by Average Rating:")
print(chain_analysis.head(10))

# -------------------------------
# Save Results
# -------------------------------
chain_analysis.to_csv("Task4_Result.csv")

print("\nResult saved as Task4_Result.csv")

# -------------------------------
# Plot Top 10 Chains
# -------------------------------
top10 = restaurant_chains.head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top10.index,
    top10.values
)

plt.title("Top 10 Restaurant Chains")
plt.xlabel("Restaurant Chain")
plt.ylabel("Number of Outlets")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("Restaurant_Chains.png")

plt.show()

print("Chart saved as Restaurant_Chains.png")