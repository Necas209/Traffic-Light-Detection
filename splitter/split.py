import os
import shutil


def val_test_split(path: str, ratio: float = 0.5) -> None:
    # Get all the files
    files = os.listdir(path)
    # strip the extension
    files = [f[:-4] for f in files]
    # Split into 50% validation
    split = int(len(files) * ratio)
    # Create the directories
    parent = os.path.dirname(path)
    os.makedirs(os.path.join(parent, 'val'), exist_ok=True)
    # Move the files
    for f in files[:split]:
        shutil.move(os.path.join(path, f + '.png'), os.path.join(parent, 'val', f + '.png'))
        shutil.move(os.path.join(path, f + '.txt'), os.path.join(parent, 'val', f + '.txt'))
