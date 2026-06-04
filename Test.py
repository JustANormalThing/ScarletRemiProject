import torch
from pathlib import Path

# Load model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\Admin\Desktop\ReactProject\ProjectNew\ProjectThing\yolov5\runs\train\exp4\weights\best.pt', source='local')

# Run inference
results = model(r'C:\Users\Admin\Desktop\ReactProject\ProjectNew\ProjectThing\dataset\train\non_grape_trees\Tree7.jpg')

# Results
results.print()
results.save()  # saves to runs/detect/exp

py detect.py --weights C:\Users\Admin\Desktop\ReactProject\ProjectNew\ProjectThing\yolov5\runs\train\exp4\weights\best.pt --img 640 --source C:\Users\Admin\Desktop\ReactProject\ProjectNew\ProjectThing\dataset\train\non_grape_trees\Tree7.jpg'