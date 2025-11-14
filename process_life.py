import pandas as pd

# Load the LiveChart CSV file (replace with your actual path if needed)
input_file = "livechart.csv"  # <-- Rename your file accordingly
output_file = "unstable_nuclides.csv"

# Read the CSV
df = pd.read_csv(input_file)

# Ensure required columns exist
required_columns = {'z', 'n', 'symbol', 'half_life_sec'}
if not required_columns.issubset(df.columns):
    raise ValueError(f"CSV missing one of the required columns: {required_columns}")

# Filter rows with non-null half-lives
df_filtered = df[df['half_life_sec'].notnull()].copy()

# Compute Mass as Z + N
df_filtered['Mass'] = df_filtered['z'] + df_filtered['n']

# Create new DataFrame with required columns
result = df_filtered[['Mass', 'symbol', 'half_life_sec']].rename(
    columns={'symbol': 'Symbol', 'half_life_sec': 'half-life'}
)

# Save to new CSV
result.to_csv(output_file, index=False)
print(f"Saved filtered data to {output_file}")