#!/usr/bin/python3
"""Markdown to HTML converter script"""
from sys import argv
import os.path
from os import path
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    # Check for Usage
    if len(argv) != 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    elif not path.exists(argv[1]):
        eprint("Missing {}".format(argv[1]))
        exit(1)

    html = []
    unordered_list = ''
    ordered_list = ''
    with open(argv[1], 'r') as src:
        lines = src.readlines()
        lines[-1] = lines[-1].replace('\n', '')
    with open(argv[2], 'w') as dest:
        for line in lines:
            # convert markdown headings ( # ) to html heading levels h1 - h6
            count_hash = line.count('#')
            if count_hash >= 1:
                line_no_hash = line.replace('#' * count_hash + ' ', '')
                line_no_hash = line_no_hash.replace('\n', '')
                line_html = "<h{}>{}</h{}>\n".format(
                    count_hash, line_no_hash, count_hash)
                html.append(line_html)

            # convert markdown unordered list to html unordered list
            elif '-' in line[0] and ' ' in line[1]:
                if '<li>' not in unordered_list:
                    unordered_list = '<ul>\n'
                line_cp = line.replace('- ', '')
                line_cp = line_cp.replace('\n', '')
                unordered_list = unordered_list + "\t<li>{}</li>\n".format(
                    line_cp)
                if lines.index(line) + 1 < len(lines):
                    if '- ' not in lines[lines.index(line) + 1]:
                        unordered_list = unordered_list + '</ul>\n'
                        html.append(unordered_list)
                        unordered_list = ''
                else:
                    unordered_list = unordered_list + '</ul>\n'
                    html.append(unordered_list)
                    unordered_list = ''

            # convert markdown ordered list to html ordered list
            elif '*' in line[0] and ' ' in line[1]:
                if '<li>' not in ordered_list:
                    ordered_list = '<ol>\n'
                line_cp = line.replace('* ', '')
                line_cp = line_cp.replace('\n', '')
                ordered_list = ordered_list + "\t<li>{}</li>\n".format(line_cp)
                if lines.index(line) + 1 < len(lines):
                    if '* ' not in lines[lines.index(line) + 1]:
                        ordered_list = ordered_list + '</ol>\n'
                        html.append(ordered_list)
                        ordered_list = ''
                else:
                    ordered_list = ordered_list + '</ol>\n'
                    html.append(ordered_list)
                    ordered_list = ''

        # write HTML to destenation file
        dest.writelines(html)
    exit(0)
