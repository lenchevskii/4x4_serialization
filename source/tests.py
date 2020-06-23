import sys
from pprint import pprint
from modules.input_processing_funcitons import from_xml, from_json
from modules.output_processing_functions import to_json, to_xml

INPUT_FILENAME = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]

if __name__ == "__main__":
    input_xml = from_xml(INPUT_FILENAME)
    input_json = from_json(INPUT_FILENAME)
    # output_json = to_json(input_xml)
    # print(output_json)
    # open(OUTPUT_FILENAME, 'w').write(output_json)
    # output_xml = to_xml(input_xml)
    print(input_json)
    # open(OUTPUT_FILENAME, 'w').write(output_xml)