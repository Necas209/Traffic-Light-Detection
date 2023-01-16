from converter.convert import convert_to_yolo


def main() -> None:
    convert_to_yolo('train.yaml', 'labels/train')
    convert_to_yolo('test.yaml', 'labels/test', test=True)


if __name__ == '__main__':
    main()
