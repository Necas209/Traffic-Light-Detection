import argparse

from splitter.split import val_test_split
from splitter.count import count_images_labels, DatasetEnum


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        default="labels",
        help="Path to the dataset",
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=0.5,
        help="Ratio of validation set",
    )
    return parser


def main() -> None:
    args = create_parser().parse_args()

    val_test_split(args.path, args.ratio)

    for dataset in DatasetEnum:
        count_images_labels(dataset)


if __name__ == "__main__":
    main()
