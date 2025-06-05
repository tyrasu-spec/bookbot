from stats import word_count
from stats import char_count


def get_book_text(path):
    with open(path) as file:
        return file.read()


def main():
    print (get_book_text("books/frankenstein.txt"))


characters = char_count(get_book_text('books/frankenstein.txt'))



print (f"{word_count(get_book_text('books/frankenstein.txt'))} words found in the document.")
print (characters)