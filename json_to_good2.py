import json

# Input JSON file and output TXT file
input_json = "unstable_nuclides.json"
output_txt = "nuclides_list.txt"

# Periodic table symbol to full name
symbol_to_name = {
    "h": "hydrogen", "he": "helium", "li": "lithium", "be": "beryllium", "b": "boron",
    "c": "carbon", "n": "nitrogen", "o": "oxygen", "f": "fluorine", "ne": "neon",
    "na": "sodium", "mg": "magnesium", "al": "aluminium", "si": "silicon", "p": "phosphorus",
    "s": "sulfur", "cl": "chlorine", "ar": "argon", "k": "potassium", "ca": "calcium",
    "sc": "scandium", "ti": "titanium", "v": "vanadium", "cr": "chromium", "mn": "manganese",
    "fe": "iron", "co": "cobalt", "ni": "nickel", "cu": "copper", "zn": "zinc",
    "ga": "gallium", "ge": "germanium", "as": "arsenic", "se": "selenium", "br": "bromine",
    "kr": "krypton", "rb": "rubidium", "sr": "strontium", "y": "yttrium", "zr": "zirconium",
    "nb": "niobium", "mo": "molybdenum", "tc": "technetium", "ru": "ruthenium", "rh": "rhodium",
    "pd": "palladium", "ag": "silver", "cd": "cadmium", "in": "indium", "sn": "tin",
    "sb": "antimony", "te": "tellurium", "i": "iodine", "xe": "xenon", "cs": "caesium",
    "ba": "barium", "la": "lanthanum", "ce": "cerium", "pr": "praseodymium", "nd": "neodymium",
    "pm": "promethium", "sm": "samarium", "eu": "europium", "gd": "gadolinium", "tb": "terbium",
    "dy": "dysprosium", "ho": "holmium", "er": "erbium", "tm": "thulium", "yb": "ytterbium",
    "lu": "lutetium", "hf": "hafnium", "ta": "tantalum", "w": "tungsten", "re": "rhenium",
    "os": "osmium", "ir": "iridium", "pt": "platinum", "au": "gold", "hg": "mercury",
    "tl": "thallium", "pb": "lead", "bi": "bismuth", "po": "polonium", "at": "astatine",
    "rn": "radon", "fr": "francium", "ra": "radium", "ac": "actinium", "th": "thorium",
    "pa": "protactinium", "u": "uranium", "np": "neptunium", "pu": "plutonium", "am": "americium",
    "cm": "curium", "bk": "berkelium", "cf": "californium", "es": "einsteinium", "fm": "fermium",
    "md": "mendelevium", "no": "nobelium", "lr": "lawrencium", "rf": "rutherfordium",
    "db": "dubnium", "sg": "seaborgium", "bh": "bohrium", "hs": "hassium", "mt": "meitnerium",
    "ds": "darmstadtium", "rg": "roentgenium", "cn": "copernicium", "nh": "nihonium",
    "fl": "flerovium", "mc": "moscovium", "lv": "livermorium", "ts": "tennessine", "og": "oganesson"
}

# Load JSON data
with open(input_json, "r") as f:
    data = json.load(f)

entries = []
for row in data:
    # Defensive: make sure keys exist
    symbol = str(row.get("Symbol", "")).lower()
    name = symbol_to_name.get(symbol, symbol)
    mass = int(row.get("Mass"))
    half_life = float(row.get("half-life"))
    entries.append(f'    {{"name":"{name}-{mass}", "half-life":{half_life}}}')

# Write JS-style formatted output
with open(output_txt, "w", newline="\n") as f:
    f.write("var nuclides;\n")
    f.write('nuclides = {"nuclides": [\n')
    f.write(",\n".join(entries))
    f.write("\n]};\n")

print(f"Saved formatted output to {output_txt}")