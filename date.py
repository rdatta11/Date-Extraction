#!/usr/bin/python
import re
import sys

textFile = open(sys.argv[1], 'r')
fileText = textFile.read()
textFile.close()
matches = re.findall("(((?:jan(?:(?:.)?|(?:uary)?)|feb(?:(?:.)?|(?:ruary)?)|mar(?:(?:.)?|(?:ch)?)|apr(?:(?:.)?|(?:il)?)|may|jun(?:(?:.)?|(?:e)?)|jul(?:(?:.)?|(?:y)?)|aug(?:(?:.)?|(?:gust)?)|sep(?:(?:.)?|(?:ept(?:(?:.)?))?|(?:tember)?)|oct(?:(?:.)?|(?:ober)?)|nov(?:(?:.)?|(?:ember)?)|dec(?:(?:.)?|(?:ember)?)) (?:[123][0-9]|[1-9])[ \t\r\f\v]?(?:rd|st|th)?(?:,)?[ \t\r\f\v]?(?:[0-2][0-9][0-9][0-9])?))",fileText,re.IGNORECASE)
print matches
matches = re.findall("(?:(?:[0]?[1-9])|(?:[1][0-2]))/(?:(?:[012]?[0-9])|(?:[3][01]))/[12][0-9][0-9][0-9]",fileText, re.IGNORECASE)
print matches
matches = re.findall("
