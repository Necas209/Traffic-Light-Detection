import argparse
import os

from converter.bosch import from_yaml
from converter.converter import convert_to_yolo


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default='.', help='Input directory')
    parser.add_argument('--output_dir', type=str, default='labels', help='Output directory')
    parser.add_argument('--train', type=str, help='Train file', default='train.yaml')
    parser.add_argument('--test', type=str, help='Test file', default='test.yaml')
    return parser


def main() -> None:
    args = create_parser().parse_args()
    train_bosch_labels = from_yaml(os.path.join(args.input_dir, args.train))
    test_bosch_labels = from_yaml(os.path.join(args.input_dir, args.test))

    print('Train boxes:', sum(map(len, (label.boxes for label in train_bosch_labels))))
    print('Test boxes:', sum(map(len, (label.boxes for label in test_bosch_labels))))

    for bosch_label in train_bosch_labels:
        bosch_label.filter_out('off')
    for bosch_label in test_bosch_labels:
        bosch_label.filter_out('off')

    print('Train boxes:', sum(map(len, (label.boxes for label in train_bosch_labels))))
    print('Test boxes:', sum(map(len, (label.boxes for label in test_bosch_labels))))

    convert_to_yolo(train_bosch_labels, os.path.join(args.output_dir, 'train'))
    convert_to_yolo(test_bosch_labels, os.path.join(args.output_dir, 'test'))


if __name__ == '__main__':
    main()
