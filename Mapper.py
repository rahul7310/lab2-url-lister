#!/usr/bin/env python
"""mapper.py"""

import sys
import re


# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
#     # split the line into words
#     words = line.split()
#     # increase counters
#     for word in words:
#         # write the results to STDOUT (standard output);
#         # what we output here will be the input for the
#         # Reduce step, i.e. the input for reducer.py
#         #
#         # tab-delimited; the trivial word count is 1
#         print('%s\t%s' % (word, 1))


# input comes from STDIN (standard input)

html_content = sys.stdin.read()

url_pattern = r'href="([^"]*)"'
urls = re.findall(url_pattern, html_content)

for url in urls:
    print('%s\t%s' % (url, 1))
