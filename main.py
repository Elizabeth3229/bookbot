from stats import get_word_count
from stats import get_char_count
from stats import sort_dict

import sys


def get_book_text(file_path):
    file_contents = None

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def print_report(file_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in range(0, len(sorted_chars)):
        if sorted_chars[i]["char"].isalpha():
            print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["count"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)
    sorted_chars = sort_dict(char_dict)

    print_report(file_path, num_words, sorted_chars)


main()
