def word_count(text):
     words = text.split()
     return len(words)

def char_count(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def to_dict_list(dict):
    dict_list = []
    for entry in dict:
        new_dict = {}
        new_dict["char"] = entry
        new_dict["num"] = dict[entry]
        dict_list.append(new_dict)
    return dict_list
    