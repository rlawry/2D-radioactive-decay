import requests
import json

url = "https://nds.iaea.org/relnsd/v1/data"
params = {
    "fields": "z,a,element,half_life,state",
    "nuclides": "all"
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

# Debug: print what the response looks like
print(f"First few records: {data[:3]}")  # optional sanity check

# Save to file
with open("nuclides_raw.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved nuclides_raw.json")
