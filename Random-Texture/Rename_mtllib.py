import os

# define list of new mtllib names
new_names = ['name1', 'name2']

# specify full path to input file
input_file = 'mtl_files\input.obj'

# loop through each new name and rename the mtllib in obj file
for name in new_names:
    # define output file path
    output_file = f'output_{name}.obj'
    
    # open input and output files
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # loop through each line in input file
        for line in f_in:
            # check if line starts with 'mtllib'
            if line.startswith('mtllib'):
                # replace mtllib name with new name
                new_line = f'mtllib {name}.mtl\n'
            else:
                # keep line as is
                new_line = line
            
            # write new line to output file
            f_out.write(new_line)

# print message to confirm completion
print(f'{len(new_names)} obj files created')








# import os

# def rename_mtllib(mtl_names):
#     # create output directory if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)

#     # loop through each new name and rename the mtllib in obj file
#     for name in mtl_names:
#         # define output file path
#         output_file = os.path.join(output_folder, f'output_{name}.obj')
        
#         # open input and output files
#         with open(obj_path, 'r') as f_in, open(output_file, 'w') as f_out:
#             # loop through each line in input file
#             for line in f_in:
#                 # check if line starts with 'mtllib'
#                 if line.startswith('mtllib'):
#                     # replace mtllib name with new name
#                     new_line = f'mtllib {name}.mtl\n'
#                 else:
#                     # keep line as is
#                     new_line = line
                
#                 # write new line to output file
#                 f_out.write(new_line)

#     # print message to confirm completion
#     print(f'{len(mtl_names)} obj files created in {output_folder}')


