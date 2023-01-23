import argparse

from data.bosch import BoschDataset


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Path to the input YAML file.')
    parser.add_argument('--output_dir', type=str, default='labels', help='Path to the output directory.')
    parser.add_argument('--filter', type=str, nargs='+', choices=['Green', 'Yellow', 'Red', 'off'],
                        help='Filter out labels')
    return parser


def main() -> None:
    args = create_parser().parse_args()
    bosch_ds = BoschDataset.from_yaml(args.input)

    print('Bounding boxes:', bosch_ds.number_of_boxes)

    if args.filter:
        bosch_ds.filter_out(args.filter)
        print('Bounding boxes after filtering:', bosch_ds.number_of_boxes)

    yolo_ds = bosch_ds.to_yolo()
    yolo_ds.to_txt(args.output_dir)


if __name__ == '__main__':
    main()
