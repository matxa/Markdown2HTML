#!/usr/bin/python3
from sys import argv
import os.path
from os import path


if len(argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    exit(1)
elif not path.exists(argv[1]):
    print("Missing {}".format(argv[1]))
    exit(1)
else:
    html_lines = []
    with open(argv[1], 'r') as src:
        lines = src.readlines()
    with open(argv[2], 'w') as dest:
        for line in lines:
            count_hash = line.count('#')
            line_no_hash = line.replace('#' * count_hash + ' ', '')
            line_no_hash = line_no_hash.replace('\n', '')
            line_html = "<h{}>{}</h{}>\n".format(
                count_hash, line_no_hash, count_hash)
            html_lines.append(line_html)
        dest.writelines(html_lines)
    exit(0)
