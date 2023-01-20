from __future__ import annotations

import os
import shutil


def val_test_split(data_path: str, ratio: float) -> None:
    """ Splits the data into a validation and test set. """
    images_path = os.path.join(data_path, "images")
    labels_path = os.path.join(data_path, "labels")
    # Get all the files
    files = os.listdir(images_path)
    # strip the extension
    files = [f[:-4] for f in files]
    # Split into 50% validation
    split = int(len(files) * ratio)
    # Create the directories
    images_parent = os.path.dirname(images_path)
    labels_parent = os.path.dirname(labels_path)
    os.makedirs(os.path.join(images_parent, "val"), exist_ok=True)
    os.makedirs(os.path.join(labels_parent, "val"), exist_ok=True)
    # Move the files
    for f in files[:split]:
        shutil.move(os.path.join(images_path, f + ".png"), os.path.join(images_parent, "val", f + ".png"))
        shutil.move(os.path.join(labels_path, f + ".txt"), os.path.join(labels_parent, "val", f + ".txt"))


def count_data(data_path: str) -> None:
    """ Counts the number of images and labels in a dataset. """
    images_path = os.path.join(data_path, "images")
    for root, _, files in os.walk(images_path):
        print(f"Images in {root}: {len(files)}")
    labels_path = os.path.join(data_path, "labels")
    for root, _, files in os.walk(labels_path):
        print(f"Labels in {root}: {len(files)}")
