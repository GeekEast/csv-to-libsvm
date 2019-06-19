#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.

"""

import sys
import csv
import operator
from collections import defaultdict

def construct_line(line):
    new_line = []
    for i, item in enumerate(line):
        if (i == 0):
            new_line.append(item)
            continue
        else:
            if item == '' or float(item) == 0.0:
                continue
            elif item=='NaN':
                item="0.0"
            new_item = "%s:%s" % (i + 1, item)
            new_line.append(new_item)
    new_line = " ".join(new_line)
    new_line += "\n"
    return new_line

# ---

input_file = sys.argv[1]
try:
    output_file = sys.argv[2]
except IndexError:
    output_file = input_file+".out"

try:
    skip_headers = sys.argv[3]
except IndexError:
    skip_headers = 0

i = open(input_file, 'rt')
o = open(output_file, 'wb')

reader = csv.reader(i)

if skip_headers:
    headers = reader.__next__()

for line in reader:
    new_line = construct_line(line)
    o.write(new_line.encode('utf-8'))