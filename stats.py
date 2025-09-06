def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch, num in char_dict.items():
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list