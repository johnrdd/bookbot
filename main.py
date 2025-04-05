from stats import get_num_words
from stats import count_characters 
from stats import char_sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def report(wcnt, sorted, bookpath):
    template_1=f""""
    ============ BOOKBOT ============
Analyzing book found at {bookpath}...
----------- Word Count ----------"""
    print(template_1)
    print(f"Found {wcnt} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted)):
        letter=sorted[i]["char"]
        if not letter.isalpha():
            continue
        else:
            value=sorted[i]["num"]
        
        print(f"{letter}: {value}")

    print("============= END ===============")

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book=get_book_text(sys.argv[1])
    bookpath=(sys.argv[1])

    wcnt = get_num_words(book)
    chars = count_characters(book)
    sorted = char_sort(chars)

    report(wcnt, sorted, bookpath)

main()
