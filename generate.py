import argparse

from video.generator import create_video


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--fps', type=int, default=15)
    parser.add_argument('--size', type=int, nargs=2, default=[1280, 720], help='video dimensions')
    parser.add_argument('--fourcc', type=str, default='mp4v')
    parser.add_argument('--input', type=str, default='../traffic_light_data/images/test')
    parser.add_argument('--output', type=str, default='../traffic_light_data/videos/test.mp4')
    return parser


def main():
    parser = create_parser()
    opt = parser.parse_args()
    create_video(opt.input, opt.output, opt.fps, opt.size, opt.fourcc)
    print(opt)


if __name__ == '__main__':
    main()
