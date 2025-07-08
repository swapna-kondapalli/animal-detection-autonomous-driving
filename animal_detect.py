import json
import os
import csv
import cv2
import matplotlib.pyplot as plt
import random
from collections import defaultdict

# Paths
image_dir = r"C:\Users\Administrator\Desktop\datasets\coco\train2017"
annotation_file = r"C:\Users\Administrator\Desktop\datasets\coco\annotations\animal_only.json"

# Load annotations
with open(annotation_file, 'r') as f:
    coco = json.load(f)

# Category mappings
category_id_to_name = {cat['id']: cat['name'] for cat in coco['categories']}

# Create CSV file to save results
csv_file = open('results.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Image Name", "Label", "Confidence", "Bounding Box"])  # Confidence is dummy (fixed value)

animal_names = ['dog', 'cat', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']
animal_ids = [cat['id'] for cat in coco['categories'] if cat['name'] in animal_names]

# Group annotations by image
image_to_anns = defaultdict(list)
for ann in coco['annotations']:
    image_to_anns[ann['image_id']].append(ann)

# Pick images with animal annotations
animal_image_ids = [img_id for img_id, anns in image_to_anns.items()
                    if any(ann['category_id'] in animal_ids for ann in anns)]

# Pick 5 random images
sample_ids = random.sample(animal_image_ids, 5)

for img_id in sample_ids:
    img_info = next(img for img in coco['images'] if img['id'] == img_id)
    img_path = os.path.join(image_dir, img_info['file_name'])

    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        continue

    image = cv2.imread(img_path)
    if image is None:
        print(f"Could not read image: {img_path}")
        continue

    print(f"Processing image: {img_info['file_name']}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for ann in image_to_anns[img_id]:
        if ann['category_id'] in animal_ids:
            x, y, w, h = ann['bbox']
            x, y, w, h = int(x), int(y), int(w), int(h)
            label = category_id_to_name[ann['category_id']]

            # Save to CSV (dummy confidence 0.90)
            csv_writer.writerow([img_info['file_name'], label, 0.90, f"[{x}, {y}, {x+w}, {y+h}]"])

            # Draw rectangle and label
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 0), 2)

    # Show and save the image
    plt.figure(figsize=(10, 8))
    plt.imshow(image)
    plt.title(f"Animals in {img_info['file_name']}")
    plt.axis('off')
    plt.show()

    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, f"boxed_{img_info['file_name']}")
    cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    print(f"Saved: {save_path}")

csv_file.close()
print("✅ Detection results saved to results.csv")
