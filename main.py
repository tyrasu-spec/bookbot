import sys

from stats import word_count
from stats import char_count
from stats import to_dict_list


def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    print (get_book_text(sys.argv[1]))

def sort_on(dict):
    return dict["num"]

if (len(sys.argv) != 2):
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



characters = char_count(get_book_text(sys.argv[1]))

unord_list = to_dict_list(characters)
unord_list.sort(reverse = True, key=sort_on)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print (f"Found {word_count(get_book_text(sys.argv[1]))} total words")
print("--------- Character Count -------")
for entry in unord_list:
    print (f"{entry["char"]}: {entry["num"]}")
print("============= END ===============")
