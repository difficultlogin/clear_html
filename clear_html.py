#!/usr/bin/env python3

import sys, re
from urllib import request

def get_html(link):
    html = request.urlopen(link)
    return html.read().decode('utf-8')

def clear_html(html):
    p = re.compile(r'style=".*?"')
    return p.sub('', html)

if __name__ == '__main__':
    # Use:
    #   link - argument command line №1
    #   get_html (link) - return original html for link
    #   clear_html (html) - return clear html without attributes 'style'
    #   python3 ./clear_html.py http://testdomain.com

    try:
        link = sys.argv[1]
    except IndexError:
        print('use: ./clear_html.py {link}')
        exit()

    html = get_html(link)
    print(clear_html(html)