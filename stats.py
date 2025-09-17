def get_num_words(text):
    words_list = text.split()

    chars_count = {}
    for letter in text:
        new_letter = letter.lower()
        if new_letter in chars_count:
            chars_count[new_letter] += 1
        else:
            chars_count[new_letter] = 1
    return len(words_list), chars_count


def on_sort_key (item):
    return item['num']

def sort_dict (dict):
    list_dict = []
    for word in dict:
        list_dict.append({"char": word, "num": dict[word]})
    
    list_dict.sort(reverse=True, key=on_sort_key)
    return list_dict
