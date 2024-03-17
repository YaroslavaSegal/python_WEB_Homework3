import argparse
import shutil
from pathlib import Path
from shutil import copyfile
from threading import Thread

from logger import logger

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument("source", help="Source folder")
parser.add_argument("--output", "-o", help="Output folder", default="sorted_folder")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")

folders = []


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as err:
                logger.error(err)


if __name__ == '__main__':
    base_folder = Path(source)
    output_folder = Path(output)
    folders.append(base_folder)
    grabs_folder(base_folder)

    threads = []

    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]

    print('Do you want to remove original folder? Print yes/no')
    decision = input()
    if decision == "yes":
        shutil.rmtree(base_folder)
        print('Original folder was removed. Your new folder is "sorted_folder"')
    elif decision == "no":
        print('We have two folders now: original and sorted_folder')
    else:
        print("Input yes or no")

