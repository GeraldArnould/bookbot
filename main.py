import sys

def open_book(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(book: str) -> int:
    return len(book.split())

def char_occurence(book):
    occurences = {}
    for c in book:
        if c.lower() in occurences:
            occurences[c.lower()] += 1
        else:
            occurences[c.lower()] = 1
    return occurences

def main() -> int:
    book = open_book("./books/frankenstein.txt")
    print(book)
    words = count_words(book)
    print(f"Book contains {words}.")
    # letters occurence
    occurences = char_occurence(book)
    print(occurences)
    return 0

if __name__ == '__main__':
    sys.exit(main())

