def get_word_count(text):
    count = 0
    words = text.split()

    for word in words:
        count += 1

    return count


def get_char_count(text_string):
    text_string = text_string.lower()

    char_dict = {}

    for char in text_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict


def sort_on(dict):
    return dict["count"]


def sort_dict(dict):
    dict_list = []

    for char, count in dict.items():
        dict_list.append({"char": char, "count": count})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
