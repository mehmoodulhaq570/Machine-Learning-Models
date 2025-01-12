import cv2
import numpy as np
import os
import random
import csv

# Output directories
output_dir = "crack_dataset"
categories = ["fatigue", "thermal", "stress_corrosion", "hydrogen_induced", "shrinkage"]

# Image dimensions
image_size = (128, 128)

# Number of images per category
num_images_per_category = 100

# Helper function to draw random lines (simulate cracks)
def generate_crack_image(crack_type, size=(128, 128)):
    img = np.ones(size, dtype=np.uint8) * 255  # Start with a white image
    num_lines = random.randint(3, 7)
    for _ in range(num_lines):
        start_point = (random.randint(0, size[1]), random.randint(0, size[0]))
        end_point = (random.randint(0, size[1]), random.randint(0, size[0]))
        thickness = random.randint(1, 3)
        color = (0,)  # Black crack
        if crack_type == "fatigue":
            # Incrementally jagged or curved lines
            for i in range(3):
                midpoint = ((start_point[0] + end_point[0]) // 2 + random.randint(-10, 10),
                            (start_point[1] + end_point[1]) // 2 + random.randint(-10, 10))
                cv2.line(img, start_point, midpoint, color, thickness)
                start_point = midpoint
        elif crack_type == "thermal":
            # Radiating lines from a random center point
            center = (random.randint(30, size[1]-30), random.randint(30, size[0]-30))
            end_point = (random.randint(center[0]-30, center[0]+30),
                         random.randint(center[1]-30, center[1]+30))
            cv2.line(img, center, end_point, color, thickness)
        elif crack_type == "stress_corrosion":
            # Multiple closely spaced lines
            for i in range(random.randint(2, 5)):
                offset = random.randint(-5, 5)
                start = (start_point[0] + offset, start_point[1] + offset)
                end = (end_point[0] + offset, end_point[1] + offset)
                cv2.line(img, start, end, color, thickness)
        elif crack_type == "hydrogen_induced":
            # Short, fragmented cracks
            for _ in range(5):
                start = (random.randint(0, size[1]), random.randint(0, size[0]))
                end = (start[0] + random.randint(-20, 20), start[1] + random.randint(-20, 20))
                cv2.line(img, start, end, color, thickness)
        elif crack_type == "shrinkage":
            # Random small cracks resembling spider webs
            center = (random.randint(30, size[1]-30), random.randint(30, size[0]-30))
            for _ in range(8):
                angle = random.uniform(0, 2 * np.pi)
                length = random.randint(20, 40)
                end = (int(center[0] + length * np.cos(angle)),
                       int(center[1] + length * np.sin(angle)))
                cv2.line(img, center, end, color, thickness)
    return img

# Create directories and generate dataset
os.makedirs(output_dir, exist_ok=True)
csv_file = open(os.path.join(output_dir, "crack_labels.csv"), mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["image", "label"])

for category in categories:
    category_dir = os.path.join(output_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    for i in range(num_images_per_category):
        image_name = f"{category}_{i+1}.png"
        image_path = os.path.join(category_dir, image_name)
        img = generate_crack_image(category, size=image_size)
        cv2.imwrite(image_path, img)
        csv_writer.writerow([image_name, category])

csv_file.close()
print(f"Dataset created in '{output_dir}' with labels saved in 'crack_labels.csv'.")
