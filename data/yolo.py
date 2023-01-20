import os
from dataclasses import dataclass
from pathlib import Path

from data.bosch import BoschLabels


@dataclass
class YOLOLabel:
    class_id: int
    x_center: float
    y_center: float
    box_width: float
    box_height: float

    def __str__(self):
        return ' '.join([str(x) for x in self.__dict__.values()])

    def __repr__(self):
        return self.__str__()


def convert_to_yolo(bosch: BoschLabels, output_path: str, width: int = 1280, height: int = 720) -> None:
    os.makedirs(output_path, exist_ok=True)
    for label in bosch.labels:
        filename = Path(label.path).stem
        new_path = os.path.join(output_path, filename + '.txt')
        with open(new_path, 'w') as file:
            for box in label.boxes:
                yolo_label = box.to_yolo(width, height)
                file.write(str(yolo_label) + '\n')
