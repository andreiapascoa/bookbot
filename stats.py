def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    list_words = file_contents.split()
    num_words = len(list_words)
    return num_words

def get_list_chars(file_contents):
    lowercase = file_contents.lower()
    list_characters = []
    for character in lowercase:
        list_characters.append(character)
    return list_characters

def set_characters(list_characters):
    seen_chars = set()
    unique_chars = []
    
    for c in list_characters:
        if c not in seen_chars:
            seen_chars.add(c)
            unique_chars.append(c)
    return unique_chars

def create_dictionary(file_contents):

    just_alpha = ""

    for c in file_contents:
        if c.isalpha():
            just_alpha += c

    lowercase_string = just_alpha.lower()
    chars_dictionary = {}
    for c in lowercase_string:
        if c in chars_dictionary:
            chars_dictionary[c] += 1
        else:
            chars_dictionary[c] = 1
    return chars_dictionary

def create_list_chars_dictionary(chars_dictionary):
    list_chars_dic = []
    for char in chars_dictionary:
        char_dic = {
            char: chars_dictionary[char]
        }
        list_chars_dic.append(char_dic)
    
    return list_chars_dic

def sort_on(items):
    for c in items:
        return c
    
def sort_list_chars(dic):
    sorted_list = create_list_chars_dictionary(dic)
    sorted_list.sort(key=sort_on)
    return sorted_list

