import random
import os
import itertools



def find_usemtl(obj_path):
    with open(obj_path, 'r') as f:
        obj_lines = f.readlines()
    # Loop through each line in the OBJ file
    tex_names = []
    # Loop through each line in the OBJ file
    for line in obj_lines:
        # Check if the line starts with "usemtl"
        if line.startswith('usemtl'):
            # If it does, extract the material name and print it
            rows = line.split()[1]
            tex_names.append(rows)
    return tex_names





def create_outputdir(obj_path):
    # Extract the file name from the file path using os.path.basename()
    file_name = os.path.basename(obj_path)
    # Remove the file extension using os.path.splitext()
    name_without_ext, _ = os.path.splitext(file_name)
    # Output folder
    output_folder = name_without_ext+"_rm"
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder    




def create_mtl(tex_names, colors, output_folder):
    # output_folder = output_folder  # Change this to the desired folder name

    mtl_files = []
    # Generate all possible color combinations for the materials
    for color_combination in itertools.permutations(colors, len(tex_names)):
        mtl_file = ""
        for i, name in enumerate(tex_names):
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
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    mtl_names = []
    # Write each MTL file to the output folder
    for i, mtl_file in enumerate(mtl_files):
        filename = f"{output_folder}_{i+1}.mtl"
        mtl_names.append(filename)
        filepath = os.path.join(output_folder, filename)
        with open(filepath, "w") as f:
            f.write(mtl_file)
    return mtl_names





def rename_mtllib(mtl_names, obj_path, output_folder):
    # create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # loop through each new name and rename the mtllib in obj file
    for name in mtl_names:
        # Split the file name into name and extension using os.path.splitext()
        name_w, ext = os.path.splitext(name)
        # Extract only the name part
        name_without_ext = name_w
        # define output file path
        output_file = os.path.join(output_folder, f'{name_without_ext}.obj')
        
        # open input and output files
        with open(obj_path, 'r') as f_in, open(output_file, 'w') as f_out:
            # loop through each line in input file
            for line in f_in:
                # check if line starts with 'mtllib'
                if line.startswith('mtllib'):
                    # replace mtllib name with new name
                    new_line = f'mtllib {name}\n'
                else:
                    # keep line as is
                    new_line = line
                
                # write new line to output file
                f_out.write(new_line)

    # print message to confirm completion
    print(f'{len(mtl_names)} obj files created in {output_folder}')



def get_colorcode():
# Prompt the user to enter a list of tuples
    input_str = input("Enter color codes: ")
# Convert the input string to a list of tuples
    colors = eval(input_str)
# Print the resulting list
    return colors



if __name__ == "__main__":

    # Open the OBJ file and read its contents
    obj_path = input("Enter your OBJ path name: ")

    # Indicates the number of materials is
    count_tex = find_usemtl(obj_path)
    print(f'The number of material is: ')
    print(len(count_tex))
    print(f'Enter your colors code Example: [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0)]')


    colors = get_colorcode()  # Possible colors: red, green, blue, yellow

    # Create output folder
    output_folder = create_outputdir(obj_path)

    #all names of newmtl ... in obj file
    tex_names = find_usemtl(obj_path)

    # all names of mtl are created
    mtl_names = create_mtl(tex_names, colors, output_folder)

    rename_mtllib(mtl_names, obj_path, output_folder)



