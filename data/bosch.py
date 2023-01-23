from __future__ import annotations

import os
from dataclasses import dataclass

import yaml

import data.yolo as yolo

AnyPath = str | bytes | os.PathLike

LABELS = {
    'Green': 0,
    'Yellow': 1,
    'Red': 2,
    'off': 3,
}


@dataclass
class BoschBox:
    """ Represents a bounding box in the Bosch dataset. """
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    label: str
    occluded: bool

    @property
    def class_id(self) -> int:
        """ Returns the class id for the label. """
        if self.label.startswith('Green'):
            return LABELS['Green']
        elif self.label.startswith('Yellow'):
            return LABELS['Yellow']
        elif self.label.startswith('Red'):
            return LABELS['Red']
        else:
            return LABELS['off']

    def to_yolo(self, width: float, height: float) -> yolo.YOLOBox:
        x_min = self.x_min if self.x_min > 0 else 0
        y_min = self.y_min if self.y_min > 0 else 0
        x_max = self.x_max
        y_max = self.y_max

        x_center = (x_min + x_max) / 2.0
        y_center = (y_min + y_max) / 2.0

        x_center = x_center / width
        y_center = y_center / height

        box_width = (x_max - x_min) / width
        box_height = (y_max - y_min) / height

        return yolo.YOLOBox(self.class_id, x_center, y_center, box_width, box_height)


@dataclass
class BoschLabel:
    """ Represents a label for a single image in the Bosch dataset. """
    path: AnyPath
    boxes: list[BoschBox]

    def filter_out(self, labels: list[str]) -> None:
        """ Filters out the given labels from the boxes. """
        self.boxes = [box for box in self.boxes if box.label not in labels]

    @property
    def number_of_boxes(self) -> int:
        """ Returns the number of boxes in this label. """
        return len(self.boxes)

    def to_yolo(self, width: float, height: float) -> yolo.YOLOLabel:
        """ Converts the label to the YOLO format. """
        boxes = [box.to_yolo(width, height) for box in self.boxes]
        return yolo.YOLOLabel(self.path, boxes)


@dataclass
class BoschDataset:
    """ Represents the Bosch dataset. """
    yaml_path: AnyPath
    labels: list[BoschLabel]

    @staticmethod
    def from_yaml(path: AnyPath) -> BoschDataset:
        """ Creates a BoschLabels from a YAML file. """
        with open(path, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return BoschDataset(
            yaml_path=path,
            labels=[BoschLabel(item['path'], [BoschBox(**box) for box in item['boxes']]) for item in data]
        )

    @property
    def number_of_boxes(self) -> int:
        """ Returns the number of boxes in the dataset. """
        return sum(label.number_of_boxes for label in self.labels)

    def filter_out(self, filter_labels: list[str]) -> None:
        """ Filters out the given labels from the boxes. """
        for bosch_label in self.labels:
            bosch_label.filter_out(filter_labels)

    def to_yolo(self, width: int = 1280, height: int = 720) -> yolo.YOLODataset:
        """ Converts the dataset to the YOLO format. """
        return yolo.YOLODataset([label.to_yolo(width, height) for label in self.labels])
