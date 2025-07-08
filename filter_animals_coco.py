import json
import os
from tqdm import tqdm

# Paths
input_json = r"C:\Users\Administrator\Desktop\datasets\coco\annotations\instances_train2017.json"
output_json = r"C:\Users\Administrator\Desktop\datasets\coco\annotations\animal_only.json"

# Animal classes of interest
animal_names = ['dog', 'cat', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']

# Load original COCO data
with open(input_json, 'r') as f:
    coco_data = json.load(f)

# Filter categories
animal_cats = [cat for cat in coco_data['categories'] if cat['name'] in animal_names]
animal_cat_ids = {cat['id'] for cat in animal_cats}

# Filter annotations
animal_anns = [ann for ann in coco_data['annotations'] if ann['category_id'] in animal_cat_ids]
animal_image_ids = {ann['image_id'] for ann in animal_anns}

# Filter images
animal_images = [img for img in coco_data['images'] if img['id'] in animal_image_ids]

# Build new JSON
animal_subset = {
    'info': coco_data.get('info', {}),
    'licenses': coco_data.get('licenses', []),
    'images': animal_images,
    'annotations': animal_anns,
    'categories': animal_cats
}

# Save to output
with open(output_json, 'w') as f:
    json.dump(animal_subset, f)

print(f"Filtered animal dataset saved to: {output_json}")
