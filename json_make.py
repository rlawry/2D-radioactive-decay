import pandas as pd
import json

# Input CSV file (from previous processing step)
input_csv = "unstable_nuclides.csv"
output_json = "unstable_nuclides.json"

# Load the CSV
df = pd.read_csv(input_csv)

# Convert to list of dictionaries
data = df.to_dict(orient="records")

# Write to JSON
with open(output_json, "w") as f:
    json.dump(data, f, indent=2)

print(f"Saved JSON output to {output_json}")
