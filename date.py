#!/usr/bin/python
import re
import sys

textFile = open(sys.argv[1], 'r')
fileText = textFile.read()
textFile.close()
matches = re.findall("((?:jan|january|feb(?:(?:.)?|(?:ruary)?)|march|apr|april|may|jun|june|july|jul|aug|august|sep|sept|september|oct|october|nov|november|dec|december) (?:[12][0-9]|[1-9]))",fileText,re.IGNORECASE)
print matches
