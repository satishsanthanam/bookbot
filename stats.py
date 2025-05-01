def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        # Now we need to either increment the existing count
        # or add this character to our dictionary
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def convert_to_dict_list(dict):
    list_of_dict = [{"char": key, "num": value} for key, value in dict.items()]
    return list_of_dict

