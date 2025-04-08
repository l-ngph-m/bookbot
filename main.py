from stats import get_num_words, get_book_text, get_char_count, get_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    sorted_list = get_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["count"]}')

main()
