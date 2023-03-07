    # # Get the directory containing the OBJ file
    # OBJ_dir = os.path.dirname(OBJ_path)
    # # find mtl name in OBJ file
    # with open(OBJ_path, 'r') as f:
    #     # Read through each line in the file
    #     for line in f:
    #         # Check if the line starts with "mtllib "
    #         if line.startswith('mtllib '):
    #             # Extract the name of the MTL file from the line
    #             mtllib_name = line.split()[1]
    #             # Construct the path to the MTL file
    #             mtllib_path = os.path.join(OBJ_dir, mtllib_name)
    #             break

    
    # # get list of images and color code from mtl
    # image_files, no_img_colcode = extract_img_from_mtl(mtllib_path)     # images list AND color codes list

    # # find all names of newmtl ... in OBJ file
    # tex_names = find_usemtl(OBJ_path)

    # # get color codes
    # color_codes = all_col(image_files)
    # new_color_codes = []
    # for sublist in color_codes:
    #     new_color_codes.extend(sublist)
    # # join color codes from images and no image obtained from mtl file
    # join_codes = new_color_codes + no_img_colcode
    # print(join_codes)