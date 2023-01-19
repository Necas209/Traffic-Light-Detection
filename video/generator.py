import cv2
import glob

import numpy as np


def create_video(input_path: str, output: str, fps: int, size: tuple[int, int], fourcc: str) -> None:
    img_array = []
    for filename in sorted(glob.glob(input_path + '/*.png')):
        img: np.ndarray = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*fourcc), fps, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
