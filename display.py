import argparse

from video.displayer import display_video


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='../YOLOv6/runs/inference/exp.mp4')
    parser.add_argument('--fps', type=int, default=15)
    return parser


def main():
    parser = create_parser()
    opt = parser.parse_args()
    display_video(opt.input)
    print(opt)


if __name__ == '__main__':
    main()
