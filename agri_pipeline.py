import pandas as pd

# --- 1. EXTRACTION ---
print("--- Extraction Phase ---")
# Loading our two separate data sources
yield_df = pd.read_csv('crop_yields.csv')
weather_df = pd.read_csv('weather_data.csv')

print("Yield and Weather data loaded successfully.")

# --- 2. TRANSFORMATION (THE JOIN) ---
print("\n--- Transformation Phase: Joining Data ---")

# We link the files on 'Year' and 'Region'
# This is like saying: "Find where 2024 Midwest exists in both files and put them together."
merged_df = pd.merge(yield_df, weather_df, on=['Year', 'Region'])

print("Data successfully joined into a single schema.")
print(merged_df)

# --- 3. FEATURE ENGINEERING ---
print("\n--- Engineering New Metrics ---")

# Creating a new column by dividing Yield by Rainfall
merged_df['Yield_Efficiency'] = merged_df['Yield_Tons'] / merged_df['Rainfall_mm']

# Rounding for a cleaner report
merged_df['Yield_Efficiency'] = merged_df['Yield_Efficiency'].round(4)

print("Yield Efficiency metric calculated.")
print(merged_df[['Year', 'Region', 'Crop', 'Yield_Efficiency']])

# --- 4. LOADING & PARTITIONING ---
print("\n--- Loading Phase ---")

# Save the final analytical table
merged_df.to_csv('master_agri_data.csv', index=False)

# Provide a summary report for stakeholders
# This shows the average efficiency per Region
summary = merged_df.groupby('Region')['Yield_Efficiency'].mean()

print("SUCCESS: Data loaded into 'master_agri_data.csv'")
print("\n--- Business Insight Summary ---")
print("Average Yield Efficiency by Region:")
print(summary)