import pandas as pd

# Read the dataset
df = pd.read_csv("Dataset.csv")

# Split cuisines into a list
all_cuisines = df["Cuisines"].str.split(",")

# Store each cuisine separately
cuisine_list = []

for cuisines in all_cuisines:
    if isinstance(cuisines, list):
        for cuisine in cuisines:
            cuisine_list.append(cuisine.strip())

# Count each cuisine
cuisine_counts = pd.Series(cuisine_list).value_counts()

# Get the top 3 cuisines
top3 = cuisine_counts.head(3)

# Total number of restaurants
total_restaurants = len(df)

print("Top 3 Most Common Cuisines\n")

for cuisine, count in top3.items():
    percentage = (count / total_restaurants) * 100

    print(f"Cuisine: {cuisine}")
    print(f"Restaurants: {count}")
    print(f"Percentage: {percentage:.2f}%")
    print("-" * 30)
# ==========================================
# Cognifyz Technologies Internship
# Level 1 - Task 1
# Top Cuisines Analysis
# ==========================================

import pandas as pd

# -------------------------------
# Step 1: Load the dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# Step 2: Display dataset information
# -------------------------------
print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal Restaurants: {len(df)}")

print("\nColumns in Dataset:")
print(df.columns)

# -------------------------------
# Step 3: Remove missing cuisine values
# -------------------------------
df = df.dropna(subset=["Cuisines"])

# -------------------------------
# Step 4: Split multiple cuisines
# -------------------------------
all_cuisines = df["Cuisines"].str.split(",")

# -------------------------------
# Step 5: Store every cuisine separately
# -------------------------------
cuisine_list = []

for cuisines in all_cuisines:
    for cuisine in cuisines:
        cuisine_list.append(cuisine.strip())

# -------------------------------
# Step 6: Count each cuisine
# -------------------------------
cuisine_counts = pd.Series(cuisine_list).value_counts()

# -------------------------------
# Step 7: Display Top 3 Cuisines
# -------------------------------
print("\n")
print("=" * 60)
print("TOP 3 MOST COMMON CUISINES")
print("=" * 60)

top3 = cuisine_counts.head(3)

for i, (cuisine, count) in enumerate(top3.items(), start=1):
    print(f"{i}. {cuisine} - {count} Restaurants")

# -------------------------------
# Step 8: Calculate Percentage
# -------------------------------
print("\n")
print("=" * 60)
print("PERCENTAGE OF RESTAURANTS SERVING TOP CUISINES")
print("=" * 60)

total_restaurants = len(df)

result = []

for cuisine, count in top3.items():

    percentage = (count / total_restaurants) * 100

    print(f"\nCuisine : {cuisine}")
    print(f"Restaurants : {count}")
    print(f"Percentage : {percentage:.2f}%")

    result.append({
        "Cuisine": cuisine,
        "Restaurants": count,
        "Percentage": round(percentage, 2)
    })

# -------------------------------
# Step 9: Save Result to CSV
# -------------------------------
result_df = pd.DataFrame(result)

result_df.to_csv("Top_3_Cuisines_Result.csv", index=False)

print("\n")
print("=" * 60)
print("Result saved successfully!")
print("File Name: Top_3_Cuisines_Result.csv")
print("=" * 60)