import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class YOLOBox:
    class_id: int
    x_center: float
    y_center: float
    box_width: float
    box_height: float

    def __str__(self):
        return ' '.join(str(x) for x in self.__dict__.values())

    def __repr__(self):
        return self.__str__()


@dataclass
class YOLOLabel:
    """ Represents a label for a single image in the YOLO format. """
    path: str
    boxes: list[YOLOBox]

    def to_txt(self, output_dir: str) -> None:
        """ Writes the label to a text file. """
        filename = Path(self.path).stem + '.txt'
        with open(os.path.join(output_dir, filename), 'w') as file:
            for box in self.boxes:
                file.write(str(box) + '\n')
