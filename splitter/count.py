from __future__ import annotations

import os
from enum import Enum
from typing import Any


class DatasetEnum(Enum):
    Train = "train"
    Val = "val"
    Test = "test"


def count_images_labels(dataset: DatasetEnum) -> None:
    value: str | Any = dataset.value
    print(f"{dataset.name} images: {len(os.listdir('images/' + value))}")
    print(f"{dataset.name} labels: {len(os.listdir('labels/' + value))}")
