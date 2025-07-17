from pathlib import Path
import json
from src.visualization.draw import draw_boxes


def main():
    predictions_dir = Path("predictions")
    for pred_file in predictions_dir.rglob("*.json"):
        data = json.loads(pred_file.read_text())
        boxes = [
            (p["class"], p["box"][0], p["box"][1], p["box"][2], p["box"][3])
            for p in data.get("objects", [])
        ]
        image_file = Path("data/kaist/images") / pred_file.with_suffix(".jpg").name
        draw_boxes(image_file, boxes)


if __name__ == "__main__":
    main()
