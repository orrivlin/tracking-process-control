# Tracking Process Control

This repository contains utilities to work with the **FLIR ADAS** thermal dataset and to run YOLOv8 detectors. It is structured to make it easy to experiment with reinforcement learning for tracking.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download and extract the dataset:
   ```bash
   python -m src.flir.download
   ```
   This will place the files under `data/flir`.
3. Convert annotations to YOLO format:
   ```bash
   python -m src.flir.convert
   ```

## Running YOLOv8

Use the `src/run_yolo.py` script to perform inference on the dataset:

```bash
python -m src.run_yolo --model yolov8n.pt --data data/flir/images
```

Predictions will be saved under the `predictions/` directory.

## Visualization

Use `scripts/visualize_predictions.py` to draw bounding boxes for predictions:

```bash
python scripts/visualize_predictions.py
```

## Directory Structure

- `src/flir/` – dataset download and conversion utilities
- `src/visualization/` – drawing helpers
- `src/run_yolo.py` – simple YOLOv8 inference script
- `scripts/` – additional runnable scripts

The `data/` directory is ignored from version control and should contain the FLIR ADAS dataset once downloaded.
