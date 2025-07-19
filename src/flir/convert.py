"""Utilities to convert FLIR annotations to YOLO format."""

from pathlib import Path
import json
from typing import Iterable


class AnnotationConverter:
    def __init__(self, root: str):
        self.root = Path(root)
        self.labels_dir = self.root / "labels"
        self.labels_dir.mkdir(parents=True, exist_ok=True)

    def convert(self) -> None:
        """Convert all annotation files from FLIR format to YOLO."""
        for ann in self.root.rglob("*.json"):
            if ann.name == "classes.json":
                continue
            yolo_path = self.labels_dir / (ann.stem + ".txt")
            bboxes = self._parse_annotation(ann)
            with open(yolo_path, "w") as f:
                for bbox in bboxes:
                    cls, xc, yc, w, h = bbox
                    f.write(f"{cls} {xc} {yc} {w} {h}\n")

    def _parse_annotation(self, file: Path) -> Iterable[tuple]:
        data = json.loads(file.read_text())
        bboxes = []
        for obj in data.get("annotations", []):
            if obj.get("category_id") != 1:
                continue
            x1, y1, w, h = obj["bbox"]
            x2 = x1 + w
            y2 = y1 + h
            xc = (x1 + x2) / 2
            yc = (y1 + y2) / 2
            bboxes.append((0, xc, yc, w, h))
        return bboxes


if __name__ == "__main__":
    converter = AnnotationConverter("data/flir/train")
    converter.convert()
