import sys

def print_book(path: str) -> None:
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

def main() -> int:
    print_book("./books/frankenstein.txt")
    return 0

if __name__ == '__main__':
    sys.exit(main())

