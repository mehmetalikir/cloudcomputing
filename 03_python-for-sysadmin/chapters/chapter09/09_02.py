#!usr/bin/env python3.8

import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists ")
receipts = glob.iglob('/new/receipt-[0-9]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.strip("/")[-1]
    destination = f"./processed/{name}"
    print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $.2f" % subtotal)