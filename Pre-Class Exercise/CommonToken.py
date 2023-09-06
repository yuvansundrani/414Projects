from nltk.tokenize import TweetTokenizer
from argparse import ArgumentParser
import sys
import string

def is_punctuation(s):
    return s in string.punctuation

def break_down_data(file_name):
    tknzr = TweetTokenizer()

    with open(file_name, "r") as file:
        file_contents = file.read().lower()

    list_of_words = tknzr.tokenize(file_contents)

    dict_to_add = {}

    for word in list_of_words:
        words_in_dict = dict_to_add.keys()

        if not is_punctuation(word):
            if word in words_in_dict:
                dict_to_add[word] = dict_to_add[word] + 1
            else:
                dict_to_add[word] = 1

    return dict_to_add


def print_correct_output(populated_dict):
    words = list(populated_dict.keys())
    nums = list(populated_dict.values())

    for i in range(10):
        max_value = max(nums)
        max_index = nums.index(max_value)

        print(f"{words[max_index]}\t{nums[max_index]}")

        words.pop(max_index)
        nums.pop(max_index)


def parse_args(args_list):
    parser = ArgumentParser(description="file name.")
    parser.add_argument(
        "file_name", type=str, help="The name of the text file to process"
    )
    args = parser.parse_args()
    return args.file_name


if __name__ == "__main__":
    try:
        file_name = parse_args(sys.argv[1:])

    except ValueError as e:
        sys.exit(str(e))

    populated_dict = break_down_data(file_name)

    print_correct_output(populated_dict)
