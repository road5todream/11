from gendiff.generate import generate_diff
from gendiff.cli import path1, path2


def main():
    print(generate_diff(path1, path2, format='stylish'))


if __name__ == '__main__':
    main()
