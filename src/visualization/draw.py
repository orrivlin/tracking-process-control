"""Helpers for drawing annotations and predictions."""

from pathlib import Path
from typing import List, Tuple

import cv2
import matplotlib.pyplot as plt


BBox = Tuple[int, float, float, float, float]


def draw_boxes(image_path: Path, boxes: List[BBox], color=(0, 255, 0)) -> None:
    img = cv2.imread(str(image_path))
    for cls, xc, yc, w, h in boxes:
        x1 = int(xc - w / 2)
        y1 = int(yc - h / 2)
        x2 = int(xc + w / 2)
        y2 = int(yc + h / 2)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
