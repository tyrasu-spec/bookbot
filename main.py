from stats import word_count
from stats import char_count
from stats import to_dict_list


def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    print (get_book_text("books/frankenstein.txt"))


characters = char_count(get_book_text('books/frankenstein.txt'))

def sort_on(dict):
    return dict["num"]

unord_list = to_dict_list(characters)
unord_list.sort(reverse = True, key=sort_on)

print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print (f"Found {word_count(get_book_text('books/frankenstein.txt'))} total words")
print("--------- Character Count -------")
for entry in unord_list:
    print (f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")