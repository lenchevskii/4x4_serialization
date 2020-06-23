import sys
from modules.switcher import convert

INPUT_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]


if __name__ == "__main__":
    result = convert(INPUT_FILENAME, OUTPUT_FILENAME)
    open(OUTPUT_FILENAME, 'w').write(result)
