import os
from pathlib import Path
from converter.bosch import from_yaml
from converter.yolo import bosch_to_yolo


def convert_to_yolo(yaml_path: str, output_path: str, test: bool = False) -> None:
    labels = from_yaml(yaml_path)

    width = 1280.0
    height = 720.0

    for label in labels:
        filename = Path(label.path).stem
        new_path = os.path.join(output_path, filename + '.txt')
        with open(new_path, 'w') as file:
            for box in label.boxes:
                yolo_label = bosch_to_yolo(box, width, height, test)
                file.write(str(yolo_label) + '\n')
