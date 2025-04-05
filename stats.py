def get_num_words(contents):
    num_words=len(contents.split())
    return num_words

def count_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def char_sort(chars):
    dict_list = []
    for key in chars:
        char_dict = {}
        char_dict["char"] = key
        char_dict["num"] = chars[key]
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list