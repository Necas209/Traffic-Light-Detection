import os
from pathlib import Path

from converter.bosch import BoschLabel
from converter.yolo import bosch_to_yolo


def convert_to_yolo(labels: list[BoschLabel], output_path: str, width: int = 1280, height: int = 720) -> None:
    for label in labels:
        filename = Path(label.path).stem
        new_path = os.path.join(output_path, filename + '.txt')
        with open(new_path, 'w') as file:
            for box in label.boxes:
                yolo_label = bosch_to_yolo(box, width, height)
                file.write(str(yolo_label) + '\n')
