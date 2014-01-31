#!/usr/bin/python
import re
import sys

textFile = open(sys.argv[1], 'r')
fileText = textFile.read()
textFile.close()
matches = re.findall("((?:jan(?:(?:.)?|(?:uary)?)|feb(?:(?:.)?|(?:ruary)?)|mar(?:(?:.)?|(?:ch)?)|apr(?:(?:.)?|(?:il)?)|may|jun(?:(?:.)?|(?:e)?)|jul(?:(?:.)?|(?:y)?)|aug(?:(?:.)?|(?:gust)?)|sep|sept|september|oct|october|nov|november|dec|december) (?:[12][0-9]|[1-9]))",fileText,re.IGNORECASE)
print matches
