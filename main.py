from stats import count_words, count_characters

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    count = count_words(file_contents)
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")
    print()
    charray = count_characters(file_contents)
    for c in charray:
        print(f"The '{c["key"]}' character was found {c["num"]} times")
    print("--- End report ---")
    
main()


