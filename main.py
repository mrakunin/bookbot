from stats import count_words, count_chars, sort_chars

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

# entry point:
book = "books/frankenstein.txt"
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")

print("----------- Word Count ----------")
text = get_book_text("books/frankenstein.txt")
num_words = count_words(text)
print(f"Found {num_words} total words")

print("--------- Character Count -------")
chars = sort_chars(count_chars(text))
for entry in chars:
    if entry["char"].isalpha():
        print(f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")
