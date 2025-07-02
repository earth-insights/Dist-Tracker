import sys
sys.path.append(".")
sys.path.append("..")

import os
from ultralytics import YOLO

# Define model and input/output paths
model = YOLO("best.pt")

video_path = "./dataset/Videos/MultiUAV-257.mp4"
output_folder = "./processed_results/MultiUAV-257/"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate subfolder name (using filename without extension)
video_name = os.path.splitext(os.path.basename(video_path))[0]
output_path = os.path.join(output_folder, video_name)

# Run object tracking
results = model.track(
    source=video_path,
    save_conf=False,
    save_txt=False,
    imgsz=1280,
    conf=0, 
    device=1,
    show_labels=False,
    show_boxes=True,
    show_conf=False,
    save=True,
    project=output_folder,  # Output directory
    name=video_name,  # Use video name as save path
    line_width=2,
    save_frames=True
)