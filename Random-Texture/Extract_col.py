from PIL import Image
# from collections import Counter
import math

# # Load the image
# input_file = input("Enter your IMAGE path: ")
# image = Image.open(input_file)

# # Get the size of the image in pixels
# width, height = image.size

# # Loop over each pixel and get its RGB color code
# for x in range(width):
#     for y in range(height):
#         r, g, b = image.getpixel((x, y))
#         print(f"Pixel ({x}, {y}): RGB = ({r}, {g}, {b})")




# # Get RGB values of all pixels
# pixels = image.load()
# width, height = image.size

# # Iterate over all pixels and print color code
# for x in range(width):
#     for y in range(height):
#         color = pixels[x, y]
#         print(f"RGB: {color}")





# # Get RGB values of all pixels
# pixels = image.load()
# width, height = image.size

# # Create set to store unique color codes
# unique_colors = set()

# # Iterate over all pixels and add color codes to set
# for x in range(width):
#     for y in range(height):
#         color = pixels[x, y]
#         unique_colors.add(color)

# # Print unique color codes
# for color in unique_colors:
#     print(f"RGB: {color}")






# # Get RGB values of all pixels
# pixels = image.load()
# width, height = image.size

# # Count occurrences of each color code
# color_counts = Counter(pixels[x, y] for x in range(width) for y in range(height))

# # Print the three most common color codes
# for color, count in color_counts.most_common(3):
#     print(f"RGB: {color}, count: {count}")







def get_image_colors(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Resize the image to reduce processing time
        # img = img.resize((150, 150))
        # Get a list of all pixel colors in the image
        pixels = list(img.getdata())
        # Calculate the color difference for each pixel
        color_diffs = [math.sqrt(sum((pixels[i][j] - pixels[i+1][j])**2 for j in range(3))) for i in range(len(pixels)-1)]
        # Get a list of unique color codes and their frequency
        colors = {}
        for i, pixel in enumerate(pixels):
            if pixel not in colors:
                colors[pixel] = 1
            else:
                colors[pixel] += 1
        # Sort the colors by frequency
        sorted_colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)
        # Get the three most different colors in the image
        top_colors = [sorted_colors[0][0]]
        for color, freq in sorted_colors[1:]:
            if all(math.sqrt(sum((color[j] - top_color[j])**2 for j in range(3))) >= 30 for top_color in top_colors):
                top_colors.append(color)
                if len(top_colors) == 4:
                    break
        # Convert the colors to hex codes and return them
        return ['#%02x%02x%02x' % color for color in top_colors]

if __name__ == '__main__':

    image_path = input("Enter your IMAGE path: ")

    top_colors = get_image_colors(image_path)
    print('The three most different colors in the image are:')
    for color in top_colors:
        print(color)