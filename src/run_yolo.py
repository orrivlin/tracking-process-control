"""Run YOLOv8 inference on the FLIR ADAS dataset."""

from pathlib import Path
from ultralytics import YOLO


def run_inference(model_path: str, data_dir: str, output: str = "predictions") -> None:
    yolo = YOLO(model_path)
    out_dir = Path(output)
    out_dir.mkdir(parents=True, exist_ok=True)

    images = list(Path(data_dir).rglob("*.jpg"))
    for img in images:
        results = yolo(img)
        for result in results:
            result.save(filename=str(out_dir / img.name))


if __name__ == "__main__":
    run_inference("yolov8n.pt", "data/flir/images")
