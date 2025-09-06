from stats import chars_dict_to_sorted_list, count_characters, get_num_words
import sys
import pathlib

def usage_and_exit():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# --- Parse CLI args ---
if len(sys.argv) != 2:
    usage_and_exit()

book_path = pathlib.Path(sys.argv[1])

if not book_path.is_file():
    print(f"Error: file not found: {book_path}")
    usage_and_exit()


def get_book_text(path):
    with open(path) as f:
        return f.read()

def show_letters(items):
    for item in items:
        print(f"{item['char']}: {item['num']}")

def main():
    text = get_book_text(book_path)
    word_count = (get_num_words(text))
    character_count = count_characters(text)
    sorted_list = chars_dict_to_sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    show_letters(sorted_list)
    print("============= END ===============")

main()