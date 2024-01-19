import sys

def open_book(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main() -> int:
    book = open_book("./books/frankenstein.txt")
    print(book)
    return 0

if __name__ == '__main__':
    sys.exit(main())

