#!/usr/bin/python
import re
import sys

textFile = open(sys.argv[1], 'r')
fileText = textFile.read()
textFile.close()
matches = re.findall("(?:(?:jan(?:(?:.)?|(?:uary)?)|feb(?:(?:.)?|(?:ruary)?)|mar(?:(?:.)?|(?:ch)?)|apr(?:(?:.)?|(?:il)?)|may|jun(?:(?:.)?|(?:e)?)|jul(?:(?:.)?|(?:y)?)|aug(?:(?:.)?|(?:gust)?)|sep(?:(?:.)?|(?:ept(?:(?:.)?))?|(?:tember)?)|oct(?:(?:.)?|(?:ober)?)|nov(?:(?:.)?|(?:ember)?)|dec(?:(?:.)?|(?:ember)?)) (?:[123][0-9]|[1-9])[ \t\r\f\v]?(?:rd|st|th)?(?:,)?[ \t\r\f\v]?(?:[0-2][0-9][0-9][0-9])?)",fileText,re.IGNORECASE)
print matches
matches = re.findall("(?:(?:[0]?[1-9])|(?:[1][0-2]))[-/](?:(?:[012]?[0-9])|(?:[3][01]))[/-][12]?[0-9]?[0-9][0-9]",fileText, re.IGNORECASE)
print matches
matches = re.findall("(?:christmas|memorial day|labor day|halloween|new years eve|new year's eve|mothers day|mother's day|martin luther king day|presidents day|president's day|memorial day| independence day|labor day|columbus day|veterans day|valentines day|valentine's day|halloween|st. patricks day|st. patricks day|veteran's day|thanksgiving|thanksgiving day)",fileText, re.IGNORECASE)
print matches
matches = re.findall("(?:mon(?:\.|day)?|tue(?:\.|sday)?|wed(?:\.|nesday)?|thur(?:\.|sday)?|fri(?:\.|day)?|sat(?:\.|urday)?|sun(?:\.|day)?)?[ \t\r\f\v]?the (?:[123][0-9]|[1-9])?[ \t\r\f\v]?(?:rd|st|th)?(?:,)?[ \t\r\f\v]?[ \t\r\f\v]?of?[ \t\r\f\v]?(?:jan(?:\.|uary)?|feb(?:\.|ruary)?|mar(?:\.|ch)?|apr(?:\.|il)?|may|jun(?:\.|e)?|jul(?:\.|y)?|aug(?:\.|ust)?|oct(?:\.|ober)?|nov(?:\.|ember)?|dec(?:\.|ember)?),?[ \t\r\f\v]?(?:[0-2][0-9][0-9][0-9])?",fileText, re.IGNORECASE)
print matches
matches = re.findall("(?:mon(?:\.|day)?|tue(?:\.|sday)?|wed(?:\.|nesday)?|thur(?:\.|sday)?|fri(?:\.|day)?|sat(?:\.|urday)?|sun(?:\.|day)?)[ \t\r\f\v]?[t]?[h]?[e]?[ \t\f\r\v]?(?:[123][0-9]|[1-9])?[ \t\r\f\v]?(?:rd|st|th)?",fileText, re.IGNORECASE)
print matches
