import argparse

import data.bosch as bosch


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Path to the input YAML file.')
    parser.add_argument('--output_dir', type=str, default='labels', help='Path to the output directory.')
    parser.add_argument('--filter', type=str, nargs='+', choices=['Green', 'Yellow', 'Red', 'off'],
                        help='Filter out labels')
    return parser


def main() -> None:
    args = create_parser().parse_args()
    bosch_labels = bosch.from_yaml(args.input)

    print('Bounding boxes:', bosch.number_of_boxes(bosch_labels))

    if args.filter:
        bosch.filter_out(bosch_labels, args.filter)
        print('Bounding boxes after filtering:', bosch.number_of_boxes(bosch_labels))

    yolo_labels = [label.to_yolo(width=1280, height=720) for label in bosch_labels]
    for label in yolo_labels:
        label.to_txt(args.output_dir)


if __name__ == '__main__':
    main()
