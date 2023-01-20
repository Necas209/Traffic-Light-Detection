import argparse

from data.split import val_test_split, count_data


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data', help='Path to the data directory.')
    parser.add_argument("--ratio", type=float, default=0.5, help="Ratio of validation set")
    return parser


def main() -> None:
    args = create_parser().parse_args()
    if args.ratio < 0 or args.ratio > 1:
        raise ValueError("Ratio must be between 0 and 1")
    if args.ratio == 0:
        print("Ratio is 0, no splitting will be done")
    else:
        val_test_split(args.data, args.ratio)
    count_data(args.data)


if __name__ == "__main__":
    main()
