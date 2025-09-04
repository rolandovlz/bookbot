import sys
from stats import count_words, count_chars, sort_dicts

def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, wc, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for d in sorted:
        if d["char"].isalpha():
            c = d["char"]
            n = d["num"]
            print(f"{c}: {n}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    characters_dict = count_chars(text)
    sorted_dicts = sort_dicts(characters_dict)

    print_report(path, num_words, sorted_dicts)

main()
