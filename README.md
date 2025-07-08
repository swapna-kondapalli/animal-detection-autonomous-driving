# animal-detection-autonomous-driving
Code, sample images, and results for our animal detection experiment using COCO dataset.
# 🐾 Animal Detection in Autonomous Driving Using COCO Dataset

This repository contains code and results for a preliminary experiment to detect animals (dog, cow, horse, etc.) in images, as a step toward integrating animal detection in autonomous driving systems.

## 📂 Contents
- `animal_detect.py`: Script to draw bounding boxes for animal detection using COCO dataset.
- `filter_animals_coco.py`: Script to filter only animal classes from COCO annotations.
- `/output/`: Contains annotated sample output images.
- `/code/fusiongen3d/`: Custom modules (for future expansion).
- `results.csv`: Output data from detection.

## 📋 Detected Classes
- Dog, Cat, Cow, Horse, Elephant, etc. (9 classes from COCO)

## ⚙️ Requirements
```bash
pip install opencv-python matplotlib
```

## 📥 Dataset
COCO 2017 Dataset (train2017 images + annotations).  
Due to size, not included here. Please download from:  
👉 [https://cocodataset.org/#download](https://cocodataset.org/#download)

## 📌 Notes
This is a 2D experiment, done as proof-of-concept.  
Future work: integrate with LiDAR, 3D datasets like KITTI or nuScenes.
