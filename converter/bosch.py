from dataclasses import dataclass

import yaml


@dataclass
class BoschBox:
    """ Represents a bounding box in the Bosch dataset. """
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    label: str
    occluded: bool


@dataclass
class BoschLabel:
    """ Represents a label for a single image in the Bosch dataset. """
    path: str
    boxes: list[BoschBox]

    def filter_out(self, label: str) -> None:
        """ Removes all boxes with the given label. """
        self.boxes = [b for b in self.boxes if b.label != label]


def from_yaml(path: str) -> list[BoschLabel]:
    """ Loads the Bosch labels from the given yaml file. """
    with open(path, 'r') as file:
        labels = yaml.load(file, Loader=yaml.FullLoader)
    return [BoschLabel(label['path'], [BoschBox(**box) for box in label['boxes']])
            for label in labels]


def get_class_id(label: str) -> int:
    """ Returns the class id for the given Bosch label. """
    labels = {
        'Green': 0,
        'Yellow': 1,
        'Red': 2,
        'off': 3,
        'GreenStraight': 0,
        'GreenLeft': 0,
        'GreenRight': 0,
        'GreenStraightLeft': 0,
        'GreenStraightRight': 0,
        'RedStraight': 2,
        'RedLeft': 2,
        'RedRight': 2,
        'RedStraightLeft': 2,
        'RedStraightRight': 2,
    }

    return labels.get(label, -1)
