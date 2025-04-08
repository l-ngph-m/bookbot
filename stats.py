def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()

    return content

def get_num_words(string):
    word_list = string.split()
    return len(word_list)

def get_char_count(string):
    char_count = {}
    for char in string.lower():
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

def sort_on(dict):
    return dict["count"]

def get_sorted_list(dict):
    sorted_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = dict[key]
        sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

