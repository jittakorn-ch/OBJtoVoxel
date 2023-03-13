import subprocess
import os
import argparse    

# def get_obj_path():
#     while True:

#         obj_path = input("Enter the path to an OBJ file: ")

#         if not os.path.exists(obj_path):
#             print(f"Path does not exist. Please try again.")
#             continue
        
#         if not obj_path.endswith(".obj"):
#             print(f"Not an OBJ file. Please try again.")
#             continue
        
#         return obj_path


def create_folder(output_folder_path, obj_path):
    # Define the path to the output folder
    # output_folder_path = "D:/Project/ObjtoVoxel/Output"
    file_name = os.path.splitext(os.path.basename(obj_path))[0]

    # Create the full path to the new folder
    new_folder_path = os.path.join(output_folder_path, "vox_" + file_name)

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        # If the folder does not exist, create it
        os.makedirs(new_folder_path)
        print(f"Folder created successfully at {output_folder_path}.")
    else:
        # If the folder already exists, print a message
        print(f"Folder already exists at {output_folder_path}.")
    return new_folder_path



if __name__ == "__main__":
    
    # obj_path = get_obj_path()

    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--Filepath', type=str, help='Path to the OBJ file')
    parser.add_argument('--Resolution', type=int, help='Resolution of voxel model (1-256)')
    parser.add_argument('--Size', type=float, help='Cube size (0-1)')
    args = parser.parse_args()

    obj_path = args.Filepath
    Resolution = str(args.Resolution)
    Cube_size = str(args.Size)
 

    VoxOn_path = "D:/Project/ObjtoVoxel/Blender-Command/VoxOn.py"
    blender_path = "C:/Program Files/Blender Foundation/Blender 3.3/blender.exe"
    output_folder_path = "D:/Project/ObjtoVoxel/Output"


    new_folder_path = create_folder(output_folder_path, obj_path)
    # print(new_folder_path)

    file_name = os.path.basename(obj_path)
    # Construct the full file path
    output_path = os.path.join(new_folder_path, f"vox{str(Resolution)}_{file_name}")

    # Change the working directory to the directory containing the Blender executable file
    os.chdir(os.path.dirname(blender_path))


    subprocess.run([blender_path, '--python', VoxOn_path, '--', obj_path, output_path, Resolution, Cube_size])
