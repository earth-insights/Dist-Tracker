import sys
sys.path.append(".")
sys.path.append("..")

import os
from ultralytics import YOLO

# Define model path
model = YOLO("best.pt")

# Input and output paths
input_folder = "./dataset/Videos"
output_folder = "./processed_results/"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get all video files in input folder
video_extensions = ('.mp4')  # Supported formats
video_files = [f for f in os.listdir(input_folder) if f.endswith(video_extensions)]

for video_file in video_files:
    video_path = os.path.join(input_folder, video_file)
    
    print(f"Processing: {video_file}")

    # Set output path (under output folder)
    output_path = os.path.join(output_folder, os.path.splitext(video_file)[0])

    # Run tracking
    results = model.track(source=video_path, 
                          save_conf=True,
                          save_txt=False,
                          imgsz=1280,
                          conf=0, 
                          device=7,
                          show_labels=True,
                          show_conf=False,
                          save=True,
                          line_width=1,
                          save_frames=True,
                          project=output_folder,  # Output folder
                          name=os.path.splitext(video_file)[0])  # Use video filename as save path
    
    print(f"Finished processing: {video_file}")
    
print("All videos processed successfully!")