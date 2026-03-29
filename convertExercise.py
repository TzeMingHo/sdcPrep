import argparse


parser = argparse.ArgumentParser(
    prog="custom-word-count",
    description="A custom word count like the actual one",

)

parser.add_argument("-l", "--lines", help="Finding out how many lines in the file", action="store_true")
parser.add_argument("-w", "--words", help="Finding out how many words in the file", action="store_true")
parser.add_argument("-c", "--characters", help="Finding how many characters in the file", action="store_true")
parser.add_argument("path", help="The file to process")

args = parser.parse_args()

print(args.path)