import csv
import sys
from pprint import pprint
from modules.input_processing_funcitons import from_xml, from_csv
from modules.output_processing_functions import to_json, to_xml
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
    # b = b'{\n    "begindate": "2016-11-22", \n    "enddate": "2016-11-22", \n    "guids": ["6593062E-9030-B2BC-E63A-25FBB4723ECC", \n              "5A9F8478-6673-428A-8E90-3AC4CD764543", \n              "D8243BA1-0847-48BE-9619-336CB3B3C70C"]\n}'
    # pprint(b.decode())