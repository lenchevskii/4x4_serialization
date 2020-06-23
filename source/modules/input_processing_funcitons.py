import csv
import json
from xmltodict import parse


def from_xml(file):
    return parse(file)


def from_json(file):
    return json.loads(file)


def from_csv(file):
    return csv.DictReader(file, dialect='unix')


def from_bin(file):
    return bytes(file, encoding='utf16')