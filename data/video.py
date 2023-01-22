import glob

import cv2
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


def display_video(video_path: str) -> None:
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
