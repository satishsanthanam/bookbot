from stats import get_num_words
from stats import count_chars
from stats import sort_on
from stats import convert_to_dict_list
import sys

def get_book_text(filepath):
    file_contents = "";
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def isalpha_wrapper(char): # Assuming 'isalpha' might not be directly available
    return isinstance(char, str) and char.isalpha()

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    file_contents = get_book_text(f"{book}")
    num_words = get_num_words(file_contents)
    char_counts = count_chars(file_contents)
    char_counts_dict_list = convert_to_dict_list(char_counts)
    char_counts_dict_list.sort(reverse=True, key=sort_on)
    only_alpha_char_count_dict_list = [char_dict for char_dict in char_counts_dict_list if 'char' in char_dict and isalpha_wrapper(char_dict['char'])]

    print("========== BOOKBOT ==========\n")
    print("=====Analyzing===book found at {book}=======\n")
    print("=====Word count======\n")
    print(f"Found {num_words} total words\n")
    print("-------Character count------\n")
    for char_diction in only_alpha_char_count_dict_list:
        print(char_diction['char'] + ": " + str(char_diction['num']))
    
main()