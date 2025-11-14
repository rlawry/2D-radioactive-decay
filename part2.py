import json

with open("nuclides_raw.json") as f:
    raw = json.load(f)

filtered = []
for n in raw:
    if n.get("state", "").strip().lower() != "g":
        continue
    try:
        z = int(n["z"])
        a = int(n["a"])
        hl = float(n["half_life"])
        if hl <= 0:
            continue
        name = f"{n['element'].lower()}-{a}"
        filtered.append({"name": name, "half-life": hl})
    except:
        continue

filtered.sort(key=lambda x: x["name"])

with open("nuclides_list.txt", "w") as f:
    f.write("var nuclides;\nnuclides = {\"nuclides\": [\n")
    for nuclide in filtered:
        f.write(f"    {{\"name\": \"{nuclide['name']}\", \"half-life\": {nuclide['half-life']}}},\n")
    if filtered:
        f.seek(f.tell() - 2)
    f.write("\n]};\n")

print("Finished: nuclides_list.txt")
