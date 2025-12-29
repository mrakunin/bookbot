import sys
from stats import count_words, count_chars, sort_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

# entry point:
book = sys.argv[1]
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")

print("----------- Word Count ----------")
text = get_book_text(book)
num_words = count_words(text)
print(f"Found {num_words} total words")

print("--------- Character Count -------")
chars = sort_chars(count_chars(text))
for entry in chars:
    if entry["char"].isalpha():
        print(f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")
