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

def sorted_char_occurence(chars_dict):
    sorted_occurences = []
    for c in chars_dict:
        if c.isalpha():
            sorted_occurences.append((c, chars_dict[c]))
    # Sort in reverse according to the second tuple member (char occurence)
    # source: https://docs.python.org/3/howto/sorting.html
    sorted_occurences.sort(reverse=True, key=lambda char: char[1])
    return sorted_occurences

def report(path):
    print(f"--- Begin report of {path}")
    book = open_book(path)
    print(count_words(book), " words found in the document\n")
    occurences = char_occurence(book)
    sorted_occurences = sorted_char_occurence(occurences)
    for occ in sorted_occurences:
        print(f"The '{occ[0]}' char was found {occ[1]} times.")



def main() -> int:
    path = "./books/frankenstein.txt"
    # book = open_book(path)
    # print(book)
    # words = count_words(book)
    # print(f"Book contains {words}.")
    # letters occurence
    # occurences = char_occurence(book)
    # print(occurences)
    report(path)
    return 0

if __name__ == '__main__':
    sys.exit(main())

