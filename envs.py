#!/usr/bin/python3

from os import getenv

stage = (getenv("STAGE" or "development"))

output = "We're running in %s" % stage

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)
