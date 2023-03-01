import os
import itertools
import random

material_names = ["Stem", "Leaf", "Ceramic", "Ground"]
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]  # Possible colors: red, green, blue, yellow
output_folder = "mtl_files"  # Change this to the desired folder name

mtl_files = []

# Generate all possible color combinations for the materials
for color_combination in itertools.permutations(colors, len(material_names)):
    mtl_file = ""
    for i, name in enumerate(material_names):
        r, g, b = color_combination[i]
        mtl_file += f"newmtl {name}\n"
        mtl_file += f"Ka {r:.3f} {g:.3f} {b:.3f}\n"
        mtl_file += f"Kd {r:.3f} {g:.3f} {b:.3f}\n"
        mtl_file += "Ks 0.000 0.000 0.000\n"
        mtl_file += "Ns 0.000\n"
        mtl_file += "d 1.000\n"
        mtl_file += "illum 2\n"
        mtl_file += "\n"
    mtl_files.append(mtl_file)

# Shuffle the list of MTL files randomly
random.shuffle(mtl_files)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Write each MTL file to the output folder
for i, mtl_file in enumerate(mtl_files):
    filename = f"my_materials_{i+1}.mtl"
    filepath = os.path.join(output_folder, filename)
    with open(filepath, "w") as f:
        f.write(mtl_file)
