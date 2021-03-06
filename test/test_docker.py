# -*- coding: utf-8 -*-
import json
import os
import sys

import requests

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


r = requests.get("http://localhost:8091/version/")
keys = r.json().keys()
if "version" in keys:
    print("OK")
else:
    print("error")
    sys.exit(1)


with open(os.path.join(THIS_DIR, "2000094.cif"), "r") as fh:
    f = fh.read()

r = requests.post(
    "http://localhost:8091/predictxrd", data=json.dumps({"fileContent": f})
)

keys = r.json().keys()
if "x" in keys:
    print("PXRD prediction API works")
    sys.exit(0)
else:
    print("failed")
    sys.exit(1)
