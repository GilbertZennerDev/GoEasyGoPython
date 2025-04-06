import matplotlib.pyplot as plt
import json
import numpy as np

def save_image(image, filename):
    # Convert 2D list to a format suitable for JSON (list of lists)
    image_data = [[[int(r), int(g), int(b)] for r, g, b in row] for row in image.tolist()]

    with open(filename, 'w') as f:
        json.dump(image_data, f)

# Usage
# Initialize a 3x3 image (red, green, blue channels)
image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],  # Red, Green, Blue
    [[255, 255, 0], [0, 255, 255], [75, 0, 130]], # Yellow, Cyan, Dark blue
    [[0, 0, 0], [128, 128, 128], [192, 192, 192]]   # Black, Gray, Light gray
])

save_image(image, 'image.json')


import json
import numpy as np

def load_image(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    # Convert JSON data back to 2D list
    image_data = [[[int(r), int(g), int(b)] for r, g, b in row] for row in data]

    # Create a numpy array from the 2D list
    return np.array(image_data)

# Usage
loaded_image = load_image('image.json')
print(loaded_image)

def load_and_display_image(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    # Convert JSON data back to 2D list and then to NumPy array
    image_data = [[[int(r), int(g), int(b)] for r, g, b in row] for row in data]
    image = np.array(image_data)

    # Display the image using matplotlib's imshow
    plt.imshow(image)
    plt.axis('off')  # Hide axis ticks
    plt.show()
    
load_and_display_image('image.json')