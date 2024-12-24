def count_words(book):
    return len(book.split())

def sort_on(dict):
    return dict["num"]

def count_characters(book):
    characters = {}
    for c in book:
        lowc = str.lower(c)
        if lowc.isalpha():
            if str.lower(c) in characters.keys():
                characters[str.lower(c)] += 1
            else:
                characters[str.lower(c)] = 1

    charray = []
    for x in characters.keys():
        cc = {"key":x, "num":characters[x]}
        charray.append(cc)
    charray.sort(reverse=True, key=sort_on)
    return charray

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

