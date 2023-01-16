from dataclasses import dataclass

import yaml


@dataclass
class BoschBox:
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    label: str
    occluded: bool


@dataclass
class BoschLabel:
    path: str
    boxes: list[BoschBox]


def from_yaml(path: str) -> list[BoschLabel]:
    with open(path, 'r') as file:
        labels = yaml.load(file, Loader=yaml.FullLoader)
    return [BoschLabel(label['path'], [BoschBox(**box) for box in label['boxes']])
            for label in labels]
