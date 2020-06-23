import sys
from pprint import pprint
from modules.switcher import convert

INPUT_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]


if __name__ == "__main__":
    # input_csv = from_csv(open(INPUT_FILENAME).read())
    # print(list(input_csv))
    # print(csv.list_dialects())

    result = convert(INPUT_FILENAME, OUTPUT_FILENAME)
    pprint(result)
    open(OUTPUT_FILENAME, 'w').write(result)
