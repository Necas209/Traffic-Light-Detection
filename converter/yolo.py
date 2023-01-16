from dataclasses import dataclass

from converter.bosch import BoschBox
from converter.labels import TEST_LABELS, TRAIN_LABELS


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


def bosch_to_yolo(box: BoschBox, width: float, height: float, test: bool) -> YOLOLabel:
    x_min = box.x_min
    y_min = box.y_min
    x_max = box.x_max
    y_max = box.y_max

    x_center = (x_min + x_max) / 2.0
    y_center = (y_min + y_max) / 2.0

    x_center = x_center / width
    y_center = y_center / height

    box_width = (x_max - x_min) / width
    box_height = (y_max - y_min) / height

    class_id = (TEST_LABELS if test else TRAIN_LABELS).index(box.label)

    return YOLOLabel(class_id, x_center, y_center, box_width, box_height)
