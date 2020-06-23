import os
from modules.input_processing_funcitons import from_json, from_xml, from_csv, from_bin
from modules.output_processing_functions import to_json, to_xml, to_csv, to_bin

FROM = {
    ".json" : from_json,
    ".xml"  : from_xml,
    ".csv"  : from_csv,
    ".bin"  : from_bin
}

TO = {
    ".json" : to_json,
    ".xml"  : to_xml,
    ".csv"  : to_csv,
    ".bin"  : to_bin
}


def convert(input_filename, output_filename):
    input_extension = os.path.splitext(input_filename)[1]
    output_extension = os.path.splitext(output_filename)[1]
    input_file = open(input_filename, "r").read()
    return TO[output_extension](FROM[input_extension](input_file))
