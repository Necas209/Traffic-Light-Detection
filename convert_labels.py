import argparse

from data.bosch import BoschLabels
from data.yolo import convert_to_yolo


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Path to the input YAML file.')
    parser.add_argument('--output_dir', type=str, default='labels', help='Path to the output directory.')
    parser.add_argument('--filter', type=str, nargs='+', choices=['Green', 'Yellow', 'Red', 'off'],
                        help='Filter out labels')
    return parser


def main() -> None:
    args = create_parser().parse_args()
    labels = BoschLabels.from_yaml(args.input)

    print('Bounding boxes:', labels.number_of_boxes)

    if args.filter:
        labels.filter_out(args.filter)
        print('Bounding boxes after filtering:', labels.number_of_boxes)

    convert_to_yolo(labels, args.output_dir)


if __name__ == '__main__':
    main()
