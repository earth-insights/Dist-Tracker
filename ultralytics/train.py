import sys
sys.path.append(".")
sys.path.append("..")

from ultralytics import YOLO

# Initialize model (specifying both model architecture and pretrained weights)
model = YOLO(
    model='./cfg/models/12/yolo12-UAV.yaml',  # Model configuration file
    task='detect',                         # Task type: detection/segmentation/pose
)

# Training configuration (complete parameter mapping)
results = model.train(
    # Required parameters
    data='./data/MOT-UAV.yaml',  # Dataset configuration file path 
    # For the Ultralytics framework, ​absolute paths must be used​ (for path )to avoid path resolution errors.
    epochs=50,  # Training duration
    batch=16,  # Batch size
    imgsz=640,  # Input image size
    device='0',  # GPU device
    # Model saving
    project='exp',        # Output directory (default runs/detect)
)