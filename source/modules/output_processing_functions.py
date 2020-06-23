import csv
import json
import pickle
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml


def to_json(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)


def to_xml(dictionary):
    return parseString(str(dicttoxml(dictionary), 'utf-8')).toprettyxml()


def to_bin(dictionary):
    return str(pickle.dumps(dictionary))


def to_csv(dictionary):
    return ','.join(['%s:: %s' % (key, value) for (key, value) in dictionary.items()])
