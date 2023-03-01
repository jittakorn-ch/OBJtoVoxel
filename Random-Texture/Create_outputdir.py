import os
def create_outputdir(obj_path):
    # Extract the file name from the file path using os.path.basename()
    file_name = os.path.basename(obj_path)
    # Remove the file extension using os.path.splitext()
    name_without_ext, _ = os.path.splitext(file_name)
    # Output folder
    output_folder = name_without_ext

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


obj_path = input("Enter your OBJ path name: ")
output_folder = create_outputdir(obj_path)
print(output_folder)

# print(output_folder)