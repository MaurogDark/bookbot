from stats import count_words, count_characters
import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>\n")
        sys.exit(1)
    book = args[1]
    with open(book) as f:
        file_contents = f.read()
    count = count_words(file_contents)
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")
    print()
    charray = count_characters(file_contents)
    for c in charray:
        print(f"{c["key"]}: {c["num"]}")
    print("--- End report ---")
    
main()


