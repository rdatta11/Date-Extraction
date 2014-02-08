Homework 1: Date-Extraction-- Leveraging NLP and Regex to extract date information from files
===============
---

**Overview:**

In this assignment the goal was to extract date information from a text file using basic Natural Language Processing techniques (NLP) including Regular Expressions (regex). Because of the various ways to represent dates it was difficult to cover all possible date combinations. I did my best to include the most common date formats.

**To Run:**

1. Install Python 2.7.6 on your UNIX based system.
2. Change the permissions on the date.py file by typing in the command line: `$: chmod a+x date.py`.
3. Execute date.py with an input test file as a command line argument. E.g.: `$: ./date.py input.txt`.
4. The output will appear in the console.

**Interpreting Output:**

Upon executing date.py there will be five different sets with dates (each set represents a different style of date formatting). Each date in a set appears in the order in which it appears in the file relative to the other dates in the set.

Please note that because of the complexities of English it is possible to get false positives (E.g. Handling the case 'mon the 21st' may result in finding the 'mon' in the word 'common'). It is also possible to get false negatives as it is not possible to cover every case for dates   
