"""Utilities to convert KAIST annotations to YOLO format."""

from pathlib import Path
import json


class AnnotationConverter:
    def __init__(self, root: str):
        self.root = Path(root)
        self.labels_dir = self.root / "labels"
        self.labels_dir.mkdir(parents=True, exist_ok=True)

    def convert(self) -> None:
        """Convert all annotation files from KAIST format to YOLO."""
        for ann in self.root.rglob("*.json"):
            yolo_path = self.labels_dir / (ann.stem + ".txt")
            bboxes = self._parse_annotation(ann)
            with open(yolo_path, "w") as f:
                for bbox in bboxes:
                    cls, xc, yc, w, h = bbox
                    f.write(f"{cls} {xc} {yc} {w} {h}\n")

    def _parse_annotation(self, file: Path):
        data = json.loads(file.read_text())
        bboxes = []
        for obj in data.get("objects", []):
            x1, y1, x2, y2 = obj["bbox"]
            xc = (x1 + x2) / 2
            yc = (y1 + y2) / 2
            w = x2 - x1
            h = y2 - y1
            bboxes.append((0, xc, yc, w, h))  # assume single class
        return bboxes


if __name__ == "__main__":
    converter = AnnotationConverter("data/kaist")
    converter.convert()
