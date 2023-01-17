from converter.bosch import from_yaml
from converter.convert import convert_to_yolo


def main() -> None:
    train_bosch_labels = from_yaml('train.yaml')
    test_bosch_labels = from_yaml('test.yaml')

    convert_to_yolo(train_bosch_labels, 'labels/train')
    convert_to_yolo(test_bosch_labels, 'labels/test')


if __name__ == '__main__':
    main()
