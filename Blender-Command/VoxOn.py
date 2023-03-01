import bpy
import sys


# Get OBJ file path from command line argument
obj_path = sys.argv[-2]
output_path = sys.argv[-1]

bpy.ops.object.delete(use_global=False, confirm=False)
# Import OBJ file
# bpy.ops.import_scene.obj(filepath=obj_file_path)
bpy.ops.wm.obj_import(filepath=obj_path)

# convert to voxel with Block On
bpy.ops.object.block_on()

# bpy.ops.export_scene.obj(filepath="D:\\Project\\Blender-command\\Output\\tree.obj",path_mode="COPY")
bpy.ops.export_scene.obj(filepath=output_path,path_mode="COPY")


