# ==========================================
# Cognifyz Internship
# Level 2 - Task 3
# Geographic Analysis
# ==========================================

# Import required libraries
import pandas as pd
import folium

# -------------------------------
# Load the dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# Display first five rows
print("\nFirst Five Rows:")
print(df.head())

# -------------------------------
# Calculate center of the map
# -------------------------------
center_lat = df["Latitude"].mean()
center_long = df["Longitude"].mean()

# Create map
restaurant_map = folium.Map(
    location=[center_lat, center_long],
    zoom_start=5
)

# -------------------------------
# Add restaurant locations
# -------------------------------
for _, row in df.iterrows():

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=3,
        popup=f"{row['Restaurant Name']}<br>Rating: {row['Aggregate rating']}",
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6
    ).add_to(restaurant_map)

# -------------------------------
# Save map
# -------------------------------
restaurant_map.save("Restaurant_Locations_Map.html")

print("\nInteractive map saved as Restaurant_Locations_Map.html")

# -------------------------------
# Restaurant count by city
# -------------------------------
city_counts = (
    df["City"]
    .value_counts()
)

print("\nTop 10 Cities with Most Restaurants:\n")
print(city_counts.head(10))

# -------------------------------
# Save results
# -------------------------------
city_counts.head(10).to_csv(
    "Task3_Result.csv",
    header=["Restaurant Count"]
)

print("\nResult saved as Task3_Result.csv")