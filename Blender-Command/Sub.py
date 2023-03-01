import subprocess
import os
    

def get_obj_path():
    while True:

        obj_path = input("Enter the path to an OBJ file: ")

        if not os.path.exists(obj_path):
            print(f"Path does not exist. Please try again.")
            continue
        
        if not obj_path.endswith(".obj"):
            print(f"Not an OBJ file. Please try again.")
            continue
        
        return obj_path



if __name__ == "__main__":
    # Prompt user for OBJ file path
    # obj_file_path = input("Enter the OBJ file path: ")
    
    obj_path = get_obj_path()

    VoxOn_path = input("Enter the VoxOn.py path: ")
    output_path = input("output path")

    # Run command in command line to import OBJ file into Blender
    subprocess.run(['blender','--python', VoxOn_path, '--', obj_path, output_path])


