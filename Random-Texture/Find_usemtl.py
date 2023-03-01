# Open the OBJ file and read its contents
# obj_name = input("Enter your OBJ name: ")

# with open(obj_name, 'r') as f:
#     obj_lines = f.readlines()



# material_name = []
# # Loop through each line in the OBJ file
# for line in obj_lines:
#     # Check if the line starts with "usemtl"
#     if line.startswith('usemtl'):
#         # If it does, extract the material name and print it
#         rows = line.split()[1]
#         material_name.append(rows)

#         #print(material_name)   #print output แบบเรียงบนลงล่าง

# print(material_name)


   
       
# def find_mtl(obj_name):
#     with open(obj_name, 'r') as f:
#         obj_lines = f.readlines()

#     # Loop through each line in the OBJ file
#     material_name = []
#     # Loop through each line in the OBJ file
#     for line in obj_lines:
#         # Check if the line starts with "usemtl"
#         if line.startswith('usemtl'):
#             # If it does, extract the material name and print it
#             rows = line.split()[1]
#             material_name.append(rows)
#     return material_name    


# x = find_mtl(obj_name)
# print(x)





colors = list(input())


print(colors)