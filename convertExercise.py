import argparse
import re


parser = argparse.ArgumentParser(
    prog="custom-word-count",
    description="A custom word count like the actual one",

)

parser.add_argument("-l", "--lines", help="Finding out how many lines in the file", action="store_true")
parser.add_argument("-w", "--words", help="Finding out how many words in the file", action="store_true")
parser.add_argument("-c", "--characters", help="Finding how many characters in the file", action="store_true")
parser.add_argument("path", help="The file to process", nargs='*')

args = parser.parse_args()

filesArray = args.path

total_lines = 0
total_words = 0
total_characters = 0

total_row_numbers = []

for file_path in filesArray:

    number_of_lines = 0
    number_of_words = 0
    number_of_characters = 0

    row_numbers = []

    with open(file_path, "r") as file:
        context = file.read()
        number_of_lines = len(context.split("\n")) - 1
        # number_of_words = len(re.findall(r"\S+", context))
        number_of_words = len(list(filter(lambda char: re.match(r"\w+", char), context.split(" "))))
        number_of_characters = len(context)

        if (args.lines):
            row_numbers.append(number_of_lines)
        if (args.words):
            row_numbers.append(number_of_words)
        if (args.characters):
            row_numbers.append(number_of_characters)
        
        if (len(row_numbers) > 0):
            print(*row_numbers, file_path)
        else:
            print(number_of_lines, number_of_words, number_of_characters, file_path)
        total_lines += number_of_lines
        total_words += number_of_words
        total_characters += number_of_characters

if (len(filesArray) > 1):
    if (args.lines):
        total_row_numbers.append(total_lines)
    if (args.words):
        total_row_numbers.append(total_words)
    if (args.characters):
        total_row_numbers.append(total_characters)
    if (len(total_row_numbers) > 0):
        print(*total_row_numbers, 'total')
    else:
        print(total_lines, total_words, total_characters, 'total')




